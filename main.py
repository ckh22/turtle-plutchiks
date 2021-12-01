import turtle


s = turtle.getscreen()
t = turtle.Turtle()


def main():
    # initialize
    turtle.title('Plutchiks')
    turtle.setup(1000, 700)
    t.hideturtle()
    turtle.hideturtle()


# This is where we need to add the sub-divides into the pedals
def pedal(angle: int, colors, emotion: str, words):
    # Color
    t.pu()
    t.home()
    t.fillcolor(colors[2])
    t.begin_fill()
    t.lt(angle + 45)
    t.circle(-200, 90)
    t.rt(90)
    t.circle(-200, 90)
    t.rt(90)
    t.end_fill()

    # Sub-divide code
    # Larger Sub-division
    t.fillcolor(colors[1])
    t.begin_fill()
    t.circle(-200, 60)
    t.rt(60)
    t.circle(-200, 30)
    t.rt(60)
    t.circle(-200, 60)
    t.end_fill()

    # Closest Sub-division
    t.fillcolor(colors[0])
    t.begin_fill()
    t.rt(90)
    t.circle(-200, 30)
    t.rt(90)
    t.circle(-200, 30)
    t.rt(90)
    t.circle(-200, 30)
    t.end_fill()

    # Labeling emotion
    t.pu()
    t.home()
    header_style = ("Arial", 16, "normal")
    if emotion == 'Anticipation/Hope':
        t.setpos(-325, 0)
        t.write(emotion, False, "right", header_style)
    elif emotion == 'Like':
        t.setpos(0, 300)
        t.write(emotion, False, "center", header_style)
    elif emotion == "Joy/Happiness":
        t.setpos(300, 0)
        t.write(emotion, False, "left", header_style)
    t.home()
    t.pd()

    # Labeling words
    for i in range(3):
        t.pu()
        t.home()
        multiplier = 0
        if i == 0:
            multiplier = 1
        elif i == 1:
            multiplier = 0.85
        elif i == 2:
            multiplier = 0.7

        style = ("Arial", int(12 * multiplier), "normal")
        if emotion == 'Anticipation/Hope':
            t.setpos(-65 + (- 80 * i), 10)
            t.write(words[i * 2], False, "center", style)
            t.setpos(-65 + (- 80 * i), -10)
            t.write(words[(i * 2) + 1], False, "center", style)
        elif emotion == 'Like':
            t.setpos(0, 50 + (80 * i))
            t.write(words[i * 2], False, "center", style)
            t.setpos(0, 70 + (80 * i))
            t.write(words[(i * 2) + 1], False, "center", style)
        elif emotion == "Joy/Happiness":
            t.setpos(65 + (80 * i), 10)
            t.write(words[i * 2], False, "center", style)
            t.setpos(65 + (80 * i), -10)
            t.write(words[(i * 2) + 1], False, "center", style)
        t.home()
        t.pd()


# settings includes the emotion as keys with the following data
#   colors - in order from high to low opacity
#   words - 6 important words from each category
#   angle - petal orientation
settings = {
    'Joy/Happiness': {'angle': 0, 'colors': ['#E0EC5F', '#E3EC84', '#E6ECAC'], 'words': ['love', 'amazing', 'awesome', 'omg', 'cute', 'lol']},
    'Like': {'angle': 90, 'colors': ['#79EC5F', '#9FEB8E', '#BCEDB1'], 'words': ['good', 'great', 'like', 'wow', 'interesting', 'nice']},
    'Anticipation/Hope': {'angle': 180, 'colors': ['#5FECE9', '#89ECEA', '#B5EBEA'], 'words': ['update', 'please', 'soon', 'wait', 'next', 'continue']}
}


main()
for emotion, setting in settings.items():
    angle = setting['angle']
    colors = setting['colors']
    words = setting['words']
    pedal(angle, colors, emotion, words)


turtle.done()