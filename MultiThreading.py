import threading
import time
from threading import *

def cal_square(start,end):
    for n in range (1,10000):
        time.sleep(0.2)
        print("Square of", n, "is:", n * n)

if __name__ == "__main__":
    
    start = time.perf_counter()
    end = time.perf_counter()

    thread = threading.Thread(target=cal_square, args=(start, end ))
    thread.start()
    thread.join()
    
    total_time = end - start

    print("Total time:", total_time)