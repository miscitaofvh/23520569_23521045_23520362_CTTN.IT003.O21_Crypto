import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

ciphertext = b"177d36396d029f19708cef8d1c861bfd1f227170511203bbb211a703905f9e5128ae38bc1312435b814108836328262a"
payload = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
flag = ""

def response(address):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/" + address.encode().hex() + '/'
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

while "}" not in flag:
    responsePayload = response(payload)[:64]
    for i in range(33, 128):
        responseAll = response(payload + flag + chr(i))[:64]
        print("Flag: " + flag + ".   Try: " + payload + flag + chr(i))
        if responsePayload == responseAll:
            flag += chr(i)
            break
    payload = payload[:-1]

print(flag)