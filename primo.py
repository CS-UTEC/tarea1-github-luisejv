num = int(input("Ingrese el numero que desee consultar: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es un numero primo")
            print("ya que", i, "es divisor del numero")
            break
    else:
        print(num, "es un numero primo")
else:
    print(num, "no es un numero primo")
