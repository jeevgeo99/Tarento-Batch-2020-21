"""
2.Accept a String input from the stdin or file
- Print the count of words in the String. Space is assumed to be the separator between words
- Print the count of alphabets & numbers in the String
"""



from re import findall##importing findall function from regular expression library
 
x=input("Enter the string : ")##input the string
alp=findall("[a-zA-Z]",x)##finding alphabets
num=findall("[0-9]",x)##finding digits
print("Total Words -",len(x.split()))##printing the total words
print("Alphabets-",len(alp))##printing count of alphabets
print("Numbers-",len(num))##printing count of numbers in the string