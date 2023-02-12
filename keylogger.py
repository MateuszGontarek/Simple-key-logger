import keyboard

recorded = keyboard.record(until='esc', suppress=True)

for i in recorded:
    print(i)