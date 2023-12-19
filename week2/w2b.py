
#* LAMBDA in FUNCTIONS
average = lambda items: sum(items) / len(items)

#* LAMBDA in IF
point = 80
result = 'Passed' if point > 60 else 'Failed'

#* LAMBDA in LIST / DICTIONARIES

faizler = [ 0.20, 0.30, 0.15, 0.19, 0.22, 0.50, 0.90, 0.80, 0.55, 1.12, 0.04, -0.05, "0", "SALAM"]
#* MIXTURE = [water, soil, dirt *camur, neft, stone....]
#* HER 1 dakika

def neftFaizKontrol( faiz: float ) -> bool:
    if type(faiz) is str: return False # EGER FAIZ IN TYPE I STRING ISE FALSE DONDUR
    if faiz > 1.0: return False
    if faiz < 0.0: return False
    return True

#! ==> became valid: faizler = [ 0.20, 0.30, 0.15, 0.19, 0.22, 0.50, 0.90, 0.80, 0.55, 0.04]

tazeliste = faizler[:] #* CLONE, birebir clone,
tazeliste2 = [faiz for faiz in faizler]
#            [faiz]

ornekliste = ['x'] * 3

tazeliste3 = []
for faiz in faizler: #* faizlerin icindeki her bir faiz icin
    #! filtreleme
    if type(faiz) is not str:
        tazeliste3.append( faiz ) # tazeliste3'e, ekle, "O ITEM", "CURRENT", "ACTIVE"

print(faizler)
print(tazeliste)
print("tazeliste2", tazeliste2)
print(tazeliste3)
print(ornekliste)





tazeliste = faizler[:]
tazeliste2 = [faiz for faiz in faizler if type(faiz) is not str]

tazeliste2 = [ #* bir liste olustur
    faiz  #* listenin itemlari, "faiz" variable dan olussun
    for faiz in faizler  #* faizlerin icindeki "HER BIR " faiz icin 
    if type(faiz) is not str #* SUCH THAT OYLE KI, sadece "string olmayanlari" # FILTRE!!!!
]

tazeliste3 = [
    faiz for faiz in tazeliste2
    if faiz >= 0.0
]

tazeliste4 = [
    faiz for faiz in tazeliste3
    if faiz <= 1.0
]

print("tazeliste2", tazeliste2)
print("tazeliste3", tazeliste3)
print("tazeliste4", tazeliste4)


tazeliste5 = [faiz for faiz in faizler if type(faiz) is not str and faiz <= 1.0 and faiz >= 0.0 ]
print("tazeliste5", tazeliste5)


tazeliste5 = [
    faiz                      #* HANGI ELEMANLARDAN OLUSACAK, ITEM   target
    for faiz in faizler       #* ANA KAYNAK NERESI?                  source
    if  type(faiz) is not str #* FILTRE, SART, KOSUL,....
        and 
        faiz <= 1.0 
        and 
        faiz >= 0.0 
]



a = "3"
b = "3%"
print( a.endswith("%") )
print( b.endswith("%") )

print('=' * 80)

#* faizler = [ '20%', '30%', '15%' .... ]

tazeliste6 = faizler[:] #* NO FILTERING, NO MANIPULATION

for faiz in faizler: 
    if type(faiz) is not str and faiz <= 1.0 and faiz >= 0.0: #* FILTRE
        print(str(round(faiz * 100)) + '%') #* CONVERT, MANIPULATION, TRANSFORMATION....




tazeliste7 = [
    str(round(faiz * 100)) + '%' 
    for faiz in faizler 
    if type(faiz) is not str 
        and 
    faiz <= 1.0 
        and 
    faiz >= 0.0 
]

print("INPUT ", faizler)
print("OUTPUT", tazeliste7)

