films = {
    "Ar":[3,5],
     "Er":[18,5],
     "Movie3":[15,5],
     "Movie4":[12,5]
    }

while True:
    choice = input("which movie would you like to watch?:").strip().title()

    if choice in films:
        age=int(input("how old are you?").strip())

        #check user age
        
        if age>=films[choice][0]:
            #check enough seats
            seats=films[choice][1]


            
            if seats>0:
                print("enjoy")
                films[choice][1] = films[choice][1]-1
            else:
                print("sorry")
        else:
            print("you're not old enought")
    else:
        print("we dont have that film ")
