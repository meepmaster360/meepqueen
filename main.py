def on_received_number(receivedNumber):
    if receivedNumber == 0:
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
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    for index in range(4):
        basic.show_icon(IconNames.STICK_FIGURE)
        basic.pause(500)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index2 in range(4):
        basic.show_icon(IconNames.HAPPY)
        basic.pause(500)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
basic.show_icon(IconNames.HEART)
maqueen.motor_stop(maqueen.Motors.ALL)

def on_forever():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    basic.pause(100)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    basic.pause(100)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    basic.pause(100)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    basic.pause(100)
basic.forever(on_forever)
