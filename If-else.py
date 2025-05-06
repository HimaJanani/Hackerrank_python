#PROGRAM CODE
n = int(input())
if n % 2 == 1 : # % represent is odd
    print("Weird")
elif n<=6:
    print("Not Weird")
elif n<=20:
    print("Weird")
else:
    print("Not Weird")


#QUESTION
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  2to5 , print Not Weird
If  is even and in the inclusive range of  6to20 , print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
