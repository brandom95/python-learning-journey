from random import choice


questions =["why fruits have color?","why are you so tall?"," why are dogs hairy ?"]

question = choice(questions)
answer=input(question).strip().lower()

while answer != "just because":
    answer=input("why?").strip().lower()
print ( "oh....ok")
 



    
