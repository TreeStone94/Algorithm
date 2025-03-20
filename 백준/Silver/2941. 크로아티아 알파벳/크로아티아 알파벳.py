s = {"c=": "č", "c-":"ć", "dz=": "dž", "d-":"đ", "lj": "lj", "nj":"nj" , "s=": "š", "z=": "ž"}

printS = input()

for x in s:
    printS = printS.replace(x, "*")


print(len(printS))