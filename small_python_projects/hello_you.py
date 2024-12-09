#ask user for name
name= input("what is your name?:")
print(name)
#ask user for age
age= input("what is your age?:")
print(age)
#ask user for city
city= input("what is your city?:")
print(city)
#ask user what they enjoy
love= input("what do you love to do?:")
print(love)
#create ouytput text
string ="your name is {} and you are {} years old. you live in {} and you love {}"
output=string.format(name,age,city,love)

#print output to screen
print(output)
