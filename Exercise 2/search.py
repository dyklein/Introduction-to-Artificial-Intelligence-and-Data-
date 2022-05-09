# search
# זהו הפתרון של תרגיל 1 והוא מימוש בפייתון לפסיאודוקוד שהוצג בכיתה
from threading import Thread
from time import sleep
import queue
import state
import frontier
import operator
import math


def search(n):
    start_state = state.create(n)
    # print(s)
    f = frontier.create(start_state)
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        if state.is_target(s):
            return start_state, s, f
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f, i)
    return 0


"""
start_state, s, f = search(2)
print("start state is", start_state, "\nthe end state is ", s,
      "\ntotal states in the frontier is ", f[1], "\ntotal states went through is ", f[2])
"""
"""
place_holer = 0
times_to_run = 1
total = [0]
for i in range(times_to_run):
    start, result = search(3)
    print(i, "th start state is \n", start)
    print(i, "th result is \n", result)
    total[place_holer] += result[2]


place_holer += 1
total.append(0)
for i in range(times_to_run):
    start, result = search(2)
    print(i, "th start state is \n", start)
    print(i, "th result is \n", result)
    total[place_holer] += result[2]

print("average moves for 3 is ", total[0]/times_to_run)
print("average moves for 4 is ", total[1]/times_to_run)

"""
queue_of_items = queue.Queue()


def threaded_function(arg):
    start_state = state.create(arg)
    # print(s)
    f = frontier.create(start_state)
    while not frontier.is_empty(f):
        result_state = frontier.remove(f)
        if state.is_target(result_state):
            queue_of_items.put(start_state)
            queue_of_items.put(result_state)
            if(result_state[1] == ''):
                queue_of_items.put(0)
            else:
                queue_of_items.put(result_state[2])
            queue_of_items.put(f[1])
            queue_of_items.put(f[2])
            return
        ns = state.get_next(result_state)
        for i in ns:
            frontier.insert(f, i)
    return 0


place_holer = 0
times_to_run = 100
total = [0]

for i in range(times_to_run):
    thread = Thread(target=threaded_function, args=(3, ))
    thread2 = Thread(target=threaded_function, args=(3, ))
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()

counter = 0
while not queue_of_items.empty():
    temp = queue_of_items.get()
    if(counter == 0):
        print("start state is", temp)
    elif(counter == 1):
        print("the end state is ", temp)
    elif(counter == 2):
        total[place_holer] += temp
    elif(counter == 3):
        print("total states in the frontier is ", temp)
    else:
        print("total states went through is ", temp)
        counter = -1
    counter += 1

place_holer += 1
total.append(0)
for i in range(times_to_run):
    thread = Thread(target=threaded_function, args=(4, ))
    thread2 = Thread(target=threaded_function, args=(4, ))
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()

counter = 0
while not queue_of_items.empty():
    temp = queue_of_items.get()
    if(counter == 0):
        print("start state is", temp)
    elif(counter == 1):
        print("the end state is ", temp)
    elif(counter == 2):
        total[place_holer] += temp
    elif(counter == 3):
        print("total states in the frontier is ", temp)
    else:
        print("total states went through is ", temp)
        counter = -1
    counter += 1

print("Average amount of steps take in the 3x3 board",
      total[0]/(times_to_run*2))
print("Average amount of steps take in the 4x4 board",
      total[1]/(times_to_run*2))
