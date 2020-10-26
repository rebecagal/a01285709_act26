let height = 0
let number = 0
let angle = 0
let randnum1 = 0
let randnum2 = 0
input.onPinPressed(TouchPin.P0, function () {
    for (let index = 0; index < 30; index++) {
        height = randint(100, 200)
        if (height <= 150) {
            basic.showNumber(height)
            basic.showString("SHORT")
        } else if (height <= 151 && height >= 170) {
            basic.showNumber(height)
            basic.showString("MEDIUM")
        } else if (height >= 171) {
            basic.showNumber(height)
            basic.showString("TALL")
        }
    }
})
input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 10; index++) {
        number = randint(1, 6)
        if (number == 1 || number == 3) {
            dice()
            basic.pause(200)
            basic.showString("TEAM GREEN")
        } else if (number == 2 || number == 5) {
            dice()
            basic.pause(200)
            basic.showString("TEAM BLUE")
        } else {
            dice()
            basic.pause(200)
            basic.showString("TEAM RED")
        }
    }
    basic.clearScreen()
})
function dice () {
    if (number == 1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else if (number == 2) {
        basic.showLeds(`
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
            `)
    } else if (number == 3) {
        basic.showLeds(`
            . . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . .
            `)
    } else if (number == 4) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            `)
    } else if (number == 5) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . # # # .
            . . . . .
            . # # # .
            . . . . .
            `)
    }
}
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 10; index++) {
        number = randint(1, 100)
        if (number % 2 == 0) {
            basic.showNumber(number)
            basic.pause(200)
            basic.showString("EVEN")
        } else {
            basic.showNumber(number)
            basic.pause(200)
            basic.showString("ODD")
        }
    }
    basic.clearScreen()
})
input.onPinPressed(TouchPin.P1, function () {
    for (let index = 0; index < 10; index++) {
        angle = randint(0, 180)
        if (angle < 90) {
            basic.showNumber(angle)
            basic.showString("ACUTE")
        } else if (angle == 90) {
            basic.showNumber(angle)
            basic.showString("STRAIGHT")
        } else if (angle > 90) {
            basic.showNumber(angle)
            basic.showString("OBTUSE")
        }
    }
})
basic.forever(function () {
    while (input.pinIsPressed(TouchPin.P2)) {
        randnum1 = randint(0, 4)
        randnum2 = randint(0, 4)
        led.plot(randnum1, randnum2)
        basic.pause(200)
        if (randnum1 == randnum2) {
            music.playMelody("G E A G C5 D A F ", 120)
        } else {
            music.playTone(262, music.beat(BeatFraction.Whole))
        }
    }
    basic.clearScreen()
})
