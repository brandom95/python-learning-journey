import random
health = 50
difficulty_levels=[1 , 2 , 3 ]
difficulty=3
potion_health = int(random.randint(25,50)/difficulty)

health=(health+potion_health)
print ("your character now have " + str(health) + " hp")
