import time

def IO_timer(epochs: int) -> float:
    f = open("timer_demo.txt", "w")
    time_start = time.time()
    for i in range(0,epochs):
        f.write(f"IO timer: IO number{i}\n")
    time_end = time.time()
    time_dif = time_end - time_start
    print("execution time for ",epochs," I/Os : ","{:e}".format(time_dif)," ms")
    return time_dif

def recurse_timer(epochs: int) -> float:
    time_start = time.time()
    recurse(0, epochs)
    time_end = time.time()
    time_dif = time_end - time_start
    print("execution time for",epochs,"recursive function : ","{:e}".format(time_dif)," ms")
    return time_dif

def recurse(current: int, target: int):
    if (current == target):
        return
    recurse(current+1, target)

def compare_time(epochs: int):
    print("-------epochs-"+str(epochs)+"-------")
    io_time  = IO_timer(epochs)
    recusive_time = recurse_timer(epochs)
    time_dif = io_time - recusive_time
    print(f"recursive function is faster than simple I/O by ","{:e}".format(time_dif), " ms")
    print("\n")

if __name__ == "__main__":
    compare_time(10)
    compare_time(20)
    compare_time(30)
    compare_time(100)
