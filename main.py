# function that determines "is a palindrome" and "is not a palindrome" 

def palindrome(string):
  length = len(string)
  first = 0
  last = length -1 
  status = 1
  while(first<last):
    if(string[first]==string[last]):
      first=first+1
      last=last-1
    else:
      status = 0
      break
  return int(status)  
string = input("Enter the string: ")

print("Method 1")
status= palindrome(string)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! Try again")

palindrome("Hannah")