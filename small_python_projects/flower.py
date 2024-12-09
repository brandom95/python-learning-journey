import turtle

def triangle(flow):
    for i in range (1,2):
        flow.left(45)
        flow.forward(50)
        flow.left(200)
        flow.forward(50)
        

def flower():
    window = turtle.Screen()
    window.bgcolor("red")
    brand = turtle.Turtle()
    brand.shape("turtle")
    brand.color("yellow")
    brand.speed(200)
    for i in range (1,60):
        triangle(brand)
        brand.left(10)
        
    brand.right(90)
    brand.forward(10)
    brand.right(285)
    brand.forward(200)

    

flower()
        
