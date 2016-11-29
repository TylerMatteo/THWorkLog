from log import Log

log = Log()

while True:
    option = input("Would you like to enter a [n]ew entry, [l]ookup an existing one, or [q]uit? ")

    if(option.upper() == "Q"):
        break

