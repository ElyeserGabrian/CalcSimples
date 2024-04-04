valor = input("Faça uma Operaçao Matematica entre dois numero Aqui: ")
for i in valor:
    lista = ["+", "-", "*", "/"]
    for j in lista:
        if i == j:
             n1, op, n2 = valor.partition(j)
             match op:
                 case "+":
                     soma = int(n1) + int(n2)
                     print(soma)
                     break 
                 case "-":
                     sub = int(n1) - int(n2)
                     print(sub)
                     break
                 case "*":
                     mul = int(n1) * int(n2)
                     print(mul)
                     break
                 case "/":
                     div = int(n1) / int(n2)
                     print(div)
                     break
                     
