
# gehaltProStunde wird als string gelesen
gehaltProStunde = input ("Stundenlohn: ")

# umwandeln in Komma Zahl
gehaltProStunde = float (gehaltProStunde)

# monatsgehalt berechnen
gehaltProMonat = gehaltProStunde * 168

# Ausgabe Monatsgehalt
print ("Gehalt pro Monat: " + str (gehaltProMonat) + " €")
# print ("Gehalt pro Monat: ", gehaltProMonat, " €")


if gehaltProMonat <= 4000:

    print ("Nix Großverdiener")
    steuern = 0
    NettoGehaltProMonat = gehaltProMonat - steuern
    print ("NettoGehaltProMonat", NettoGehaltProMonat)
    

if gehaltProMonat > 4000 and gehaltProMonat <= 6000:

    print ("Großverdiener")
    steuern = gehaltProMonat * 0.20
    NettoGehaltProMonat = gehaltProMonat - steuern
    print ("NettoGehaltProMonat", NettoGehaltProMonat)
    


if gehaltProMonat > 6000:

    print ("Sehr Großverdiener")
    steuern = gehaltProMonat * 0.50
    NettoGehaltProMonat = gehaltProMonat - steuern
    print ("NettoGehaltProMonat", NettoGehaltProMonat)
    




