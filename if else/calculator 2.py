print 'enter a no?',
a=input()

print 'enter another no?',
b=input()

print 
print 'MENU'
print '1.Add'
print '2.Subtract'
print '3.Multiply'
print 'Choice?',
choice=input()
print


if choice==1 :
    ans = a+b
    print 'Sum =', ans
else:
    if choice==2:
        ans= a-b
        print 'difference=',ans
    else:
        if choice==3:
            ans=a*b
            print 'Product =', ans

print 'Done!'
