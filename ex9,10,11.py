n1 = int(input('Digite o valor da tabuada que voce quer saber: '))

print('a tabuada de {}'.format(n1))

print(f'{n1} x 1 = {n1*1}')
print(f'{n1} x 2 = {n1*2}')
print(f'{n1} x 3 = {n1*3}')
print(f'{n1} x 4 = {n1*4}')
print(f'{n1} x 5 = {n1*5}')
print(f'{n1} x 6 = {n1*6}')
print(f'{n1} x 7 = {n1*7}')
print(f'{n1} x 8 = {n1*8}')
print(f'{n1} x 9 = {n1*9}')
print(f'{n1} x 10 = {n1*10}')

R = int(input('Quanto voce tem em reais:'))

D = R / 5.12

print(f'Então voce tem {D} dolares')

larg = float(input("largura da parede: "))
alt = float(input("altura da parede: "))
area = larg * alt
tinta = area / 2
print(f'sua parede tem a dimensao de {larg}x{alt} e a sua area de {area}m²')
print(f'voce precisa de {tinta} litros para pintar a parede')

