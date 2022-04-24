radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        if (maqueen.Ultrasonic(PingUnit.Centimeters) < 25) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 120)
        } else if (maqueen.Ultrasonic(PingUnit.Centimeters) < 20) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 100)
        } else if (maqueen.Ultrasonic(PingUnit.Centimeters) < 15) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 80)
        } else if (maqueen.Ultrasonic(PingUnit.Centimeters) < 10) {
            maqueen.motorStop(maqueen.Motors.All)
            basic.pause(1000)
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 80)
            basic.pause(500)
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 130)
        } else {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 130)
        }
    }
})
input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.StickFigure)
        basic.pause(500)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Square)
        basic.pause(500)
        basic.showIcon(IconNames.SmallSquare)
        basic.pause(500)
    }
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Happy)
        basic.pause(500)
        basic.clearScreen()
    }
})
radio.setGroup(1)
basic.showIcon(IconNames.Heart)
maqueen.motorStop(maqueen.Motors.All)
basic.forever(function () {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    basic.pause(100)
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
    basic.pause(100)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    basic.pause(100)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    basic.pause(100)
})
