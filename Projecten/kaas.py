getal = int(input('Wat is je getal?'))
if getal > 300:
    getal = str(getal)
    print(getal + ' is het grootste getal')
elif getal < 300:
    getal = str(getal)
    print(getal + ' is het kleinste getal')
else:
    getal = 300
    print('Jouw getal is gelijk aan 300!')
