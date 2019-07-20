# Fibonacci Değerini Bulan Fonksiyon

def FibonacciDegeriBul(n):
    if n < 0:
        print("Değer sıfırdan büyük olmalıdır.")
   # İlk Fibonacci sayısı 0'dır
    elif n == 1:
        return 0
    # İkinci Fibonacci sayısı 1'dir
    elif n == 2:
        return 1
    else:
        return FibonacciDegeriBul(n - 1) + FibonacciDegeriBul(n - 2)



sayi = int(input("fibonacci değerini bulmak istediğiniz sayı : "))
print(FibonacciDegeriBul(sayi))
