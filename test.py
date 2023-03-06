import ble_uart
import bluetooth
import time

def print_handler():
    print(uart.read().decode().strip())

ble = bluetooth.BLE()
uart = ble_uart.Ble_uart(ble, name="bens app")


while True:
    uart.write("hello\n")
    time.sleep(1)
