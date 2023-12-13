import random
text = """
“Azərbaycan iqlim dəyişikliyi ilə mübarizə üzrə qlobal fəaliyyəti ardıcıl olaraq dəstəkləyir və enerji səmərəliliyinin artırılması üçün müxtəlif tədbirlər həyata keçirir”.

Bunu Azərbaycan Prezidenti İlham Əliyev “X” hesabında bildirib.

Paylaşımda qeyd edilir: “Təmiz ətraf mühit və yaşıl inkişaf milli prioritetlərimizdəndir. Azərbaycanda bərpa olunan enerji geniş vüsət alır.

2024-cü ildə BMT-nin İqlim Dəyişikliyi üzrə Çərçivə Konvensiyasının Tərəflər Konfransının (COP29) 29-cu Sessiyasına ev sahibliyi etməyimiz iqlim dəyişikliyi ilə mübarizə üzrə qlobal səylərə töhfə vermək əzmimizdən irəli gəlir. Azərbaycana verdiyi dəyərli dəstəyə görə bütün ölkələrə səmimi təşəkkürümü bildirirəm. Biz COP29-u uğur hekayəsinə çevirmək üçün əlimizdən gələni edəcəyik.

Birləşmiş Ərəb Əmirliklərinin Prezidenti Şeyx Mohamed bin Zayed Al Nahyana tədbirin gözəl təşkilinə görə təşəkkür edir və iqlimlə bağlı tədbirləri inkişaf etdirmək üçün birlikdə işləməyi səbirsizliklə gözləyirik”.
"""

text = text.lower()

letters = ['A','B','C','Ç','D','E','Ə','F','G','Ğ','H','X','I','İ','J','K','Q','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','a','b','c','ç','d','e','ə','f','g','ğ','h','x','ı','i','j','k','q','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
letters = ['a','b','c','ç','d','e','ə','f','g','ğ','h','x','ı','i','j','k','q','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']

kopya_letters = letters[:]

sifreleme = {}

# This is to check that all are letters
for letter in letters:
    if len(letter) > 1:
        print(letter, len(letter))

for letter in letters:
    chosen = random.choice( kopya_letters )
    sifreleme[ letter ] = chosen
    kopya_letters.remove( chosen )


print(sifreleme)
sifrelenmis_text = ""
for l in text:
    if l in sifreleme:
        sifrelenmis_text = sifrelenmis_text + sifreleme[l]
    else:
        sifrelenmis_text = sifrelenmis_text + l

print(sifrelenmis_text)

