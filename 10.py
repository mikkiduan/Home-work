import turtle



turtle.setup(400,500)

wn = turtle.Screen()

wn.title("Tess becomes a traffic light!")

wn.bgcolor("lightgreen")

tess = turtle.Turtle()





def draw_housing():

    tess.pensize(3)

    tess.color("black", "darkgrey")6

    tess.begin_fill()

    tess.forward(80)

    tess.left(90)

    tess.forward(200)

    tess.circle(40, 180)

    tess.forward(200)

    tess.left(90)

    tess.end_fill()





draw_housing()
tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
state_num = 0

def advance_state_machine():

    global state_num

    if state_num == 0:

        tess.forward(70)

        tess.fillcolor("orange")

        state_num = 1

        wn.ontimer(advance_state_machine, 100)

    elif state_num == 1:

        tess.forward(70)

        tess.fillcolor("red")

        wn.ontimer(advance_state_machine, 1000)

        state_num = 2

    else:

        tess.back(140)

        tess.fillcolor("green")

        wn.ontimer(advance_state_machine, 1000)

        state_num = 0





advance_state_machine()

wn.listen()

wn.mainloop()

import turtle  # Tess becomes a traffic light.

turtle.setup(400, 500)

wn = turtle.Screen()

wn.title("Tess becomes a traffic light!")

wn.bgcolor("lightgreen")

tess = turtle.Turtle()

yoga = turtle.Turtle()

miki = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """

    tess.pensize(3)

    tess.color("black", "darkgrey")

    tess.begin_fill()

    tess.forward(80)

    tess.left(90)

    tess.forward(200)

    tess.circle(40, 180)

    tess.forward(200)

    tess.left(90)

    tess.end_fill()


draw_housing()

tess.penup()

# Position tess onto the place where the green light should be

tess.forward(40)

tess.left(90)

tess.forward(50)

# Turn tess into a big green circle


tess.shape("circle")

tess.shapesize(3)

tess.fillcolor("green")

yoga.forward(40)

yoga.left(90)

yoga.forward(190)

yoga.shape("circle")

yoga.shapesize(3)

yoga.fillcolor("red")

miki.forward(40)

miki.left(90)

miki.forward(120)

miki.shape("circle")

miki.shapesize(3)

miki.fillcolor("orange")

state_num = 2


def advance_state_machine():
    global state_num

    if state_num == 0:  # Transition from state 0 to state 1

        tess.fillcolor("black")

        yoga.fillcolor("black")

        miki.fillcolor("orange")

        state_num = 1

    if state_num == 1:

        tess.fillcolor("black")

        miki.fillcolor("black")

        yoga.fillcolor("red")

        state_num = 2

    else:

        yoga.fillcolor("black")

        miki.fillcolor("black")

        tess.fillcolor("green")

        state_num = 0


wn.onkey(advance_state_machine, "space")
wn.listen()
wn.mainloop()
