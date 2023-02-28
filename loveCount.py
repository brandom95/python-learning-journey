
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


x= name1.lower()
y= name2.lower()

F= x.count('t') + x.count('r')+ x.count('u')+ x.count('e')
S= y.count('t') + y.count('r')+ y.count('u')+ y.count('e')
T= x.count('l') + x.count('o')+ x.count('v')+ x.count('e')
C= y.count('l') + y.count('o')+ y.count('v')+ y.count('e')

prim= F+S 
sec= T+C
ter = int(str(prim) + str(sec))

if ter < 10 or ter > 90 :
    print (f"Your score is {ter}, you go together like coke and mentos.")

elif ter > 40 and ter < 50 : 
    print(f"Your score is {ter}, you are alright together.")

else:
    print (f"Your score is {ter}.")

