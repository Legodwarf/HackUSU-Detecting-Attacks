dict latinCryllic = {'A': ['А','А̂','А̄','Ӑ','Ӓ'], 'B': ['B']}

for letter in 'АА̂А̄ӐӒ':
    for key in latinCryllic:
        for special in key:
            print()