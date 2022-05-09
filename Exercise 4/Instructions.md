Exercise 4- First Step
0.	To use the functions we need, the following directories must be imported:

import math
import csv

1.	Define point tagged vector and 2 tagged vectors data1, data2 as follows:

point = [1, 0, 0, '?'] (an unknown tag)
data1 = [1, 1, 1, 'M']
data2 = [1, 2, 0, 'F']


2.	The two vectors data1, data2 must be printed separately from their tags so that the output looks like this:

The vector [1, 1, 1] has tag M
The vector [1, 2, 0] has tag F

3.	Given a function that calculates the Euclidean distance between two vectors. It receives two vectors, and a length that determines where to read (so you can make sure the tag doesn't read). You must calculate and print the distance between data1 and data2.

def euclideanDistance(instance1, instance2, length):
   distance = 0
   for x in range(length):
         #print ('x is ' , x)
         num1=float(instance1[x])
         num2=float(instance2[x])
         distance += pow(num1-num2, 2)
   return math.sqrt(distance)
 
4.	Enter code to read from myFile.csv file into list (you may need to
update the path).   

with open('myFile.csv', 'r') as myCsvfile:
    lines = csv.reader(myCsvfile)
    dataWithHeader = list(lines)

#put data in dataset without header line
dataset = dataWithHeader[1:]

a.	You must print the first 2 vectors of the file 
b.	The distance between the above vectors must be calculated and printed

5.	  Suppose the first vector is untagged. We'll call him a point. You must create a list called eucDistances, which contains the point-to-point distance for any other vector in the file, along with the tagging of the vector.
          The structure (object) will be:
class distClass:
    dist = -1 #distance of current point from test point
    tag = '-' #tag of current point
         The way to set up eucDistances would be:
eucDistances = [] # list of distances, will hold objects of type distClass

Helping code:

temp=dataset[1]
label=temp[-1]
d=euclideanDistance(point,temp,3)
print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
print(" and the label is " + label)
obj = distClass() #one record's distance and tag
obj.dist=d
obj.tag=label
eucDistances.append(obj)

6.	 You must sort the list you created in the previous section.
           Hint: To sort a list of distClass objects named distList, if you want to
           sort the list by distances, use the following code:    

distList.sort(key=lambda x: x.dist) 


7.	 Print all their vectors and distances from the first point.

8.	 What is the tag (tag) / category of the first record (point) with k = 1?

             9. What is the tag (category) of the first record (point) with k = 3?

Exercise 4- Step two

In the first exercise, we classified the point, “point” with values of k = 1, and also k = 3. In the second part of the exercise, we will work with one file for learning, and another for classification. Before working with the large files, we will learn from the original file, myFile (including the first line), and classify the records in the second file, myFile_test. What would be the tagging of the records in the second file with k = 3?
You can give values in the second file by the sample code:

with open('mytrain.csv', 'r') as myCsvfile2:
    lines = csv.reader(myCsvfile2)
    dataWithHeader = list(lines)

dataWithHeader[1][3] = 'F'
dataWithHeader[2][3] = 'M'

with open('mytest.csv ', 'w', newline='') as myCSVtest:
    writer = csv.writer(myCSVtest)
    writer.writerows(dataWithHeader)

Questions:
1.	Classify the myFile_test file with k = 3. Save the output to the same file
(myFile_test) based on the code above. 
 
2.	Browse the mytrain and mytest file. Notice that there are about 200 total
records of which 100 exist in the mytrain file, and another 100 in the mytest file.
 
a.	What accuracy do we get with k = 1? Save the tags as a file named
mytest1e. 
b.	What accuracy do we get with k = 7? Save the tags as a file named
mytest7e.

c.	What accuracy did we get with k = 19? Save the tags as a file named
mytest19e. 
d. Which value of k came out best?
e. Implement Manhattan distance in addition to the Euclidean distance.
    Repeat the test on the mytest file with the same files and also with k =
    1, k = 7, and k = 19. Save the file output to names: mytest1m, mytest7m
     and mytest19m      
 
f. Apply the Hamming distance in addition to the previous distances. Repeat the test on mytest file swiping with the same files and also k = 1, k = 7, and k = 19. Save the file output to names: mytest1h, mytest7h and mytest19h

g. Which combination of distance / value measure of k brings out the best
    accuracy? 

All 10 files must be submitted - one Python file and another 9 CSV files per model. It is recommended to submit everything as one zip file to the model.

Score:
40%   - correct answers
  40% -  readable and clear code
  20% -  documentation 
