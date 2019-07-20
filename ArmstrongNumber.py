#armstrong sayısı
girilenSayi = int(input("üç basamaklı bir sayı gir :"))

sayiYuzlerBasamak = int(girilenSayi / 100);
sayiOnlarBasamak = int((girilenSayi - (sayiYuzlerBasamak * 100)) / 10)
sayiBirlerBasamak = int((girilenSayi - (sayiYuzlerBasamak * 100) - (sayiOnlarBasamak * 10)));

if (girilenSayi == (pow(sayiYuzlerBasamak,3) + (pow(sayiBirlerBasamak,3)) + (pow(sayiOnlarBasamak,3)))):
    print("sayı armstrong sayısıdır")
    print(sayiBirlerBasamak)
    print(sayiOnlarBasamak)
    print(sayiYuzlerBasamak)
else :
    print("sayı armstrong sayısı değildir.")
    print(sayiBirlerBasamak)
    print(sayiOnlarBasamak)
    print(sayiYuzlerBasamak)

