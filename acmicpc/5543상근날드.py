hambuger = []
drink = []
for i in range(3):
    hambuger.append(int(input()))

min_hambuger = min(hambuger)
for i in range(2):
    drink.append(int(input()))
min_drink = min(drink)
print(min_hambuger + min_drink - 50)
