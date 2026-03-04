medida = float(input('uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida / 1
cm = medida * 100
mm = medida * 1000
print(f'A media de {medida}m corresponde a {km:.0f}km, {hm:.0f}hm, {dam:.0f}dam, {dm:.0f}dm, {cm:.0f}cm, {mm:.0f}mm')
