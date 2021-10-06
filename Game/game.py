X = 37
ant = input("Welkom in de Pokemon wereld! Ik ben professor Mahogany, en welkom in de stad Elblesser City. Omdat jij 10 jaar bent     geworden sturen we je de grote wereld met een totaal niet gevaarlijke Pokemon. Als je het misbruikt kan je de wereld    overnemen maar he yolo je bent 10 jaar dus dat is wel lache als je er zelf acher komt. Goed, je mag je Pokemon kiezen.  Wil je Bulbasaur, Squirtle of Charmander? ")
if ant == ("Bulbasaur"):
    print ("Bulbasaur, de gras pokemon? Goeie keuze. Nu mag je de wildernis in gaan. De bedoeling is dat je alle steden bezoekt en  hun Gymbaas verslaat ook al ben je 10 jaar hahaha.")
    ant = input ("Wil je naar Pewter City gaan? ")
    if ant == ("ja"):
        print ("Helemaal prima! Succes met je avontuur!")
        ant = input ("Terwijl je onderweg was naar Pewter City is je Bulbasaur level 9 geworden! Nu ga je je de gym verslaan! Nu je bij de gym bent aangekomen en tegen Brock, de steen pokemon gym leader vecht mag je een attack kiezen! Welke attack wil je doen:  VineWhip of FlameThrower? ")
        if ant == ("VineWhip"):
            print ("Super! Het was super effectief! Je hebt Brock verslagen! Je Bulbasaur is gevolueerd naar een Ivysaur! En het heeft de   attack RazorLeaf geleerd!")
            ant = input ("Nu je naar de volgende stad bent gereisd is Ivysaur een paar levels omhoog gegaan, het is nu level 21! Goed bezig!      Alleen nu je bent aangekomen in Cerulean City moet je tegen Misyt, de water gym leader vechten. Ook al is Ivysaur qua   type in het voordeel kan het niet zwemmen. Geven we Ivysaur zwembandjes? Beantwoord met ja of nee. ")
            if ant == ("ja"):
                print ("Prima keuze! Ivysaur heeft weer gewonnen en is nu gevolueerd in Venusaur! Het heeft helaas geen nieuwe attacks geleerd. Nu je Venusaur sterk genoeg is om tegen team Rocket te vechten kan je het doen, maar wil je dat ook? ja of nee? ")
                ant = input ("ja of nee? ")
                if ant == ("ja"):
                    print ("Helaas was Venusaur net niet goed genoeg om team Rocket te verslaan en hebben ze Venusaur gestolen van je. GAME OVER")
                elif ant ==("nee"):
                    print ("Team Rocket heeft voor je neus heel het drop overgenomen en is nu de rijkste mafia-club van de hele wereld. GAME OVER")
            elif ant == ("nee"):
                print ("Helaas in Ivysaur verdronken dankzij jouw slechte keuze. GAME OVER")
        elif ant == ("FlameThrower"):
            print ("Je gebruikte FlameThrower maar dat is een attack wat Bulbasaur niet kan leren, jij cheater! Je hebt verloren.")

    elif ant == ("nee"):
        print ("Dan niet, blijf maar lekker chillen thuis, dan word mijn kleinzoon GARY easy kampioen")
if ant == ("Charmander"):
    print ("Charmander ligt te slapen en heeft geen zin om wakker gemaakt te worden.")
    ant = input ("Maak je Charmander alsnog wakker? Beantwoord de vraag met ja of nee. ")
    if ant == ("ja"):
        print ("Verkeerde keuze! Charmander is super chagrijnig wakker geworden en heeft zijn attack FlameThrower gebruikt op je. GAME OVER")
    elif ant == ("nee"):
        print ("Je laat Charmander lekker verder slapen. Kies een andere pokemon de volgende keer. GAME  OVER.")
if ant == ("Squirtle"):
    print ("Ongeloofelijke goede keuze! Nu je Squirtle uit de Pokeball hebt gelaten heeft Squirtle 99 Rare Candys gevonden!")
    ant = float(input("Hoeveel Rare Candys wil je gebruiken? "))
    if ant <= 10:
        print ("Je mag wel meer kiezen hoor. Je hoeft niet zo netjes te doen! GAME OVER")
    elif ant >= 11:
            print ("Prima keuze! Nu is je Squirtle gevolueerd naar een Blastoise, een beast van een Pokemon!")
            ant=float(input("Even snel een vraagje tussen door: Op welk level evolueert Wartortle in Blastoise? "))
            if ant > 35 and ant < X:
                print ("Helemaal correct!") 
                ant=float(input("Nog een vraagje: Op welke levels evolueren Bulbasaur naar Ivysaur OF Charmander naar Charmeleon? Tip: de 2 getallen     zitten tussen de 10 en 20. "))
                if ant > 15 or ant < 19:
                    print ("Helemaal correct!") 
                    ant = input ("Ben je er klaar voor om Pokemon meester te worden? Beantwoord met ja of nee. ")
                    if ant == ("ja"):
                        print ("Helemaal mooi! Je hebt de beste Pokemon verslagen met je sterke Blastoise and bent kampioen van je regio geworden.      SUCCES")
                    elif ant == ("nee"):
                        print ("Haha wat een domme fout, je hebt een hele sterke en nu word mijn kleinzoon kampioen. GAME OVER") 
                else:
                    print ("Fout! GAME OVER!")                  
            else: print ("Fout! We kunnen geen Pokemon meester van je maken als je geen basic Pokemon kennis kent. GAME OVER")
