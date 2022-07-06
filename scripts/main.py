#!/usr/bin/env python3
import timer 

def main():
    t1 = timer.Timer()
    command = None 
    while command != 'Q':
        command = input('Enter your command \n[1] Start timer\n[2] Show elapsed time\n[Q] Quit\nYour choice: ')
        if(command == '1'):
            t1.start()
        elif(command == '2'):
            print(t1.get_formated_timer_duration())
        else:
            continue

if __name__ == '__main__':
    main()
    