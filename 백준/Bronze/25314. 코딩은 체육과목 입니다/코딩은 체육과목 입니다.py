byte = int(input())

cnt = int(byte / 4)
str = ""
for _ in range(cnt):
    str += "long "

print(str + "int")