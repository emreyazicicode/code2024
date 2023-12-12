# -*- coding: utf-8 -*-

# String operations

# Split
a = "ahmet@gmail.com"
print( a.split("@") )

# Concat
b = "Mustafa"
c = "Ozturk"
print(b + ' ' + c)

# Join
talebeler = ['Ahmet', 'Mehmet', 'Dilek', 'Canan']

print("\n".join(talebeler))

# Repeat
print("A" * 5)

# List
l = [1,2,3]
l = []

l.append( 'xx' )
l.append( 'yy' )
l.append( 'zz' )
l.append( 'aa' )
l.insert( 0, 'bxqb' )
print(l)

# Accesing 3rd item
print(l[3])

# Accesing 3rd as a list
print(l[3:4])

# accessing 3rd and 4th item
print(l[3:5])

# Accesing from beging
print(l[:2])

# Accesing from end
print(l[2:])

# Accessing
print(l[:])

# Last element
print(l[-1])
print(l[ len(l) - 1 ])

# Last before end
print(l[-2])

# Last 2
print(l[-2:])

# We can use it in strings also

text1 = "Kamran Əliyev: “Azərbaycanın həbs etdiyi erməni separatçılar barəsində istintaq davam edir”"
text2 = "YAP-ın növbədənkənar Prezident seçkilərində namizədi İlham Əliyev olacaq - RƏSMİ"
text3 = 'Qurban Yetirmişli: "Azərbaycanda güclü zəlzələnin başvermə ehtimalı yoxdur"'
text4 = 'Dövlət və hökumət rəsmiləri Fəxri xiyabanda Heydər Əliyevin xatirəsini yad ediblər'
text5 = "Son dakika: Dövlət və hökumət rəsmiləri Fəxri xiyabanda President'in xatirəsini yad ediblər"


alltext = ["Kamran Əliyev: “Azərbaycanın həbs etdiyi erməni separatçılar barəsində istintaq davam edir”",
 "YAP-ın növbədənkənar Prezident seçkilərində namizədi İlham Əliyev olacaq - RƏSMİ",
 'Qurban Yetirmişli: "Azərbaycanda güclü zəlzələnin başvermə ehtimalı yoxdur"',
 'Qurban Yetirmişli:"Azərbaycanda güclü zəlzələnin başvermə ehtimalı yoxdur"',
 'Dövlət və hökumət rəsmiləri Fəxri xiyabanda Heydər Əliyevin xatirəsini yad ediblər',
 "Son dakika: Dövlət və hökumət rəsmiləri Fəxri xiyabanda President'in xatirəsini yad ediblər"]


t1 = 'Ahmet'
t2 = "Ahmet"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def determineTextType( text: str ):
    quotes = ['"', '“', '”', '‘', '’', "'"]
    #: Rule 1
    if not ":" in text: return False
    #: Count all quotes
    total_count = 0
    for q in quotes:
        total_count = total_count + text.count( q )
    #: If total_count < 2
    if total_count < 2: return False

    parts = text.split(':')
    parts[1] = parts[1].strip().strip("".join(quotes))  # "“”‘’'

    return tuple(parts)


print('=' * 80)


for t in alltext[:]  :
    print(t, bcolors.FAIL + bcolors.BOLD, determineTextType( t ), bcolors.ENDC)


