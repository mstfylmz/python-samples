# faktöriyel hesaplama rekürsif fonksiyon kullanımı
def factorial(n):
    #faktoriyeli hesaplama
    return 1 if (n==1 or n== 0) else n * factorial(n-1)

sayi = int(input("faktoriyelini almak istediğiniz sayı :"))
print(factorial(sayi));