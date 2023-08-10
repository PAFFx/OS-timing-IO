import time
import numpy as np

def IO_timer(epochs: int):
    f = open("timer_demo.txt", "w")
    time_start = time.time()
    for i in range(0,epochs):
        f.write(f"IO, #%d" %i)
    time_end = time.time()
    print("execution time for ",epochs," I/Os : ",time_end-time_start," ms")

def matrix_mul_timer(epochs: int):
    a = np.ndarray(4);
    a.reshape(2,2)
    time_start = time.time()
    for _ in range(0,epochs):
        a.max()
    time_end = time.time()
    print("execution time for finding ",epochs," 2x2 matrix max value : ",time_end-time_start," ms")


if __name__ == "__main__":
    IO_timer(10)
    matrix_mul_timer(10)
    IO_timer(100)
    matrix_mul_timer(100)
    IO_timer(1000)
    matrix_mul_timer(1000)
