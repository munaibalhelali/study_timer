#!/usr/bin/env python3

class Session:
    def __init__(self, start=None):
        self.start_time = start
        self.end_time = None 
        self.total_breaks = 0 
        self.alive = True 
        
    def set_start_time(self, start):
        self.start_time = start 

    def set_end_time(self, end):
        self.end_time = end
        self.alive = False 

    def add_break(self, start, end):
        break_duration = end - start
        self.total_breaks += break_duration 

    def get_start_time(self):
        return self.start_time 

    def get_end_time(self):
        return self.end_time

    def get_total_breaks(self):
        return self.total_breaks 