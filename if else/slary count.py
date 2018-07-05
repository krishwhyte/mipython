print 'enter your salary amount, in Rs.'
salary=input()


if salary < 100000:
    tax=100
    print 'tax on salary amount', tax
else:
    tax = 0.1*salary
    print 'Tax = ', tax

