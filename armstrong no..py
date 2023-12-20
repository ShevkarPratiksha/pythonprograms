# write a program to accept a number and print whether it is  Armstrong no or not
# 153  1*1*1+5*5*5+3*3*3 = 153 Armstrong number
# 164  1*1*1+6*6*6+4*4*4 = 164 not armstrong number
# 370  3*3*3+7*7*7+0= 370  Armstrong Number

no=int(input("Enter any Number"))
P=no
sum=0
while no>0:
    d=no%10
    sum=sum+d*d*d
    no=no//10
if P==sum:
    print( " Armstrong")
else:
    print ("Not Armstrong")
