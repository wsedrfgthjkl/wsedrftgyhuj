a = True
while a:
    ps = input("Ввдите код")
    if len(ps)<8:
         print("Короткий")
    else:
        print("OK")
        a = False
print("Хорош")

        