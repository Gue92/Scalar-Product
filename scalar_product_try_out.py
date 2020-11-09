"""Skalarfunktion zweier Vektoren"""

print(" Die Vektor-Eingabe bitte folgendermaßen ausführen: scalar([ , , ],[ , , ]).\n Die Vekotor-Dimension kann selbst bestimmt werden")

def scalar(Vektor1,Vektor2):

    if len(Vektor1)==len(Vektor2):   #Vergleicht die Anzahl der Vektoren Spalten
        
        scalar=0          #Nötig um Aufsummierung immer wieder von 0 zu starten
        
        for i in range(len(Vektor1)):
            scalar += Vektor1[i] * Vektor2[i]      # mit += werden die einzelnen Produkte auf Summiert
        return(scalar)
    else:
        print(" Falsche Eingabe\n Beide Vektoren benötigen die selbe Dimension")

              