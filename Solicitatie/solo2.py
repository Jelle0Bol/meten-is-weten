print ("+++++++++++++++++++++++++++++++++++++++++")
print ("+++++++++   Circus diricteur   ++++++++++")
print ("+++++++++++++++++++++++++++++++++++++++++")
print ("+   We gaan een paar vragen stellen.    +")
print ("+ Zou u alstublieft zo eerlijk mogelijk +")
print ("+       de vragen beantwoorden?         +")
print ("+++++++++++++++++++++++++++++++++++++++++")

dressuur = int(input("Hoeveel jaar praktijk ervaring heeft u met dieren-dressuur? : "))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren? : "))
acrobatiek = int(input("Hoeveel jaar ervaring heeft u met acrobatiek? : "))
rarevraag1 = str(input("Heeft u een computer? : "))
mbo = str(input("Bent u in bezit van een MBO-4 diploma? : ")).lower()
rijbewijs = str(input("Bent u in bezit van een GELDIG vrachtwagen rijbewijs? : ")).lower()
rarevraag2 = str(input("Wat voor huis woont u? : "))
hoed = str(input("Bent u in bezit van een hoge hoed? : "))
rarevraag3 = str(input("Heeft u een huisdier? : ")).lower()
geslacht = str(input("Bent u een man of vrouw? :  ")).lower()
if geslacht == "man":
    snor = int(input("Hoe breed is uw snor? Typ het antwoord in centimeters : "))
elif geslacht == "vrouw":
    krullen = int(input("Hoelang zijn uw krullen? Typ het antwoord in centimeters  : "))
lengte = int(input("Hoe lang bent u? Typ het antwoord in centimeters : "))
gewicht = int(input("Hoeveel weegt u? Typ het antwoord in kilos : "))
fruit = str(input("Houdt u van fruit? : "))
certificaat = str(input("Heeft u het certificaat Overleven met gevaarlijk personeel? : ")).lower()

if geslacht == "man" and snor >= 10 and (dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3) and mbo == "ja" and rijbewijs == "ja" and hoed == "ja" and lengte >= 150 and gewicht >= 90 and certificaat == "ja":
    print ("Gefeliciteerd, u bent aangenomen! Bedankt voor het meedoen!")
elif geslacht == "vrouw" and krullen >=20 and (dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3) and mbo == "ja" and rijbewijs == "ja" and hoed == "ja" and lengte >= 150 and gewicht >= 90 and certificaat == "ja":
    print ("Gefeliciteerd, u bent aangenomen! Bedankt voor het meedoen!")
else:
    print ("Sorry, u heeft niet de eisen die je nodig hebt voor de baan...")