data = ""

def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_uart_data_received():
    global data
    data = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    basic.show_string(data)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

def on_button_pressed_b():
    basic.show_number(input.temperature())
    basic.show_leds("""
        . # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
