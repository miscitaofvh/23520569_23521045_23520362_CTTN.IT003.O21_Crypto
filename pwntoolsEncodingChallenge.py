from pwn import * # pip install pwntools
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(101):
    received = json_recv();
    if "flag" in received: 
        print(received["flag"])
    
    msg = received["encoded"]
    typemsg = received["type"]

    print(msg)
    if typemsg == "base64":
        decoded = base64.b64decode(msg).decode('utf-8')
    if typemsg == "hex":
        decoded = bytes.fromhex(msg).decode('utf-8')
    if typemsg == "rot13":
        decoded = codecs.decode(msg, 'rot_13')
    if typemsg == "bigint":
        decoded = bytes.fromhex(msg[2:]).decode('utf-8')
    if typemsg == "utf-8":
        decoded = "".join([chr(u) for u in msg])

    to_send = {
        "decoded" : decoded
    }

    json_send(to_send)
