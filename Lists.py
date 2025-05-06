#PROGRAM CODE
# Initialize empty list
my_list = []

# Read number of commands
n = int(input())

# Process each command
for _ in range(n):
    command = input().split()
    
    if command[0] == "insert":
        i = int(command[1])
        e = int(command[2])
        my_list.insert(i, e)
        
    elif command[0] == "print":
        print(my_list)
        
    elif command[0] == "remove":
        e = int(command[1])
        my_list.remove(e)
        
    elif command[0] == "append":
        e = int(command[1])
        my_list.append(e)
        
    elif command[0] == "sort":
        my_list.sort()
        
    elif command[0] == "pop":
        my_list.pop()
        
    elif command[0] == "reverse":
        my_list.reverse()


#QUESTION
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e .
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
