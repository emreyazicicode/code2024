#: Import
import datetime
import pprint

pp = pprint.PrettyPrinter()
# BASIC, ATOMIC, SIMPLE DATA TYPES:
isim = "Emre" # str, string, text, metin, yazi
yas = 39 # int, integer, tam sayi, number, numeric, sayisal
askerlik_yapti_mi = True # Bool, Var/Yok, Evet/Hayir, Boolean
boy = 178.2 # float, double, floating number ","
d_o_b = datetime.date(1984, 5, 5)

# VARIABLE, DEGISKEN, Temporarily stores a "value"
# VALUE: FACTS, OLCUM, MEASUREMENT

# NOTE: data may have coordinates (indexes: column, row)
# NOTE: data have "types" (str, int, ....)
# NOTE: data have capacity (not our problem)

# NOTE: Synonyms
# ROW = SATIR = OBJECT = LINE
# COLUMN = ATTRIBUTE = FEATURE = SUTUN = KOLON

# COMPLEX DATA TYPES:
TALEBELER = ['Ahmet', 'Mehmet', 'Dilek']
a = "Emre"

# Value
print("selam")
# Variable
print("the value of a", a)
# Value
print("a")

print(type(TALEBELER))
# Multiple
print("neferin ozellikleri", isim, yas, askerlik_yapti_mi, boy, d_o_b)
# Operation
print("2+3 islemi", 2+3)

print("LISTE", TALEBELER)

COORDINATES = (26.45, 36.42) # X, Y koordinat

print('coordinate', COORDINATES)

boy = 178.0

# Python is a scripting language
# Python is a late-binding language


# c:
# int i = 0;
i = 3

talebe = {
    'isim': 'Mustafa',
    'soyisim': 'OZTURK',
    'age': 35
}


print("TALEBE", talebe)



GENDERS = ['m', 'm','m','f','f','f']
AGES = [26,24,23,22,26,21]


NAMES1 = ['Ahmet', 'Kamilla', 'Anar', 'Mehmet', 'Dilek', 'Feride']
NAMES2 = ['Ahmet', 'Anar', 'Mehmet', 'Dilek', 'Feride', 'Kamilla']
#! NAMES1 != NAMES2

print('GENDERS', GENDERS)
print('AGES', AGES)
print('NAMES', NAMES1)


talebe1 = {'age': 23, 'gender': 'm', 'name': 'Mustafa'}
talebe2 = {'gender': 'm', 'name': 'Ali', 'age': 26}
talebe3 = {'name': 'Kamilla', 'age': 22, 'gender': 'f'}
print("talebe1", talebe1)
print("talebe2", talebe2)
print("talebe3", talebe3)



talebeA = {'age': 23, 'gender': 'm', 'name': 'Mustafa'}
talebeB = {'name': 'Mustafa', 'age': 23, 'gender': 'm'}
#! talebeA = talebeB


print("======================")
talebelerin_tum_ozellikleri = [
    'Ahmet', 'Mehmet', 'Ali'
]

talebelerin_tum_ozellikleri = [
    {'age': 23, 'gender': 'm', 'name': 'Mustafa'},
    {'gender': 'm', 'name': 'Ali', 'age': 26},
    {'name': 'Kamilla', 'age': 22, 'gender': 'f'}
]
pp.pprint(talebelerin_tum_ozellikleri)





print("======================")
talebeA = {'age': 23, 'gender': 'm', 'name': 'Mustafa', 'hobbies': ['chess', 'football'] }


