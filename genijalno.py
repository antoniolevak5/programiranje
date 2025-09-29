# Izbornik za kalkulator
print("----------------------")
print("Izbornik za kalkulator")
print("----------------------")
print("1. Izračun napona struje")
print("2. izračun otpora struje")
print("3. Izračun jakosti struje")
print("4. Izračun za zbroj serijske otpornike")
print("5. Izračun za zbroj paralelnih otpornika")
print("----------------------")
opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 4 / 5):"))
#Struktura grananja
if opcija == 1:   # == != < > <> >= <=
    print("Izračun napona struje")
    jakost = int(input("Upiši jakost struje: "))
    otpor = int(input("Upiši otpor: "))
    napon = jakost*otpor
    print(f"Napon struje je: {napon} V")
elif opcija == 2:
    print("Izračun otpora struje")
    napon = int(input("Upiši napon: "))
    jakost = int(input("Upiši jakost struje: "))
    otpor = napon/jakost
    print(f"Otpor je: {otpor} ohm")
elif opcija == 3:
    print("Izračun jakosti struje")
    napon = int(input("Upiši napon: "))
    otpor = int(input("Upiši otpor: "))
    jakost = napon/otpor
    print(f"Jakost struje je: {jakost} A")
elif opcija == 4:
    print("Izračun za zbroj serijskih otpornika")
    R1 = int(input("Upiši otpor R1:"))
    R2 = int(input("Upiši otpor R2:"))
    Ruk = R1+R2
    print(f"Zbroj serijskih otpornika je: {Ruk} ohma")
elif opcija == 5:
    print("Izračun za zbroj paralelnih otpornika")
    R1 = int(input("Upiši otpor R1:"))
    R2 = int(input("Upiši otpor R2:"))
    Ruk = 1/(1/R1+1/R2)
    print(f"Zbroj paralelnih otpornika je: {Ruk} ohma")
else:
    print("Pogrešan unos")
