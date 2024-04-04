valor = input("Faça uma Operaçao Matematica entre dois numero Aqui: ")
for i in valor:
    lista = ["+", "-", "*", "/"]
    for j in lista:
        if i == j:
             n1, op, n2 = valor.partition(j)
             match op:
                 case "+":
                     soma = float(n1) + float(n2)
                     print(soma)
                     break 
                 case "-":
                     sub = float(n1) - float(n2)
                     print(sub)
                     break
                 case "*":
                     mul = float(n1) * float(n2)
                     print(mul)
                     break
                 case "/":
                     div = float(n1) / float(n2)
                     print(div)
                     break
                     
