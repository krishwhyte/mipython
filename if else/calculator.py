print 'enter a n=',
a=input()

print 'enter another no=',
b=input()

print 
print 'MENU'
print '1.Add'
print '2.Subtract'
print '3.Multiply'
print 'YOU HAVE TO CHOOSE ONE OF THE GIVEN NUMBERS'
print 'you have chosen=',
choice=input()
print


if choice==1:
   ans=a+b
   print 'ADDITION=', ans
    

if choice==2:
    ans= a-b
    print 'SUBTRACTION=', ans
   

if choice==3:
    ans=a*b
    print 'MULTIPLICATION =', ans

