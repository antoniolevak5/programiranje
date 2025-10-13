#Izbornik za pretvarač mjernih jedinica
while True:
    print("----------------------")
    print("Izbornik za pretvarač mjernih jedinica")
    print("----------------------")
    print("1. Pretvarač volta(V) u milivolte(mV)")
    print("2. Pretvarač ohma(Ω) u kiloohme(kΩ)")
    print("3. Pretvarač ampera(A) u miliampere(mA)")
    print("0. Izlaz iz programa")
    print("----------------------")    
    opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 0):"))
    #Struktura grananja
    if opcija == 1:   # == != < > <> >= <=
        print("Pretvarač volta(V) u milivolte(mV)")
        volt = float(input("Upiši napon (u V):"))
        mV = volt*1000
        print(f"Napon je: {mV} mV") #Ispis rezultata
    elif opcija == 2:
        print("Pretvarač ohma(Ω) u kiloohme(kΩ)")
        ohm = float(input("Upiši otpor (u Ω):"))
        kΩ = ohm/1000
        print(f"Otpor je: {kΩ} kΩ")
    elif opcija == 3:
        print("Pretvarač ampera(A) u miliampere(mA)")
        amper = float(input("Upiši jakost struje (u A):"))
        mA = amper*1000
        print(f"Jakost struje je: {mA} mA")
    elif opcija == 0:
        print("Hvala na korištenju. Doviđenja!")
        break #Ovom naredbom prekidamo while True petlju
    else:
        print("Pogrešan unos!!")
    
              

         

