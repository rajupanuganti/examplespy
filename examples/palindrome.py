value  = input("Enter the String to check for palindrome : ")
 
reverseval = value[::-1]
 
if value == reverseval :
    print("Yes it is palindrome")
else:
    print("No it is Not a palindrome")