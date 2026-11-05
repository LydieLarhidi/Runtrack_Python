def any_computation(num1, operator, num2):
    match operator:
        case "+":
            #print(num1, "+", num2, "=", num1+num2)
            return num1+num2
        case "-":
            #print(num1, "-", num2, "=", num1-num2)
            return num1-num2

        case "*":
            #print(num1, "*", num2, "=", num1*num2)
            return num1*num2

        case "/":
            #print(num1, "/", num2, "=", num1/num2)
            return num1/num2

        case "%":
            #print(num1, "%", num2, "=", num1%num2)
            return num1%num2

        case _:
            print("cas non pris en compte!")

num1 = float(input("num1 = "))
num2 = float(input("num2 = "))
operator = input("operator ")

resultat = any_computation(num1, operator, num2)
print("Le resultat de ", num1, operator, num2, " est : ", resultat)


