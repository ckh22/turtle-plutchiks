import turtle


# This is where we need to add the sub-divides into the pedals
def pedal(angle: int, color: str):
    # Color
    t.fillcolor(color)
    t.begin_fill()
    t.lt(45 + angle)
    t.circle(-200, 90)
    t.rt(90)
    t.circle(-200, 90)
    t.rt(90)
    t.end_fill()

    # Sub-divide code

    # Labeling code


# These might need to be edited later if the edits in the above
# Land the arrow in an uneven spot.
# Settings includes angle & color for the respective pedal
settings = {
    'Joy/Happiness': {'angle': 0, 'color': '#E8EFA2', 'words': []},
    'Like': {'angle': 46, 'color': '#B1EFA2', 'words': []},
    'Anticipation/Hope': {'angle': 45, 'color': '#A2EFEF', 'words': []}
}

# Uses the angles above to create three pedals
s = turtle.getscreen()
t = turtle.Turtle()
for key, value in settings.items():
    angle = value['angle']
    color = value['color']
    pedal(angle, color)


# End
turtle.done()
