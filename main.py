basic.show_icon(IconNames.HAPPY)
maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)

def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 25:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 120)
    elif maqueen.ultrasonic(PingUnit.CENTIMETERS) < 20:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
    elif maqueen.ultrasonic(PingUnit.CENTIMETERS) < 15:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 80)
    elif maqueen.ultrasonic(PingUnit.CENTIMETERS) < 10:
        maqueen.motor_stop(maqueen.Motors.ALL)
        basic.pause(1000)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 80)
        basic.pause(500)
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 130)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 130)
basic.forever(on_forever)
