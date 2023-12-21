
import re

#! pattern = re.compile(r"\w+\.\w+\.\w+") #* HAZIRLIYOR  PREPARE MEMORY DAHA HIZLI CALISMAK ICIN
#! DAHA HIZLI ISTIFADE ETMEMIZ ICIN
#! pattern.match("www.google.com")


text = "www.google.com"
pattern = "\w+\.\w+\.\w+"

if re.match(pattern, text):
    print(f"{text} metni, {pattern} ile match ediyor")


text = """
Bu gün Xankəndi şəhərində tarixi oyun keçiriləcək.

Oxu.Az xəbər verir ki, Ağdamın “Qarabağ” komandası Azərbaycan kubokunun 1/8 final mərhələsindəki oyunu adını daşıdığı Qarabağ bölgəsinin mərkəzi şəhərlərindən olan Xankəndidə keçirəcək. “Qarabağ” MOİK-lə üz-üzə gələcək.

Xankəndi stadionunda reallaşacaq qarşılaşma  mustafa@yahoo.com saat 14:00-da başlayacaq. Matçın qalibi 1/4 finalda “Sabah”la qarşılaşacaq. Oyunu yüzlərlə tamaşaçı stadiondan canlı izləyəcək.

Xatırladaq ki, bu, 30 illik fasilədən sonra Qarabağ bölgəsinin işğaldan azad edilən hissəsində ilk rəsmi oyun olacaq. Son dəfə işğal altında olmuş ərazilərdə oyun 1993-cü ilin may ayında Azərbaycan çempionatında “Qarabağ”la “Turan” (“Turan Tovuz”) arasında olub.

ahmet@domain.com

Ağdamın “İmarət” stadionunda keçirilmiş həmin matçda “Qarabağ” 2:1 hesabı ilə qələbə qazanıb. Bu oyundan iki ay sonra Ağdam işğal edilib.
"""

# * Extracting "tokens" which matches with given pattern within text
results = re.findall(r"[a-zəŞşÜüĞğÖöÇçİıA-Z]+", text)
print(results)

# * Extracting "tokens" (NOT) which matches with given pattern within text
NOTresults = re.findall(r"[^a-zəŞşÜüĞğÖöÇçİıA-Z\s]+", text)
print(NOTresults)

emailler = re.findall(r"\w+@\w+\.\w+", text)
print(emailler)


results = re.findall(r"^\w+", text)

#* ^ ==> 1. meaning if it is in a [] ==> NOT
#* ^ ==> 2. meaning if it is out of a [] ==> beginning



print(results)

p = r"^\d\d\.\d\d\.\d\d\d\d$"
s = "12.12.2022 xadsfjsadfjdsafjdslf ja;d"
# s = "12.12.2022"

if re.match(p, s):
    print("s, p ile match ediyor")



e = "ahmet@domain.com asdf"

#* TUM PATTERNLERDE, ^$ kullanalim
#* IF WE WANT THE PATTERN TO MATCH EXACLTY (FROM BEGINNING TO END), we use ^$
#* IF WE WANT TO SEARCH IN TEXT, WE DONT


s = "ahmet@domain.com"
p = r"^\w+@\w+\.\w+$" #! WHOLE LINE MATCH, EXACT MATCH

if re.match(p, s):
    pass

