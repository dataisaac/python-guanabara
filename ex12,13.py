produto = float(input('digite o valor do seu produto: '))
desconto = float(input('digite o valor do seu desconto: '))

valor_desconto = produto * desconto / 100
valor_final = produto - valor_desconto

print(f'seu produto de {produto:.2f} reais ficao com desconto de {desconto}% fica {valor_final} reais')

salario = float(input('digite o valor do seu salario: '))
aumento = float(input('digite o valor do seu aumento: '))

valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

print(f'seu salario de {salario:.2f} reais ficará com {novo_salario} reais com o aumento de {aumento}%')