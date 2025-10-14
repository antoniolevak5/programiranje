#Izbornik za pretvarač mjernih jedinica
def ispisi_izbornik():  #ovom naredbom uljepšavamo cjelokupni kod
    print("----------------------")
    print("Izbornik za pretvarač mjernih jedinica")
    print("----------------------")
    print("1. Pretvarač volta(V) u milivolte(mV)")
    print("2. Pretvarač ohma(Ω) u kiloohme(kΩ)")
    print("3. Pretvarač ampera(A) u miliampere(mA)")
    print("0. Izlaz iz programa")
    print("----------------------")    
def pretvori_V_u_mV(): 
    try: 
            print("Pretvarač volta(V) u milivolte(mV)")
            volt = float(input("Upiši napon (u V):"))
            mV = volt*1000
            print(f"Napon je: {mV} mV") #Ispis rezultata
    except ValueError:
            print("GREŠKA: Unesena vrijednost nije ispravan broj.")
def pretvori_Ω_u_kΩ():
    try:
            print("Pretvarač ohma(Ω) u kiloohme(kΩ)")
            ohm = float(input("Upiši otpor (u Ω):"))
            kΩ = ohm/1000
            print(f"Otpor je: {kΩ} kΩ")
    except ValueError:
            print("GREŠKA: Unesena vrijednost nije ispravan broj.")
def pretvori_A_u_mA():
    try:
            print("Pretvarač ampera(A) u miliampere(mA)")
            amper = float(input("Upiši jakost struje (u A):"))
            mA = amper*1000
            print(f"Jakost struje je: {mA} mA")
    except ValueError:
            print("GREŠKA: Unesena vrijednost nije ispravan broj.")

while True:
    ispisi_izbornik()
    
    try:
        opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 0):"))
    except ValueError:  # Ovaj kod se izvršava SAMO ako se dogodi ValueError
        print("GREŠKA: Unesena vrijednost nije ispravan broj.")
        continue #Ovom naredbom petlja odmah krene ispočetka
    #Struktura grananja
    if opcija == 1:   # == != < > <> >= <=
         pretvori_V_u_mV()
       
    elif opcija == 2:
         pretvori_Ω_u_kΩ()
        
    elif opcija == 3:
          pretvori_A_u_mA()
        
    elif opcija == 0:
        print("Hvala na korištenju. Doviđenja!")
        break #Ovom naredbom prekidamo while True petlju
    else:

        print("GREŠKA: Opcija ne postoji. Unesite broj od 0 do 3.")