all_students = [
    {'name':'Anar', 'surname':'Gasimov','gender':'male','age':25, 'hobbies': ['chess']},
    {'name':'Fariz', 'surname':'Azimov','gender':'male','age':28, 'hobbies': ['football']},
    {'name':'Fatima', 'surname':'Umudova','gender':'female','age':20, 'hobbies': ['painting', 'piano playing']},
    {'name':'Fazil', 'surname':'Zeynalov','gender':'male','age':26},
    {'name':'Kamilla', 'surname':'Mirzeyeva','gender':'female','age':22},
    {'name':'Khagani', 'surname':'Gasimov','gender':'male','age':28},
    {'name':'Nigar', 'surname':'Jahangirli','gender':'female','age':26},
    {'name':'Orkhan', 'surname':'Mustafayev','gender':'male','age':23},
    {'name':'Sabina', 'surname':'Muradzada','gender':'female','age':20},
    {'name':'Samir', 'surname':'Suleymanov','gender':'male','age':25},
    {'name':'Sevinj', 'surname':'Amanova','gender':'female','age':25},
    {'name':'Ujar', 'surname':'Ismayilzada','gender':'male','age':25},
    {'name':'Ulvi', 'surname':'Hasanov','gender':'male','age':31},
    {'name':'Shargiyya', 'surname':'Mahmudzada','gender':'female','age':28}
]




# A string is a list of characters
a = "xyz"
# Convert a string into a list of characters
print("a          : ", a)
print("a as a list: ", list(a))


# SET 
a = {3,4,5}
b = (3,4,5)
c = [3,4,5]
d = {'x': 3, 'y': 4, 'z': 5}


c = [3,4,5,5] # same item can be occoured in a list!
a = {3,4,5,5} # but not in a set

print("a", a)

print("list to set", list(set(c)))







def f(m,a):
    return m * a

y = f(3, 10)
print("y", y)

BUYUKLER = ['A','B','C','Ç','D','E','Ə','F','G','Ğ','H','X','I','İ','J','K','Q','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z']
KUCUKLER = ['a','b','c','ç','d','e','ə','f','g','ğ','h','x','ı','i','j','k','q','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
RAKAMLAR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
OZEL = ['~','!','@','#','$','%','^','*','-','_','=','+','[','{',']','}','/',';',':',',','.','?']

sample = ['a', 'b', 'c', '1', '2', 'xx', 'yyyyyy', 'zzz']

for i in sample:
    length = len(i)
    print(i, length)



# When you call this function you must pass an argument "sifre" where its type is "str"
# This function returns a "bool", whether the given password is "correct" or "not"
def sifreKontrolEt( sifre: str ) -> bool:
    karakter_sayisi = len( sifre )
    karakterler = list( sifre ) # sifre: stringini, bir listeye CEVIRDIM (convert)
    tek_karakterler = list(set(karakterler)) # benzersiz, tekil, yegane, different, unique
    # Rule1: at least 7 characters
    if karakter_sayisi < 7: return False
    # Rule2: at most 100 characters
    if karakter_sayisi > 100: return False
    # Rule3: at least 3 different characters
    if len(tek_karakterler) < 3: return False
    # Rule4: have both "letters" and "digits"
    digit = False
    upper = False
    lower = False
    special = False
    for k in karakterler:
        if k in RAKAMLAR:
            digit = True
        if k in BUYUKLER:
            upper = True
        if k in KUCUKLER:
            lower = True
        if k in OZEL:
            special = True
    # If no digits, return false
    # If no letters, return false
    if digit == False: return False
    if upper == False: return False
    if lower == False: return False
    if special == False: return False

    return True

print("===================================")
print("===================================")

sifreler = [
    '12!#',
    '1111111111',
    '1234a',
    'ab123',
    '111122223333',
    'eyz13240',
    'Eyzc1234',
    'Eyzc1234!',
    'aaaaaa11111111',
    '112034810  DADwe98r309qyrwerqewr3q9ryewr987y8743yr87ewyrewirewywiurewiuryewiuryewiuryiuewyriuyewiuryewiuryweriuyoiuyewriuayroiuwyrwaoiryweiuryewiur'
]


for sifre in sifreler:
    print( sifre )
    print( sifreKontrolEt(sifre) )
    print('===================')


"""
"Password Requirements
3 or more unique characters
At least 3 of the following: uppercase, lowercase, numeric, or special characters.  The allowed special characters are ~ ! @ # $ % ^ * - _ = + [ { ] } / ; : , . ?  [no spaces allowed!]"												

"""




