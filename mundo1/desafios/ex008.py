metros = float(input("Uma distância em metros: "))

# conversao

km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'A medida de {metros}m corresponde a')

print(f"{km}KM")
print(f'{hm}HM')
print(f'{dam:.2f}DAM')
print(f'{dm:.2f}DM')
print(f'{metros}M')
print(f'{cm:.2f}CM')
print(f'{mm:.2f}MM')
