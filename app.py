import turtle

pen = turtle.Turtle()
pen.speed(0)
screen = turtle.Screen()
screen.bgcolor("#111")

def draw_petal(t, radius, angle):
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

def draw_flower(t, num_petals, petal_radius, petal_angle, center_radius, petal_color, center_color):
    t.fillcolor(petal_color)
    t.begin_fill()
    for _ in range(num_petals):
        draw_petal(t, petal_radius, petal_angle)
        t.left(360 / num_petals)
    t.end_fill()
    t.penup()
    t.goto(0, -center_radius)
    t.pendown()
    t.fillcolor(center_color)
    t.begin_fill()
    t.circle(center_radius)
    t.end_fill()

# 🌸 Flor de cerezo
draw_flower(pen, 5, 100, 60, 25, "#ffb6c1", "#ff69b4")

pen.hideturtle()
turtle.done()
