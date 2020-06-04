import math as m
def timeConverter(seconds):
    hourtemp = m.floor(seconds/3600) # untuk mencari jam
    if hourtemp > 99 : # jika hasil modulus jam lebih dari 99 makan akan dimodulus dan hasil modulus akan dikembalikan ke sisa
        batashour = hourtemp%99
        hour = hourtemp - batashour 
        sisa1 = (seconds%3600) + (batashour * 3600)
    else : # jika tidak lebih dari 99 maka jam adalah hasil dari second modulus 3600
        hour = hourtemp
        sisa1 = seconds%3600

    minutestemp = m.floor(sisa1/60) # untuk mencari menit
    if minutestemp > 60: # jika hasil modulus menit lebih dari 60 makan akan dimodulus dan hasil modulus akan dikembalikan ke sisa
        batasminutes = minutestemp%60
        minutes = minutestemp - batasminutes
        sisa2 = (sisa1%60) + (batasminutes * 60)
    else: # jika tidak lebih dari 60 maka menit adalah hasil dari second modulus 60
        minutes = minutestemp
        sisa2 = sisa1%60
    detik = sisa2

    if detik < 10 and minutes < 10 and hour < 10: # kondisi jika hasil detik menit jam kurang dari 10
        return f"0{hour}:0{minutes}:0{detik}"
    elif detik < 10 and minutes < 10: # kondisi jika hasil detik menit kurang dari 10
        return f"{hour}:0{minutes}:0{detik}" 
    elif detik < 10 and hour < 10: # kondisi jika hasil detik jam kurang dari 10
        return f"0{hour}:{minutes}:0{detik}"
    elif minutes < 10 and hour < 10: # kondisi jika hasil menit jam kurang dari 10
        return f"0{hour}:0{minutes}:{detik}"
    elif detik < 10: # kondisi jika hasil detik saja yang kurang dari 10
        return f"{hour}:{minutes}:0{detik}"
    elif minutes < 10: # kondisi jika hasil menit saya yang kurang dari 10
        return f"{hour}:0{minutes}:{detik}"
    elif hour < 10: # kondisi jika hasil jam saya yang kurang dari 10
        return f"0{hour}:{minutes}:{detik}"
    else:
        return f"{hour}:{minutes}:{detik}"

#### Stuck jika input yang diinginkan integer tetapi saat dimasukkan input float atau 3.5 tidak diproses
inputseconds = input("Masukkan detik : ")
if inputseconds.isdigit() == True: # jika input berupa digit maka akan masuk ke if ini
    if int(inputseconds) > 359999: # jika input detik lebih dari 359999 makan akan akan masuk ke if ini
        print("Invalid Input!")
    else:
        print(timeConverter(int(inputseconds)))
else: #jika input yang dimasukkan bukan berupa angka
    print("Invalid Input!")

