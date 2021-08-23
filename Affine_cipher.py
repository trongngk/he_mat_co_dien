import string
# mã hóa
plantext = input("Input plantext: ")
m,n = map(int,input('Input key: ').split())
cipher = ""
print("Symbol", end = " | ")
P_index = []
E_x = []
for symbol in plantext:
    print("{:<3}".format(symbol), end = "|")
    if symbol.isupper():
        index = string.ascii_uppercase.find(symbol)
        P_index.append(index)
        index = (m*index+n)%26
        E_x.append(index)
        cipher += string.ascii_uppercase[index]
    elif symbol.islower():
        index = string.ascii_lowercase.find(symbol)
        P_index.append(index)
        index = (m*index+n)%26
        E_x.append(index)
        cipher += string.ascii_lowercase[index]
    else:
        P_index.append(symbol)
        E_x.append(symbol)
        cipher += symbol
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
for i in range(26):
    if m*i % 26 == 1:
        break
for symbol in cipher:
    print("{:<3}".format(symbol), end = "|")
    if symbol.isupper():
        index = string.ascii_uppercase.find(symbol)
        C_index.append(index)
        index = (i*(index - n)) % 26
        E_y.append(index)
        decode += string.ascii_uppercase[index]
    elif symbol.islower():
        index = string.ascii_lowercase.find(symbol)
        C_index.append(index)
        index = (i * (index - n) )% 26
        E_y.append(index)
        decode += string.ascii_lowercase[index]
    else:
        C_index.append(symbol)
        E_y.append(symbol)
        decode  += symbol
print("\nIndex ", end = " | ")
for i in C_index:
    print("{:<3}".format(i),end = "|")
print("\nE(y)  ",end = " | ")
for j in E_y:
    print("{:<3}".format(j), end = "|")
print("\nCipher", end = " | ")
for c in decode:
    print("{:<3}".format(c), end = "|")
