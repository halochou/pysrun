import time

def _buildkey(num,reverse):
    ret = ""
    low = num & 0x0f
    high = num >> 4
    high = high & 0x0f
    if not reverse:
        ret += chr(low + 0x36)
        ret += chr(high + 0x63)
    else:
        ret += chr(high + 0x63)
        ret += chr(low + 0x36)
    return ret

def encrypt(password,delta):
    key = str(int((time.time()+delta)/60))
    password = password[0:16]
    ret = ""
    for i in range(0,len(password)):
        p = ord(password[i])
        k = ord(key[-1*(i+1)])
        keychar = p ^ k
        ret += _buildkey(keychar,i%2)
    return ret

if __name__ == "__main__":
    msg = encrypt('19890730',0)
    print msg
