# Pico_w_ble_uart
A simple BLE UART module for Pico W

This isn't my own work, the guts of the code come straight from the MicroPython BLE examples. I've just wrapped it up in a module so it's easy to use.

I've tested this out on a Raspberry Pi Pico W. It might work on other microcontrollers with Bluetooth, it might not.

See the test.py example. This will continuously send hello, and also print out anything that's received
