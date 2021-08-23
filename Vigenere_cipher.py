import string
# mã hóa
plantext = input("Input plantext: ")
key = input("Input key: ")
cipher = ""
print("Symbol", end = " | ")
P_index = []
E_x = []
key_index = 0
for symbol in plantext:
    print("{:<3}".format(symbol), end = "|")
    if symbol.isupper():
        if key[key_index].islower():
            new_key = key[key_index].upper()
        else:
            new_key = key[key_index]
        index = string.ascii_uppercase.find(symbol)
        P_index.append(index)
        index = (index + string.ascii_uppercase.find(new_key)) % 26
        E_x.append(index)
        cipher += string.ascii_uppercase[index]
    elif symbol.islower():
        if key[key_index].isupper():
            new_key = key[key_index].lower()
        else:
            new_key = key[key_index]
        index = string.ascii_lowercase.find(symbol)
        P_index.append(index)
        index = (index + string.ascii_lowercase.find(new_key)) % 26
        E_x.append(index)
        cipher += string.ascii_lowercase[index]
    else:
        P_index.append(symbol)
        E_x.append(symbol)
        cipher += symbol
        continue
    key_index += 1
    if key_index == len(key):
        key_index = 0
print("\nIndex ", end = " | ")
for i in P_index:
    print("{:<3}".format(i),end = "|")
print("\nE(x)  ",end = " | ")
for j in E_x:
    print("{:<3}".format(j), end = "|")
print("\nCipher", end = " | ")
for c in cipher:
    print("{:<3}".format(c), end = "|")
print("\n____\n____")

# giải mã
decode = ""
print("Symbol", end = " | ")
C_index = []
E_y = []
decode_key_index = 0
for symbol in cipher:
    print("{:<3}".format(symbol), end = "|")
    if symbol.isupper():
        if key[decode_key_index].islower():
            new_decode_key = key[decode_key_index].upper()
        else:
            new_decode_key = key[decode_key_index]
        index = string.ascii_uppercase.find(symbol)
        C_index.append(index)
        index = (index - string.ascii_uppercase.find(new_decode_key)) % 26
        E_y.append(index)
        decode += string.ascii_uppercase[index]
    elif symbol.islower():
        if key[decode_key_index].isupper():
            new_decode_key= key[decode_key_index].lower()
        else:
            new_decode_key = key[decode_key_index]
        index = string.ascii_lowercase.find(symbol)
        C_index.append(index)
        index = (index - string.ascii_lowercase.find(new_decode_key)) % 26
        E_y.append(index)
        decode += string.ascii_lowercase[index]
    else:
        C_index.append(symbol)
        E_y.append(symbol)
        decode += symbol
        continue
    decode_key_index += 1
    if decode_key_index == len(key):
        decode_key_index = 0
print("\nIndex ", end = " | ")
for i in C_index:
    print("{:<3}".format(i),end = "|")
print("\nE(y)  ",end = " | ")
for j in E_y:
    print("{:<3}".format(j), end = "|")
print("\nCipher", end = " | ")
for c in decode:
    print("{:<3}".format(c), end = "|")
