n = int(input("Какой степени будет многочлен? "))
l = []
for i in range(1,n+2):
    l.append(int(input(f"Чему равен {i} коэффициент?")))
if n == 1:
   print(f"Корнем многочлена является:{(-l[n])/(l[n-1])}")
elif n == 2:
    if l[n-1] ** 2 - 4 * l[n-2] * l[n] < 0:
        print("Нет рациональных корней")
    else:
        x = -l[n-1] / (2 * l[n-2])
        y = l[n-2] * x ** 2 + l[n-1] * x + l[n]
        while y > 0.0001 or y < -0.0001:
            x += 0.00001
            y = l[n-2] * x ** 2 + l[n-1] * x + l[n]
        X1 = x
        x = -l[n-1] / (2 * l[n-2])
        y = l[n-2] * x ** 2 + l[n-1] * x + l[n]
        while y > 0.0001 or y < -0.0001:
            x -= 0.00001
            y = l[n-2] * x ** 2 + l[n-1] * x + l[n]
        X2 = x
        print(f"Корни многочлена:{round(X1,4), round(X2,4)}")
elif n==3:
    b = l.copy()
    l[n - 3] *= 3
    l[n - 2] *= 2
    A = l[n - 3]
    B = l[n - 2]
    C = l[n-1]
    del l[n]
    if B ** 2 - 4 * A * C < -0.0001:
        print("Нет экстремумов")
        if b[n]==0:
            print("Один действительный корень: 0")
        elif b[n]>0:
            if b[n-3]>=0:
                x = 0
                y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                while y > 0.0001 or y < -0.0001:
                    x -= 0.00001
                    y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                print(f"Один корень многочлена: {round(x,3)}")
            else:
                x = 0
                y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                while y > 0.001 or y < -0.001:
                    x += 0.00001
                    y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                print(f"Один корень многочлена: {round(x,3)}")
        else:
            if b[n-3]>=0:
                x = 0
                y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                while y > 0.0001 or y < -0.0001:
                    x += 0.00001
                    y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                print(f"Один корень многочлена: {round(x,3)}")
            else:
                x = 0
                y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                while y > 0.001 or y < -0.001:
                    x -= 0.00001
                    y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                print(f"Один корень многочлена: {round(x,3)}")
    elif (B ** 2 - 4 * A * C) > -0.0001 and (B ** 2 - 4 * A * C) < 0.0001:
        x = -l[n - 2] / (2 * l[n - 3])
        print(f"Один экстремум': {x}")
        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
        if b[n]==0:
            print("Один действительный корень: 0")
        else:
            if b[n - 3] > 0:
                if y >= 0:
                    while y > 0.0001 or y < -0.0001:
                        x -= 0.00001
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                    print(f"Один корень многочлена: {round(x,3)}")
                else:
                    while y > 0.0001 or y < -0.0001:
                        x += 0.00001
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                    print(f"Один корень многочлена: {round(x,3)}")
            else:
                if y >= 0:
                    while y > 0.001 or y < -0.001:
                        x += 0.00001
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                    print(f"Один корень многочлена: {round(x,3)}")
                else:
                    while y > 0.001 or y < -0.001:
                        x -= 0.00001
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                    print(f"Один корень многочлена: {round(x,3)}")
    else:
        x = -B / (2 * A)
        y = A * x ** 2 + B * x + C
        while y > 0.0001 or y < -0.0001:
            x -= 0.00001
            y = A * x ** 2 + B * x + C
        X1 = x
        x = -B / (2 * A)
        y = A * x ** 2 + B * x + C
        while y > 0.0001 or y < -0.0001:
            x += 0.00001
            y = A * x ** 2 + B * x + C
        X2 = x
        print(f"Экстремумы многочлена:{round(X1, 3), round(X2, 3)}")
        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
        if b[n]==0:
            x1=0
            if b[n-3]>0:
                if b[n-2]>=0:
                    if b[n-1]>=0:
                        x=X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2=x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
                    else:
                        x = X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2 = x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
                else:
                    if b[n-1]>=0:
                        x=X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2=x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
                    else:
                        x = X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2 = x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
            else:
                if b[n-2]>=0:
                    if b[n-1]>=0:
                        x=X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2=x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
                    else:
                        x = X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2 = x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
                else:
                    if b[n-1]>=0:
                        x=X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x += 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2=x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
                    else:
                        x = X2
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x2 = x
                        x = X1
                        y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        while y > 0.001 or y < -0.001:
                            x -= 0.00001
                            y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                        x3 = x
                        print(f"Вещественные корни многочлена: {round(x1,3),round(x2,3),round(x3,3)}")
        else:
            Y1 = b[n - 3] * X1 ** 3 + b[n - 2] * X1 ** 2 + b[n - 1] * X1 + b[n]
            Y2 = b[n - 3] * X2 ** 3 + b[n - 2] * X2 ** 2 + b[n - 1] * X2 + b[n]
            if Y1>0 and Y2>0:
                x = X1
                y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                while y > 0.001 or y < -0.001:
                    x -= 0.00001
                    y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                print(f"Один вещественный корень многочлена: {round(x, 3)}")
            elif Y1 < 0 and Y2 < 0:
                x = X2
                y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                while y > 0.001 or y < -0.001:
                    x += 0.00001
                    y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                print(f"Один вещественный корень многочлена: {round(x, 3)}")
            else:
                 x = X1
                 y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                 while y > 0.001 or y < -0.001:
                     x -= 0.00001
                     y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                 x1 = x
                 x = X1
                 y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                 while y > 0.001 or y < -0.001:
                     x += 0.00001
                     y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                 x2 = x
                 x = X2
                 y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                 while y > 0.001 or y < -0.001:
                     x += 0.00001
                     y = b[n - 3] * x ** 3 + b[n - 2] * x ** 2 + b[n - 1] * x + b[n]
                 x3 = x
                 print(f"Вещественные корни многочлена: {round(x1, 3), round(x2, 3), round(x3, 3)}")
else: print("hard")
input()