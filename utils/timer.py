import time

def start_timer():
  global start
  start = time.time()
  return start

def stop_timer():
  return time.time() - start