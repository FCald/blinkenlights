# -*- coding: utf-8 -*

from tinkerforge.bricklet_multi_touch import MultiTouch
from tinkerforge.bricklet_dual_button import DualButton

import termios
import fcntl
import sys
import os

from Queue import Queue
from threading import Thread

from repeated_timer import RepeatedTimer

import config

class MultiTouchInput:
    current_state = 0
    current_state_counter = [0]*12

    def __init__(self, ipcon, key_queue):
        self.UID = config.UID_MULTI_TOUCH_BRICKLET
        if self.UID == None:
            self.mt = None
            print("Not Configured: Multi Touch")
            return
            
        self.key_queue = key_queue
        self.ipcon = ipcon
        self.mt = MultiTouch(self.UID, self.ipcon)
        try:
            self.mt.get_electrode_sensitivity()
            print("Found: Multi Touch ({0})").format(self.UID)
        except:
            print("Not Found: Multi Touch ({0})").format(self.UID)
            self.UID = None
            return

        self.mt.register_callback(self.mt.CALLBACK_TOUCH_STATE, self.cb_touch_state)
        
        self.touch_timer = RepeatedTimer(0.1, self.touch_tick)

    def state_to_queue(self, state):
        for item in config.KEYMAP_MULTI_TOUCH.items():
            if state & (1 << item[0]):
                self.key_queue.put(item[1])
    
    def touch_tick(self):
        state = 0
        for i in range(12):
            if self.current_state & (1 << i):
                self.current_state_counter[i] += 1
            else:
                self.current_state_counter[i] = 0

            if self.current_state_counter[i] > 5:
                state |= (1 << i)

        self.state_to_queue(state)

    def cb_touch_state(self, state):
        changed_state = self.current_state ^ state
        self.current_state = state

        self.state_to_queue(changed_state & self.current_state)

    def read_single_keypress(self):
        return self.key_queue.get()

class DualButtonInput:
    current_state = 0
    current_state_counter = [0]*4

    def __init__(self, ipcon, key_queue):
        self.UID = config.UID_DUAL_BUTTON_BRICKLET
        if self.UID[0] == None:
            print("Not Configured: Dual Button 1")
        if self.UID[1] == None:
            print("Not Configured: Dual Button 2")
            
        self.key_queue = key_queue

        self.ipcon = ipcon
        
        if self.UID[0] != None:
            self.db1 = DualButton(self.UID[0], self.ipcon)
        else:
            self.db1 = None
            
        if self.UID[1] != None:
            self.db2 = DualButton(self.UID[1], self.ipcon)
        else:
            self.db2 = None
        
        if self.db1 != None:
            try:
                self.db1.get_button_state()
                print("Found: Dual Button 1 ({0})").format(self.UID[0])
            except:
                print("Not Found: Dual Button 1 ({0})").format(self.UID[0])
                self.UID = (None, self.UID[1])
        
        if self.db2 != None:
            try:
                self.db2.get_button_state()
                print("Found: Dual Button 2 ({0})").format(self.UID[1])
            except:
                print("Not Found: Dual Button 2 ({0})").format(self.UID[1])
                self.UID = (self.UID[0], None)

        if self.db1 != None:
            self.db1.register_callback(self.db1.CALLBACK_STATE_CHANGED, self.cb_state_changed1)
        if self.db2 != None:
            self.db2.register_callback(self.db2.CALLBACK_STATE_CHANGED, self.cb_state_changed2)
        
        self.press_timer = RepeatedTimer(0.1, self.press_tick)

    def cb_state_changed1(self, button_l, button_r, led_l, led_r):
        l = button_l == DualButton.BUTTON_STATE_PRESSED
        r = button_r == DualButton.BUTTON_STATE_PRESSED
        state = (l << 0) | (r << 1)

        changed_state = (self.current_state ^ state) & 0b0011
        self.current_state = state

        self.state_to_queue(changed_state & self.current_state)

    def cb_state_changed2(self, button_l, button_r, led_l, led_r):
        l = button_l == DualButton.BUTTON_STATE_PRESSED
        r = button_r == DualButton.BUTTON_STATE_PRESSED
        state = (l << 2) | (r << 3)

        changed_state = (self.current_state ^ state) & 0b1100
        self.current_state = state

        self.state_to_queue(changed_state & self.current_state)

    def state_to_queue(self, state):
        for item in config.KEYMAP_DUAL_BUTTON.items():
            if state & (1 << item[0]):
                self.key_queue.put(item[1])
    
    def press_tick(self):
        state = 0
        for i in range(4):
            if self.current_state & (1 << i):
                self.current_state_counter[i] += 1
            else:
                self.current_state_counter[i] = 0

            if self.current_state_counter[i] > 1:
                state |= (1 << i)

        self.state_to_queue(state)

    def read_single_keypress(self):
        return self.key_queue.get()

class KeyBoardInput:
    def __init__(self, key_queue):
        self.key_queue = key_queue
        self.fd = sys.stdin.fileno()
        self.loop = True

        self.prepare_stdin()

        self.thread = Thread(target = self.keyboard_loop)
        self.thread.start()
    
    def prepare_stdin(self):
        # save old state
        self.flags_save = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        self.attrs_save = termios.tcgetattr(self.fd)

        # copy the stored version to update
        attrs = list(self.attrs_save)

        # iflag
        attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK 
                      | termios.ISTRIP | termios.INLCR | termios. IGNCR 
                      | termios.ICRNL | termios.IXON )

        # cflag
        attrs[2] &= ~(termios.CSIZE | termios. PARENB)
        attrs[2] |= termios.CS8

        # lflag
        attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                      | termios.ISIG | termios.IEXTEN)
        termios.tcsetattr(self.fd, termios.TCSANOW, attrs)

        # turn off non-blocking
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.flags_save & ~os.O_NONBLOCK)

    def restore_stdin(self):
        self.loop = False
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.attrs_save)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.flags_save)

    def keyboard_loop(self):
        while self.loop:
            try:
                self.key_queue.put(sys.stdin.read(1)) # read single character
            except KeyboardInterrupt: 
                pass 

class KeyPress:
    key_queue = Queue()

    def __init__(self, ipcon):
        self.mti = MultiTouchInput(ipcon, self.key_queue)
        self.dbi = DualButtonInput(ipcon, self.key_queue)
#       Don't use keyboard input in gui demo
#       self.kbi = KeyBoardInput(self.key_queue)

    def read_single_keypress(self):
        return self.key_queue.get()