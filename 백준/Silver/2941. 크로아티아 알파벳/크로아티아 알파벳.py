s = {"c=": "č", "c-":"ć", "dz=": "dž", "d-":"đ", "lj": "lj", "nj":"nj" , "s=": "š", "z=": "ž"}

printS = input()

cnt = 0
for x in s:
    if printS.count(x) > 0:
        cnt += printS.count(x)
        printS = printS.replace(x, "//")

printS = printS.replace("//", "")
print(cnt + len(printS))