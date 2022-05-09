import math
import csv
import inspect

# 1.	Define point tagged vector and 2 tagged vectors data1,
#  data2 as follows:
point = [1, 0, 0, "?"]
data1 = [1, 1, 1, "M"]
data2 = [1, 2, 0, "F"]

# 2.	The two vectors data1, data2 must be printed separately
# from their tags so that the output looks like this:
def printVector(instance):
    print("The vector", instance[0:-1], "has the tag ", instance[-1])


printVector(data1)
printVector(data2)


# 3.	Given a function that calculates the Euclidean distance between two vectors.
# It receives two vectors, and a length that determines where
# to read (so you can make sure the tag doesn't read). You must calculate and print the distance between data1 and data2.
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += pow(num1 - num2, 2)
    return math.sqrt(distance)


# print out the distance between to vectors
def printVectorDistance(instance1, instance2):
    print(
        "The distance between",
        instance1,
        "and",
        instance2,
        "is",
        euclideanDistance(instance1, instance2, len(data1) - 1),
    )


printVectorDistance(data1, point)
printVectorDistance(data2, point)
# 4.	Enter code to read from myFile.csv file into list
# (you may need to update the path).

with open("myFile.csv", "r") as myCsvfile:
    lines = csv.reader(myCsvfile)
    dataWithHeader = list(lines)

# put data in dataset without header line
dataset = dataWithHeader[1:]

# print(dataset)
# a.	You must print the first 2 vectors of the file
printVector(dataset[0])
printVector(dataset[1])
# b.	The distance between the above vectors must be calculated and printed
printVectorDistance(dataset[0], point)
printVectorDistance(dataset[1], point)


# 5.	  Suppose the first vector is untagged. We'll call him a point. You must
#  create a list called eucDistances, which contains the point-to-point
# distance for any other vector in the file, along with the tagging of the vector.


class distClass:
    dist = -1  # distance of current point from test point
    tag = "-"  # tag of current point
    vector = "-"


# calculate the distacne for vectors and a point
def calculateDistOfVec(
    instance,
    point,
):
    list = []
    for index in instance:
        temp = index
        label = temp[-1]
        d = euclideanDistance(point, temp, len(temp) - 1)
        print(
            "The distances between "
            + str(point)
            + " and "
            + str(temp)
            + " is "
            + str(d)
        )
        print(" and the label is " + label)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        obj.vector = index
        list.append(obj)
    return list


def calculateDist(
    instance,
    point,
):
    list = []
    for index in instance:
        temp = index
        label = temp[-1]
        d = euclideanDistance(point, temp, len(temp) - 1)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        obj.vector = index
        list.append(obj)
    return list


eucDistances = []  # list of distances, will hold objects of type distClass
eucDistances = calculateDistOfVec(dataset, point)


# You must sort the list you created in the previous section.
eucDistances.sort(key=lambda x: x.dist)
# Print all their vectors and distances from the first point.
for index in eucDistances:
    print(
        "the distance between vector",
        index.vector[0:-1],
        "and",
        point[0:-1],
        "has the distance of",
        index.dist,
    )

# calculate the tag of a data
def calcTag(list, k):
    male = 0
    female = 0
    total = 0
    for index in list:
        if total == k:
            break
        if index.tag == "F":
            female += 1
        else:
            male += 1
        total += 1
    if male > female:
        return "M"
    return "F"


# What is the tag (tag) / category of the first record (point) with k = 1?
print("the tag of vector", point[0:-1], "when k = 1 is", calcTag(eucDistances, 1))
# What is the tag (category) of the first record (point) with k = 3?
print("the tag of vector", point[0:-1], "when k = 3 is", calcTag(eucDistances, 3))

# read from csv with header
def readFile(string):
    with open(string, "r") as myCsvfile2:
        lines = csv.reader(myCsvfile2)
        dataTest = list(lines)
        return dataTest


# write to csv with head
def writeFile(string, data):
    with open(string, "w", newline="") as myCSVtest:
        writer = csv.writer(myCSVtest)
        writer.writerows(data)


# 1.	Classify the myFile_test file with k = 3. Save the output to the same file
# (myFile_test) based on the code above.
dataTest = readFile("myFile_test.csv")
dataTrain = readFile("myFile.csv")
k = 3
for index in dataTest[1:]:
    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    print(
        "the tag of vector", index[0:-1], "when k =", k, "is", calcTag(eucDistances, k)
    )
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("myFile.csv", dataTrain)

#
# 2.	Browse the mytrain and mytest file. Notice that there are about 200 total
# records of which 100 exist in the mytrain file, and another 100 in the mytest file

# a.	What accuracy do we get with k = 1? Save the tags as a file named
# mytest1e.


dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 1
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest1e.csv", dataTrain)

# b.	What accuracy do we get with k = 7? Save the tags as a file named
# mytest7e.
dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 7
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest7e.csv", dataTrain)

# c.	What accuracy did we get with k = 19? Save the tags as a file named
# mytest19e

dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 19
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest19e.csv", dataTrain)

