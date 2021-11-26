import turtle


s = turtle.getscreen()
t = turtle.Turtle()
def main():
    # initialize
    turtle.title('Plutchiks')
    turtle.setup(800, 700)


# This is where we need to add the sub-divides into the pedals
def pedal(angle: int, color: str, emotion: str):
    # Color
    t.home()
    t.fillcolor(color)
    t.begin_fill()
    t.lt(angle + 45)
    t.circle(-200, 90)
    t.rt(90)
    t.circle(-200, 90)
    t.rt(90)
    t.end_fill()

    # Sub-divide code

    # Labeling emotion
    t.pu()
    if emotion == 'Anticipation/Hope':
        t.setpos(-325, 0)
    elif emotion == 'Like':
        t.setpos(0, 300)
    elif emotion == "Joy/Happiness":
        t.setpos(325, 0)
    t.write(emotion, False, "center")
    t.home()
    t.pd()

    # Labeling words


# These might need to be edited later if the edits in the above
# Land the arrow in an uneven spot.
# Settings includes angle & color for the respective pedal
settings = {
    'Joy/Happiness': {'angle': 0, 'color': '#E8EFA2', 'words': []},
    'Like': {'angle': 90, 'color': '#B1EFA2', 'words': []},
    'Anticipation/Hope': {'angle': 180, 'color': '#A2EFEF', 'words': []}
}



main()
# Uses the angles above to create three pedals
for emotion, setting in settings.items():
    angle = setting['angle']
    color = setting['color']
    pedal(angle, color, emotion)


# End
turtle.done()
