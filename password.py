import os, sys
os.system("termux-open-url https://t.me/who_am_i_xxx")

p = int(input('password: '))

i = 1

while i <= p:
    i = i + 1
    if i == p:
        break
    print(i + 1)
print('OPEN:) password')
