import time

def IO_timer(epochs: int):
    f = open("timer_demo.txt", "w")
    time_start = time.time()
    for i in range(0,epochs):
        f.write(f"IO, #%d" %i)
    time_end = time.time()
    time_dif = time_end - time_start
    print("execution time for ",epochs," I/Os : ","{:e}".format(time_dif)," ms")

def max_list_timer(epochs: int):
    a = [[1,2],[3,4]]
    time_start = time.time()
    for _ in range(0,epochs):
        max(a)
    time_end = time.time()
    time_dif = time_end - time_start
    print("execution time for finding ",epochs," 2x2 python's list max value : ","{:e}".format(time_dif)," ms")


if __name__ == "__main__":
    IO_timer(10)
    max_list_timer(10)
    IO_timer(100)
    max_list_timer(100)
    IO_timer(1000)
    max_list_timer(1000)
    IO_timer(10000)
    max_list_timer(10000)
    IO_timer(100000)
    max_list_timer(100000)
    IO_timer(1000000)
    max_list_timer(1000000)
