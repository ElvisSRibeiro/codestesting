def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    return x / y

print("select operation")
print("1.Adicao")
print("2.Subtracao")
print("3.Multiplicacao")
print("4.Dividsao")

operacao = input("Entre com a operacao(1/2/3/4):")

num1 = float(input("Entre com o primeiro numero: "))
num2 = float(input("Entre com o segundo numero: "))

if operacao == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif operacao == '2':
    print(num1, "-", num2, "=", sub(num1,num2))

elif operacao == '3':
    print(num1, "*", num2, "=", add(num1,num2))

elif operacao == '4':
    print(num1, "/", num2, "=", add(num1,num2))

else:
    print("Isso naõ é uma operação")
