ant = input('is de kaas geel? Beantwoord met ja of nee. ')
if ant.lower() == ("ja"):
    ant = input ('heeft de kaas gaten?')
    if ant.lower() == ("ja"):
        ant = input ("is de kaas ongelofelijk duur?")
        if ant.lower() == ("ja"):
            print ("Emmenthaler")
        elif ant.lower() == ("nee"):
            print ("Leerdammer")
    elif ant.lower() == ("nee"):
        ant = input ("is de kaas hard als steen?")
        if ant.lower() == ("ja"):
            print ("Pammigiano Reggiano")
        elif ant.lower() == ("nee"):
            print ("Goudse kaas")
elif ant.lower() == ("nee"):
    ant = input ('heeft de kaas blauwe schimmels?')
    if ant.lower() == ("ja"):
        ant = input ('heeft de kaas een korst?')
        if ant.lower() == ("ja"):
            print ('Bleu de rochbaron')
        elif ant.lower() == ("nee"):
            print ("Foume d.ambert")
    elif ant.lower() == ("nee"):
        ant = input ("heeft de kaas een korst?") 
        if ant.lower() == ("ja"):
            print ("Camembert") 
        elif ant.lower() == ("nee"):
            print ("Mozzarella")
else:
    print ("Gebruik alleen ja of nee AUB")

