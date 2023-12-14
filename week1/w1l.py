













marks = {
    'Anar Gasimov': 78,
    'Fariz Azimov': 71,
    'Fatima Umudova': 87,
    'Fazil Zeynalov': 93,
    'Kamilla Mirzeyeva': 91,
    'Khagani Gasimov': 79,
    'Nigar Jahangirli': 76,
    'Orkhan Mustafayev': 92,
    'Sabina Muradzada': 94,
    'Samir Suleymanov': 88,
    'Sevinj Amanova': 81,
    'Ujar Ismayilzada': 82,
    'Ulvi Hasanov': 82,
    'Shargiyya Mahmudzada': 87
}

indiye_kadar_olan_en_buyuk_skor = 0

"""
her bir item a bakacagiz
eger o itemin skoru, indiye_kadar_olan_en_buyuk_skor dan buyukse
indiye_kadar_olan_en_buyuk_skor = o itemin skoru
"""

for talebe in marks: # in dictionary, for gives the "KEY"
    key = talebe
    val = marks[talebe]
    if val > indiye_kadar_olan_en_buyuk_skor:
        indiye_kadar_olan_en_buyuk_skor = val


print(indiye_kadar_olan_en_buyuk_skor)

# =====================

l = [45,54,67,76,87,89,0]
indiye_kadar_olan_en_buyuk_value = 0

for pinokyo in l:
    if pinokyo > indiye_kadar_olan_en_buyuk_value:
        indiye_kadar_olan_en_buyuk_value = pinokyo

print("indiye_kadar_olan_en_buyuk_value", indiye_kadar_olan_en_buyuk_value)

#! print(max(l))
#! print(sorted(l)[-1])




