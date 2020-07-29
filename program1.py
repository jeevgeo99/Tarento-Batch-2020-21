##1.Write a program to print the sum of cubes of even digits in a given number. 


num = input("Enter the number : ")##Input the number
sum = 0##sum is initialized to zero
for i in num:
    x = int(i)
    if(x%2==0):##Checking whether it is even
        sum += x**3##sum of cubes
print("Sum of cubes of even digits in this given number is : ", sum  )