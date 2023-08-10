import time

def IO_timer(epochs: int) -> float:
    f = open("timer_demo.txt", "w")
    time_start = time.time()
    for i in range(0,epochs):
        f.write(f"IO, #{i}")
    time_end = time.time()
    time_dif = time_end - time_start
    print("execution time for ",epochs," I/Os : ","{:e}".format(time_dif)," ms")
    return time_dif

def max_list_timer(epochs: int) -> float:
    a = [[1,2],[3,4]]
    time_start = time.time()
    for _ in range(0,epochs):
        max(a)
    time_end = time.time()
    time_dif = time_end - time_start
    print("execution time for finding ",epochs," 2x2 python's list max value : ","{:e}".format(time_dif)," ms")
    return time_dif

def compare_time(epochs: int):
    print("-------epochs-"+str(epochs)+"-------")
    io_time  = IO_timer(epochs)
    max_list_time = max_list_timer(epochs)
    time_dif = io_time - max_list_time
    print(f"list's max val opearation is faster than simple I/O by ","{:e}".format(time_dif), " ms")
    print("\n")

if __name__ == "__main__":
    compare_time(10)
    compare_time(100)
    compare_time(1000)
    compare_time(10000)
    compare_time(100000)
    compare_time(1000000)
