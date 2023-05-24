import atexit
import sys
import time

def cleanup():
     timeout_sec = 5
     for p in all_processes: # list of your processes
         p_sec = 0
         for second in range(timeout_sec):
             if p.poll() == None:
                 time.sleep(1)
                 p_sec += 1
         if p_sec >= timeout_sec:
             p.kill() # supported from python 2.6
     print('cleaned up!')
atexit.register(cleanup)
sys.exit()