def main():
    try:
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
                    raise IndexError
            else:
                raise NameError
            
    except NameError:
        print ("Het zoekwoord", zoekwoord," komt niet voor in de één van de headers, probeer nog een keer.")
        main()
    except IndexError:
        print ("U heeft een bestand gekozen zonder DNA probeer opnieuw")
        main()
        
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

        if ">" in headers[0]:
            return headers, seqs
        else:
            raise IndexError

    except IndexError:
        print ("-"*80)
        print("Het is geen fasta bestand.")
        print("Controleer of het bestand wat je opgegeven hebt een fasta bestand is of geef een andere naam op.")
        print (" ")
        main()
    except FileNotFoundError:
        print ("-"*80)
        print("Het bestand staat niet in de map of geef een andere naam op.")
        print (" ")
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

def knipt(alpaca_seq):
    try:
        bestand_1 = (input ("Geef naam van bestand met de knip enzymen op: ")) + ".txt"
        bestand = open(bestand_1)
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^","")
            if ">" in line:
                raise IndexError
            else:
                if seq in alpaca_seq:
                    print(naam, "knipt in sequentie")
            
    except IndexError:
        print ("Het bestand dat u gekozen heeft bevat geen restrictie enzymen maar headers, probeer opnieuw.")
        knipt(alpaca_seq)
            
    except FileNotFoundError:
        print ("Het bestand",bestand_1," staat niet in de map of geef een andere naam op.")
        knipt(alpaca_seq)
    
    


main()
