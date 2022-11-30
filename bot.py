lista=["estero", "laura" , "jas", "jackson", "morelo"]

while True:
    print (lista)
    print("hello my name is bot !")
    name = input("what's your name ?:").strip().capitalize()
    
    if name in lista:
        print( "hola".format(name))
        remove=input("would you like to be removed form the list (y/n)").strip().lower()

        if remove=="y":
            lista.remove(name)
        elif remove=="n":
            print("no worries")
    else:

        print( "Pinga {}".format(name))
        add=input("would you like to be added to the system (y/n)").strip().lower()
        if add == "y":
            lista.append(name)
        elif add=="n":
            print("dw{}".format(name))

