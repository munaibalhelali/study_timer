#!/usr/bin/env python3
import time
from threading import Timer as TM 

class Timer:
    def __init__(self):
        self.start_time = None
        self.duration = 0
        self.count_down_time = 0
        self.paused = False 
        self.started = False
        self.count_down = False  

    def start(self):
        self.start_time = time.time()
        self.paused = False
        self.started = True

    def initalize_count_down(self, time_in_sec):
        self.count_down_time = time_in_sec
        self.start_time = time.time()
        self.count_down = True

    def pause(self):
        self.paused = True

    def continue_timer(self):
        self.paused = False 
        self.start_time = time.time() - self.duration

    def stop(self):
        self.reset()
        self.paused = True
        self.count_down = False

    def reset(self):
        self.start_time = time.time()
        self.duration = 0
        self.paused = False 
        self.started = False

    def get_timer_duration(self):
        return self.duration

    def get_formated_timer_duration(self):
        t = self.duration if not self.count_down else (self.count_down_time-self.duration)
        H = int(t//3600)
        M = int((t%3600)//60)
        S = int((t%3600)%60)
        time_str = "%02d:%02d:%02d" % (H, M, S)
        return time_str

    def update(self):
        if not self.paused and self.started:
            self.duration = time.time() - self.start_time
            if self.count_down:
                if self.count_down_time - self.duration <= 0:
                    self.stop()
