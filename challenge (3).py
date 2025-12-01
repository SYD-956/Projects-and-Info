import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_triangle(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_water_tank():
    turtle.bgcolor("lightblue")

def draw_rock():
    draw_circle("gray", -150, -150, 50)

def draw_sign():
    x, y = 150, -120
    draw_rectangle("green", x, y, 60, 40)
    turtle.penup()
    turtle.goto(x + 10, y + 10)
    turtle.pendown()
    turtle.color("black")
    turtle.write("RUN", font=("Arial", 12, "bold"))

def draw_fish1():
    # Big red fish
    body_color = "red"
    body_radius = 40
    x, y = -50, 0
    draw_circle(body_color, x, y, body_radius)
    # fish tail 
    draw_triangle(body_color, x + body_radius, y, 50)
    # fish eye
    draw_circle("white", x - 15, y + 15, 5)
    draw_circle("black", x - 15, y + 15, 2)

def draw_fish2():
    #Small blue fish 
    body_color = "blue"
    body_radius = 25
    x, y = 100, 50
    draw_circle(body_color, x, y, body_radius)
    # fish tail 
    draw_triangle(body_color, x + body_radius, y, 30)
    # fish eye
    draw_circle("white", x - 10, y + 10, 3)
    draw_circle("black", x - 10, y + 15, 1.5)

def draw_bubbles():
    # Big fish bubbles 
    for i in range(3):
        draw_circle("white", -100 + i*15 , 60 + i*30, 5)
    # Small fish bubbles
    for i in range (3):
        draw_circle("white", 150 + i*10, 100 + i*25, 4)

def draw_water_scene():
    draw_water_tank()
    draw_fish1()
    draw_fish2()
    draw_bubbles()
    draw_rock()
    draw_sign()
    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    draw_water_scene()
