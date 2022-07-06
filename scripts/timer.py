#!/usr/bin/env python3
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.loops = []
        self.prev_loop_time = None 

    def start(self):
        self.start_time = time.time()
        self.prev_loop_time = time.time()

    def record_loop(self):
        if self.start_time is None:
            self.start()
        loop = time.time() - self.prev_loop_time 
        self.loops.append(loop)
        self.prev_loop_time = time.time()

    def reset(self):
       self.start_time = time.time()

    def get_timer_duration(self):
        if self.start_time is None:
            self.start()
        return time.time() - self.start_time

    def get_formated_timer_duration(self):
        if self.start_time is None:
            self.start()
        t = time.time() - self.start_time
        H = int(t//3600)
        H = f'{H}' if H > 9 else f'0{H}'
        M = int((t%3600)//60)
        M =  f'{M}' if M > 9 else f'0{M}'
        S = int((t%3600)%60)
        S =  f'{S}' if S > 9 else f'0{S}'
        str_time = f'{H}:{M}:{S}'
        return str_time



