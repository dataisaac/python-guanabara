dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de km/h: '))

dias = dias * 60
km = km * 0.15

total = dias + km


print(f'voce deve pagar {total:.2f} reais.')