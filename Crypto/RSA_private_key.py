def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def inverse_modulo(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
    
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

phiN = (p-1)*(q-1)
print(inverse_modulo(e, phiN))