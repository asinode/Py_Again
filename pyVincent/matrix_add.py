#!/home/as/anaconda2/bin/python

# Somehow, this one was a bit easier than the first exercise. This is done!
import numpy as np

print "Matrix Addition\n==============="
print "We need a few things from you. \nYou will give us the dimensions as well as the values for both matrices.\n"
#---------------------------------------------------------------#
print "Matrix-1:\n---------"

rows1 = input("How many rows you would like in your first matrix? ")
cols1 = input("How many columns you would like in your first matrix? ")
values1 = rows1 * cols1
print "The matrix you have chosen is, ", rows1, "x", cols1, "matrix with ", rows1, "rows and ", cols1, "columns, and totally ", values1, "elements inside the matrix."
list1 = []
for i in range(values1):
    x = input("Enter your Value-")
    print "This is your Value-", i
    list1.append(x)

matrix1 = np.asarray(list1)
matrix1 = matrix1.reshape(rows1, cols1)
print "This is your first matrix: \n", matrix1
#---------------------------------------------------------------#
print "Matrix-2:\n---------"

rows2 = input("How many rows you would like in your second matrix? ")
cols2 = input("How many columns you would like in your second matrix? ")
values2 = rows2 * cols2
print "The matrix you have chosen is, ", rows2, "x", cols2, "matrix with ", rows2, "rows and ", cols2, "columns, and totally ", values2, "elements inside the matrix."
list2 = []
for i in range(values2):
    x = input("Enter your Value-")
    print "This is your Value-", i
    list2.append(x)

matrix2 = np.asarray(list2)
matrix2 = matrix2.reshape(rows2, cols2)
print "This is your second matrix: \n", matrix2
#---------------------------------------------------------------#
print "Adding your matrices ...\n------------------------"
resultant = matrix1 + matrix2
print "Matrix-1 \n", matrix1, "\n+ \nMatrix-2 \n", matrix2, "\n= \nResultant Matrix \n", resultant
