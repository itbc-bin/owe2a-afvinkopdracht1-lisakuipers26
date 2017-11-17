# Naam:
# Datum:
# Versie:

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's. Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    
    bestand = (input("Geef naam van het bestand van de sequenties: "))+".fa"
    headers, seqs = lees_inhoud(bestand)
    
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:",headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")
    
def lees_inhoud(bestand):
    
    try:
    
        bestand = open(bestand)   
    
    
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line=line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)

        
            
        return headers, seqs
    except FileNotFoundError:
        print("Het bestand staat niet in de map of geef een andere naam op.")
        main()
    


    
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    return dna

# bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken
def knipt(alpaca_seq):
        bestand_1 = (input ("Geef naam van bestand met de knipenzymen op: ")) + ".txt"
        bestand = open(bestand_1)
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^","")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")

    
    


main()
