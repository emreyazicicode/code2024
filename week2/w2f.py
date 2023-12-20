import string


c = 25

print("Hava sicakligi=", c)
#* Hava sicakligi= 25

print("Hava sicakligi=" + str(c))


print("Hava sicakligi=c")
# Hava sicakligi=c

print("FORMATTED", f"Hava sicakligi={c}")


print("FORMATTED", f"Hava sicakligi={int(c/5)}")



a = f"xjgajfdsjfls" #* Formatted string

name = "Emre"
age = 39

print("Merhaba benim adim " + name + ", ben " + str(age) + " yasindayim")

print(f"Merhaba benim adim {name}, ben {age} yasindayim")

print("Merhaba benim adim {name2}, ben {age2} yasindayim".format(age2 = 39, name2 = 'Emre'))

print("Merhaba benim adim {}, ben {} yasindayim".format("Emre", 39))

#! print( "For only {price:.2f} dollars!".format(price = 49) )


#* REGEX
#* REGULAR EXPRESSIONS
import re

#* REGEX is a "syntax checking" methodology

email = "salam_34@naber.com"

emails = [
    'sdfafsf',
    '@naber.com',
    'salam@naber.com',
    'salam_3@naber.com',
    'salam34@naber.com',
    'salam.salam@naber.com',
    '.salam@naber.com',
    '!salam@naber.com',
    '_salam@naber.com.tr',
    'salam.@naber.com',
    'sa.lam@naber.com',
    'a@aasdfds.com',
    'salam.salam@yahoo',
    'salam@naber.yirv',
    'salam.@naber2.com',
    'salam@salam2@naber.com',
    'emre.yazici@',
    'salam@naber'
]

#! EMAIL
#* There must be a (only) "@" TAMAM
#* Before "@" there must be a string, word/keyword/name like
#* After "@" there must be a domain TAMAM

#! DOMAIN
#* There must be at least one "." TAMAM
#* The first part before "." must be a string, word/keyword/name like
#* After "." it must be an extension TAMAM

#! EXTENSION
#* An extension usually is short! examples: com net org ru .... TAMAM



def checkNameLike( name: str ) -> bool:
    if len(name) < 2: return False
    if not name[0].isalpha(): return False
    for i in name:
        if not i.isalnum(): # abcdf... 012345 
            return False
    return True


def checkEmail( address: str ) -> bool:
    if "@" not in address: return False
    if "." not in address: return False
    hisseler = address.split("@")
    if len(hisseler) != 2: return False
    
    name = hisseler[0]
    domain = hisseler[1]
    if len(name) < 2: return False
    if len(domain) < 2: return False
    if "." not in domain: return False

    hisselerdomain = domain.split('.')
    if hisselerdomain[1] not in ['com', 'net', 'org', 'ru']: return False

    if not checkNameLike(name): return False
    if not checkNameLike(hisselerdomain[0]): return False
    
    return True


print('=' * 80)
for email in emails:
    print(email, checkEmail(email))




email   = "Salam_34@naber.com"
pattern = "lllllsdd@lllll.lll"

name    = "Ahmet"
pattern = "ullll"

tarih   = "19/01/2023"
pattern = "dd/dd/dddd"


def convertToPattern( inp: str ) -> str:
    output = ""
    for i in inp:
        if i.islower() and i.isalpha():
            output = output + "l"
        elif i.isupper() and i.isalpha():
            output = output + "u"
        elif i.isdigit():
            output = output + "d"
        elif i in ['_', '.', '@']:
            output = output + i
        else:
            output = output + "?"

    return output


print("=" * 80)
print( convertToPattern( email )) # STRING PATTERN
print(email)


"""



Bu fikirlər İTV-nin efirində yayımlanan “Diqqət Mərkəzi” verlişində səsləndirilib.

“\w+(\s\w+)+”


\w  ==> karakter [a-z, A-Z, əş...]
\w+ ==> KELIME, word
\s\w+ ==> " verlişində"

(\s\w+)+ ==> kelimeler

\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+
\s\w+\s\w+\s\w+
\s\w+\s\w+
\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+<



sentence = \w+\s\w+\s\w+\.
sentence = "Ben eve geldim."



REGEX icinde, "."

"." ==> ANYTHING






"""

# 12/12/2023
# 12.12.2022
# 12 Jan 2023
# Jan 12 2023
# 12-12-2023
# 12-12-2023 18:50

# 9,5
# 9.5



#* MATCH
text = "ahmet@hotmail.com"
pattern = r"\w+@\w+\.\w+" # Bana bir tane UPPER CASE LETTER ILE MATCH ET

if re.match( pattern, text ):
    print(f"{text} ifadesi, {pattern} ile match ediyor")


text = "12-12-2023"
pattern = r"\d+-\d+-\d+" # Bana bir tane UPPER CASE LETTER ILE MATCH ET

if re.match( pattern, text ):
    print(f"{text} ifadesi, {pattern} ile match ediyor")






