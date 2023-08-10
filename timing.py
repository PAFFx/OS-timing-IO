import time

def IO_timer(total_IO: int):
    f = open("timer_demo.txt", "w")
    time_start = time.time()
    for i in range(0,total_IO):
        f.write(f"IO, #%d" %i)
    time_end = time.time()
    print("execution time for ",total_IO,"I/O : ",time_end-time_start," ms")


if __name__ == "__main__":
    IO_timer(0)
    IO_timer(10)
    IO_timer(100)
    IO_timer(1000)
    IO_timer(int(1e3))
    IO_timer(int(1e4))
    IO_timer(int(1e3))
    IO_timer(int(1e3))
    IO_timer(int(1e3))
    IO_timer(int(1e3))
    IO_timer(int(1e3))
    IO_timer(int(1e3))
    IO_timer(int(1e3))
    IO_timer(int(1e3))
    
    
