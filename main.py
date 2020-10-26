height = 0
number = 0
angle = 0
randnum1 = 0
randnum2 = 0

def on_pin_pressed_p0():
    global height
    for index in range(30):
        height = randint(100, 200)
        if height <= 150:
            basic.show_number(height)
            basic.show_string("SHORT")
        elif height <= 151 and height >= 170:
            basic.show_number(height)
            basic.show_string("MEDIUM")
        elif height >= 171:
            basic.show_number(height)
            basic.show_string("TALL")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global number
    for index2 in range(10):
        number = randint(1, 6)
        if number == 1 or number == 3:
            dice()
            basic.pause(200)
            basic.show_string("TEAM GREEN")
        elif number == 2 or number == 5:
            dice()
            basic.pause(200)
            basic.show_string("TEAM BLUE")
        else:
            dice()
            basic.pause(200)
            basic.show_string("TEAM RED")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def dice():
    if number == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif number == 2:
        basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
            """)
    elif number == 3:
        basic.show_leds("""
            . . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . .
            """)
    elif number == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
    elif number == 5:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . # # # .
            . . . . .
            . # # # .
            . . . . .
            """)

def on_button_pressed_b():
    global number
    for index3 in range(10):
        number = randint(1, 100)
        if number % 2 == 0:
            basic.show_number(number)
            basic.pause(200)
            basic.show_string("EVEN")
        else:
            basic.show_number(number)
            basic.pause(200)
            basic.show_string("ODD")
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global angle
    for index4 in range(10):
        angle = randint(0, 180)
        if angle < 90:
            basic.show_number(angle)
            basic.show_string("ACUTE")
        elif angle == 90:
            basic.show_number(angle)
            basic.show_string("STRAIGHT")
        elif angle > 90:
            basic.show_number(angle)
            basic.show_string("OBTUSE")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    global randnum1, randnum2
    while input.pin_is_pressed(TouchPin.P2):
        randnum1 = randint(0, 4)
        randnum2 = randint(0, 4)
        led.plot(randnum1, randnum2)
        basic.pause(200)
        if randnum1 == randnum2:
            music.play_melody("G E A G C5 D A F ", 120)
        else:
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.clear_screen()
basic.forever(on_forever)
