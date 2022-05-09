from typing import final
import frontier
import state
import time
import threading
import queue


def search(number):
    first = state.create(number)
    #print("this is the first state", first)
    f = frontier.create(first)
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        if(state.is_target(s)):
            return s, f, first
        ns = state.get_next(s)
        #print("the depth is ", f[4])
        for i in ns:
            frontier.insert(f, i)

    return None


#    for i in range(4, 5):
#        totalAverage = 0
#        totalDepth = 0
#        for l in range(1):
#            tic = time.perf_counter()
#            s, f = search(i)
#            toc = time.perf_counter()
#            print("final solution is ", s)
#            print("max depth is ", f[1])
#            print(f"Solution took  {toc - tic:0.4f} seconds")
#            totalAverage += len(s[1])
#            totalDepth += f[1]
#        finalList.append(totalDepth/100)
#        finalList.append(totalAverage/100)
#    for k in range(len(finalList)//2):
#        print("Average depth ", finalList[k])
#        print("Average number ", finalList[k + 1])


def worker(num, totalAverage, totalDepth):

    tic = time.perf_counter()
    s, f, first = search(3)
    toc = time.perf_counter()
    print("average ", len(s[1]))
    print("depth ", f[1])
    totalAverage.append(len(s[1]))
    totalDepth.append(f[1])
    #print("this is the first state", first)
    #print("final solution is ", s)
    #print("max depth is ", f[1])
    #print(f"Solution took  {toc - tic:0.4f} seconds for task ", num)


totalAverage = []
totalDepth = []
num = 2
threads = []
for i in range(num):
    t = threading.Thread(target=worker, args=(i, totalAverage, totalDepth))
    threads.append(t)
    t.start()

print(totalAverage)
print(totalDepth)
print("Average depth ", sum(totalDepth)/num)
print("Average number ", sum(totalAverage)/num)
