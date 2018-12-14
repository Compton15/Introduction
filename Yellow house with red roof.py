# draw a yellow house with red roof

from turtle import *

fillcolor("yellow")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

penup()
forward(100)
left(90)
forward(100)
left(90)
forward(100)

pendown()
fillcolor("red")
begin_fill()
right(120)
forward(100)
right(120)
forward(100)
end_fill()



