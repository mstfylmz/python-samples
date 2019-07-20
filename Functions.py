
#listenin ilk elemanı ile son elemanını yerini değiştirme
def swapList(newList):
    size = len(newList)

    #Yer Değiştirme
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList

newList=[10,20,30,40,50]
print(newList)
print(swapList(newList))


#palinderom uygulaması
def reverse(s):
    return s[::-1];

def isPalindrome(s):
    rev = reverse(s);
    if(s==rev):
        return True;
    return  False;


print("SOS palindrom bir kelime midir ?");
print(isPalindrome("SOSA"))


#type fonksiyonu..
print(type([]) is list)
print(type([]) is not list)
print(type(()) is tuple)
print(type({}) is dict)
print(type({}) is not list)


#map function nedir
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]

    result = map(lambda x, y: x + y, numbers1, numbers2)
    print(list(result));

