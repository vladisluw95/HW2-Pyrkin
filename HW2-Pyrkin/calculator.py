def subst(a,b):
    #Вычитание
    return a - b 

def mult(a,b):
    #Умножение
    return a * b
def div(a,b):
    #Деление
    return a / b

def plus(a,b):
    #Сложение
    return a + b


def main():
    expression = input('Введите математическое выражение, используя 2 переменные и символы "+", "-", "*", "/"')
    some_parts = expression.split()
    a, operator, b = some_parts
    a = float(a)
    b = float(b)
    if (operator == '*'):
        result = mult(a, b)
    elif (operator == '/'):
        result = div(a, b)
    elif (operator == '-'):
        result = subst(a, b)
    elif (operator == '+'):
        result = plus(a, b)

    


    print(result)

if __name__ == "__main__":
    main()
