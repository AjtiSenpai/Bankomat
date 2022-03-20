felvesz = input("Mennyit szeretnél felvenni:")  #Létre hozok egy változót és megadom neki, hogy felhasználói bemenet adja meg az értékét
husze = int (float(felvesz) / 20000)            #Létre hozok egy változót és megadom neki, hogy a változó egy int adat legyen, illetve az osztás miatt szükség van , hogy a változó float adat legyen, ezek után elosztom húszezerrel, ez adja, hogy hány húszezresre lesz szükség
marad1 = int (float(felvesz) % 20000)           #Létre hozok egy változót és megadom neki, hogy a változó egy int adat legyen, illetve a maradékos osztás miatt szükség van , hogy a változó float adat legyen, ezek után elosztom maradékosan húszezerrel, ez adja, hogy szükség lesz további osztásra, illetve, hogy hány osztásra
if marad1 > 1:                                  #Létre hozok egy if kaput, ez vizsgálja a vátozómat, ha annak az értéke nagyobb, mint egy akkor, akkor tovább megy
    tize= int (float(marad1) / 10000)           #Változó létrehozása, int, float, előző maradék elosztása
    marad2 = int (float(marad1) % 10000)        #Változó létrehozása, int, float, előző maradék elosztása maradékosan
    if marad2 > 1:                              #If kapu létrehozása, maradék vizsgálata
        ote = int (float(marad2) / 5000)        #Változó létrehozása, int, float, előző maradék elosztása
        marad3 = int (float(marad2) % 5000)     #Változó létrehozása, int, float, előző maradék elosztása maradékosan
        if marad3 > 1:                          #If kapu létrehozása, maradék vizsgálata
            kete = int (float(marad3) / 2000)   #Változó létrehozása, int, float, előző maradék elosztása
            marad4 = int (float(marad3) % 2000) #Változó létrehozása, int, float, előző maradék elosztása maradékosan
            if marad4 > 1:                      #If kapu létrehozása, maradék vizsgálata
                e = int (float(marad4) / 1000)  #Változó létrehozása, int, float, előző maradék elosztása
                print ("%s húszezresre, %s tízezresre, %s ötezresre, %s kétezresre, %s ezresre lesz szükség." % (husze, tize, ote, kete, e)) #print parancsal, a kiadni való bankjegyek kiiratása
            else:   #Ha nincs szükség több osztásra, mivel nincs maradék, akkor kiírja a szükséges bankjegyeket
                print ("%s húszezresre, %s tízezresre, %s ötezresre, %s kétezresre lesz szükség" % (husze, tize, ote, kete)) #print parancsal, a kiadni való bankjegyek kiiratása
        else:   #Ha nincs szükség több osztásra, mivel nincs maradék, akkor kiírja a szükséges bankjegyeket
            print ("%s húszezresre, %s tízezresre, %s ötezresre lesz szükség" % (husze, tize, ote)) #print parancsal, a kiadni való bankjegyek kiiratása
    else:   #Ha nincs szükség több osztásra, mivel nincs maradék, akkor kiírja a szükséges bankjegyeket
        print ("%s húszezresre, %s tízezresre lesz szükség" % (husze, tize)) #print parancsal, a kiadni való bankjegyek kiiratása
else:   #Ha nincs szükség több osztásra, mivel nincs maradék, akkor kiírja a szükséges bankjegyeket
    print ("%s húszezresre lesz szükség" % (husze)) #print parancsal, a kiadni való bankjegyek kiiratása