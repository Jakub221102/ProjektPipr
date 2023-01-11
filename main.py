from interface import Interface, StopException

interface = Interface()
while True:
    try:
        interface.tick()
    except StopException:
        break
