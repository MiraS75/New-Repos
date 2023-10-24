import turtle

# Создаем экземпляр черепахи
animal = turtle.Turtle()

# Рисуем тело животного
animal.pensize(3)
animal.fillcolor("yellow")
animal.begin_fill()
animal.circle(50)
animal.end_fill()

# Рисуем голову животного
animal.penup()
animal.goto(0, 60)
animal.pendown()
animal.fillcolor("yellow")
animal.begin_fill()
animal.circle(30)
animal.end_fill()

# Рисуем глаза животного
animal.penup()
animal.goto(-15, 80)
animal.pendown()
animal.fillcolor("black")
animal.begin_fill()
animal.circle(7)
animal.end_fill()

animal.penup()
animal.goto(15, 80)
animal.pendown()
animal.fillcolor("black")
animal.begin_fill()
animal.circle(7)
animal.end_fill()

# Рисуем нос животного
animal.penup()
animal.goto(0, 60)
animal.pendown()
animal.fillcolor("black")
animal.begin_fill()
animal.circle(3)
animal.end_fill()

# Рисуем уши животного
animal.penup()
animal.goto(0, 120)
animal.pendown()
animal.fillcolor("pink")
animal.begin_fill()
animal.goto(-30, 180)
animal.goto(30, 180)
animal.goto(0, 120)
animal.end_fill()

# Скрываем черепаху
animal.hideturtle()

# Завершаем рисование
turtle.done()