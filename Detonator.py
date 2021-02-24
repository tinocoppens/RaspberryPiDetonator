import automationhat
import time
detonatetrueorfalse = input('Detonate ? (y/n) : ')
if detonatetrueorfalse == "y":
    print("3")
    time.sleep(1.0)
    print("2")
    time.sleep(1.0)
    print("1")
    time.sleep(1.0)
    print("Detonate")
    automationhat.relay.one.toggle()
if detonatetrueorfalse == "n":
    print('Ok')
else:
    print('Invalid')
#with https://shop.pimoroni.com/products/automation-hat
