def berechne_urlaubstage(alter, behinderung, betriebszugehoerigkeit):
    urlaubstage = 26
    
    if alter < 18:
        urlaubstage = 30
    elif alter > 55:
        urlaubstage = 28
    
    if behinderung >= 50:
        urlaubstage += 5
    
    if betriebszugehoerigkeit > 10:
        urlaubstage += 2
    
    return urlaubstage

# Beispielaufruf 
alter = int(input("Gib dein Alter ein: "))
behinderung = int(input("Gib deine Behinderung in Prozent ein: "))
betriebszugehoerigkeit = int(input("Gib deine Betriebszugehörigkeit in Jahren ein: "))

urlaubstage = berechne_urlaubstage(alter, behinderung, betriebszugehoerigkeit)
print("Der Urlaubsanspruch beträgt", urlaubstage, "Tage.")