# calculate the accuracy of the k
def compareTest(test, list):
    correct = 0
    total = len(test) - 1
    k = -1
    for index in test[::-1]:
        if index[-1] == (list[k][-1]):
            correct += 1
        k -= 1
    return correct / total


# a.	What accuracy do we get with k = 1? Save the tags as a file named
# mytest1e.
dataTest = readFile("mytest.csv")
dataTrain = readFile("mytest1e.csv")
print(
    "The accuracy when k = 1 in Euclidean is",
    compareTest(dataTest, dataTrain),
    "percent",
)
# b.	What accuracy do we get with k = 7? Save the tags as a file named
# mytest7e.
dataTrain = readFile("mytest7e.csv")
print(
    "The accuracy when k = 7 in Euclidean is",
    compareTest(dataTest, dataTrain),
    "percent",
)
# c.	What accuracy did we get with k = 19? Save the tags as a file named
# mytest19e.
dataTrain = readFile("mytest19e.csv")
print(
    "The accuracy when k = 19 in Euclidean is",
    compareTest(dataTest, dataTrain),
    "percent",
)

# Which value of k came out best?
print("the best accuracy is when k = 7 in Euclidean")


def manhattanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += abs(num1 - num2)
    return math.sqrt(distance)


def calculateManhattanDist(
    instance,
    point,
):
    list = []
    for index in instance:
        temp = index
        label = temp[-1]
        d = manhattanDistance(point, temp, len(temp) - 1)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        obj.vector = index
        list.append(obj)
    return list


dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 1
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateManhattanDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest1m.csv", dataTrain)

# b.	What accuracy do we get with k = 7? Save the tags as a file named
# mytest7e.

dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 7
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateManhattanDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest7m.csv", dataTrain)

# c.	What accuracy did we get with k = 19? Save the tags as a file named
# mytest19e

dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 19
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateManhattanDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest19m.csv", dataTrain)

# calculate the accuracy of the k
def compareTest(test, list):
    correct = 0
    total = len(test) - 1
    k = 0
    for index in test[1:]:
        if index[-1] == (list[len(list) - total + k][-1]):
            correct += 1
        k += 1
    return correct / total


# a.	What accuracy do we get with k = 1? Save the tags as a file named
# mytest1e.
dataTest = readFile("mytest.csv")
dataTrain = readFile("mytest1m.csv")
print(
    "The accuracy when k = 1 in manhattan is",
    compareTest(dataTest, dataTrain),
    "percent",
)
# b.	What accuracy do we get with k = 7? Save the tags as a file named
# mytest7e.
dataTrain = readFile("mytest7m.csv")
print(
    "The accuracy when k = 7 in manhattan is",
    compareTest(dataTest, dataTrain),
    "percent",
)
# c.	What accuracy did we get with k = 19? Save the tags as a file named
# mytest19e.
dataTrain = readFile("mytest19m.csv")
print(
    "The accuracy when k = 19 in manhattan is",
    compareTest(dataTest, dataTrain),
    "percent",
)

# Apply the Hamming distance in addition to the previous distances.
def hammingDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        if num1 != num2:
            distance += 1
    return distance


def calculateHammingDist(
    instance,
    point,
):
    list = []
    for index in instance:
        temp = index
        label = temp[-1]
        d = hammingDistance(point, temp, len(temp) - 1)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        obj.vector = index
        list.append(obj)
    return list


dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 1
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateHammingDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest1h.csv", dataTrain)

# b.	What accuracy do we get with k = 7? Save the tags as a file named
# mytest7e.

dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 7
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateHammingDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest7h.csv", dataTrain)

# c.	What accuracy did we get with k = 19? Save the tags as a file named
# mytest19e

dataTest = readFile("mytest.csv")
dataTrain = readFile("mytrain.csv")
k = 19
for index in dataTest[1:]:

    eucDistances = []  # list of distances, will hold objects of type distClass
    eucDistances = calculateHammingDist(dataTrain[1:], index)
    eucDistances.sort(key=lambda x: x.dist)
    index[-1] = calcTag(eucDistances, k)
    dataTrain.append(index)

writeFile("mytest19h.csv", dataTrain)


# a.	What accuracy do we get with k = 1? Save the tags as a file named
# mytest1e.
dataTest = readFile("mytest.csv")
dataTrain = readFile("mytest1h.csv")
print(
    "The accuracy when k = 1 in hamming is", compareTest(dataTest, dataTrain), "percent"
)
# b.	What accuracy do we get with k = 7? Save the tags as a file named
# mytest7e.
dataTrain = readFile("mytest7h.csv")
print(
    "The accuracy when k = 7 in hamming is", compareTest(dataTest, dataTrain), "percent"
)
# c.	What accuracy did we get with k = 19? Save the tags as a file named
# mytest19e.
dataTrain = readFile("mytest19h.csv")
print(
    "The accuracy when k = 19 in hamming is",
    compareTest(dataTest, dataTrain),
    "percent",
)


# Which combination of distance / value measure of k brings out the best
#    accuracy?

print("the best combination is Euclidean when k = 7 at 92 percent accuracy ")
