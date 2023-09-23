# 1. Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.


user_input = int(input("Enter any number: "))
print("Number is: ",user_input)
new_number = lambda i : i + 25
print("Number after adding 25: ",new_number(user_input))


# 2. Write a Python program to triple all numbers of a given list of integers. Use Python map.


lst = [1,2,3,4,5,6,7]
print("Original list: ",lst)
res = list(map(lambda i : i * 3, lst))
print("New list: ",res)


# 3. Write a Python program to square the elements of a list using map() function.


lst = [4,5,2,9]
print("Original list: ",lst)
res = list(map(lambda i : i ** 2, lst))
print("New list: ",res)


