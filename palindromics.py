n=1111
n1=n
rev = 0
while ( n!=0 ):
    rem = n%10
    rev = (rev*10) +rem
    n= n//10

if (n1==rev):
    print("palindrome")

else:
    print("not palindrome")
