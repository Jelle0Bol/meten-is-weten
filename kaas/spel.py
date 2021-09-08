ant = input('is de kaas geel? Beantwoord met ja of nee. ')
if ant == ("ja"):
    ant = input ('heeft de kaas gaten?')
    if ant == ("ja"):
        ant = input ("is de kaas ongelofelijk duur?")
        if ant == ("ja"):
            print ("Emmenthaler")
        elif ant == ("nee"):
            print ("Leerdammer")
    elif ant == ("nee"):
        ant = input ("is de kaas hard als steen?")
        if ant == ("ja"):
            print ("Pammigiano Reggiano")
        elif ant == ("nee"):
            print ("Goudse kaas")
elif ant == ("nee"):
    ant = input ('heeft de kaas blauwe schimmels?')
    if ant == ("ja"):
        ant = input ('heeft de kaas een korst?')
        if ant == ("ja"):
            print ('Bleu de rochbaron')
        elif ant == ("nee"):
            print ("Foume d.ambert")
    elif ant == ("nee"):
        ant = input ("heeft de kaas een korst?") 
        if ant == ("ja"):
            print ("Camembert") 
        elif ant == ("nee"):
            print ("Mozzarella")
else:
    print ("Gebruik alleen ja of nee AUB")

