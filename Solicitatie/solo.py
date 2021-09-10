
weight = float(input("Hoeveel weegt u? "))
if weight >= 90:
    print ("Sorry, u bent niet geschikt voor de baan")
elif weight < 90:
    print ("Super! Volgende vraag")
    jaar = float(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
    if jaar >= 4:
        print ("Nice! Volgende vraag")
        diploma = (input("Bent u in bezit van een diploma MBO-4 Onderneming? Beantwoord de vraag met ja of nee "))
        if diploma == ("ja"):
            print ("Grandioos! volgende vraag")
            rij = (input("Bent u in bezit van een geldig vrachtwagen rijbewijs? Beantwoord de vraag met een ja of nee "))
            if rij == ("ja"):
                print ("Fantastisch! Volgende vraag")
                hoed = (input("Bent u in bezit van een hoge hoed. Het moet speciaal een HOGE hoed zijn! Beanwoord met ja of nee "))
                if hoed == ("ja"):
                    print ("Geweldig! Volgende vraag")
                    pers = (input("Bent u een man met een snor met de breedte van 20 cm OF een vrouw met rood krulhaar langer dan 20cm? Beantwoord de vraag met een ja of nee "))
                    if pers == ("ja"):
                        print ("Uitmuntend! Volgende vraag")
                        cm = float(input("Hoelang bent u? Beantwoord de vraag in centimeters. "))
                        if cm > 150:
                            print ("Top! Volgende vraag!")
                            cert = (input("Heeft u de certificaat \'Overleven met gevaarlijk personeel\'? Beantwoord de vraag met een ja of nee. "))
                            if cert == ("yes"):
                                print ("Helemaal mooi! Dit was de solicitatie! U bent aangenomen, en wat zijn wij ongelofelijk blij om u in het team te hebben. Ik zal nu wat uitleggen waar je je rooster en vakantie kan aanvragen.")
                            elif cert == ("no"):
                                print ("U komt helaas niet in opmerking voor onze vacature")
                            else:
                                print ("Beantwoord de vraag alleen met een ja of nee")   
                        elif cm < 150:
                            print ("U komt helaas niet in opmerking voor onze vacature")
                    elif pers == ("nee"):
                        print ("U komt helaas niet in opmerking voor onze vacature")
                    else:
                        print ("Beantwoord alleen met ja of nee")
                elif hoed == ("nee"):
                    print ("U komt helaas niet in opmerking voor onze vacature")
                else:
                    print ("Beantwoord alleen met ja of nee")
            elif rij == ("nee"):
                print ("U komt helaas niet in opmerking voor onze vacature")
            else:
                print ("Beantwoord alleen met ja of nee")
        elif diploma == ("nee"):
            print ("U komt helaas niet in opmerking voor onze vacature")
        else:
            print ("beantwoord de vraag alleen met een ja of nee")
    elif jaar < 4:
        print ("U komt helaas niet in opmerking voor onze vacature")