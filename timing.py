import time

def IO_timer(total_IO:int):
    time_start = time.time()
    for i in range(0,total_IO):
        print("IO #",i)
    time_end = time.time()
    print("execution time for ",total_IO,"I/O : ",time_end-time_start," ms")


if __name__ == "__main__":
    IO_timer(0)
    IO_timer(1)
    IO_timer(2)
    IO_timer(3)
    IO_timer(4)
    IO_timer(5)
    IO_timer(6)
    IO_timer(7)
    
    
