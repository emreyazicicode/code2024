
marks = {
    'Anar Gasimov': 78, # ==> C
    'Fariz Azimov': 71, # ==> 
    'Fatima Umudova': 87,
    'Fazil Zeynalov': 93,
    'Kamilla Mirzeyeva': 91,
    'Khagani Gasimov': 79,
    'Nigar Jahangirli': 96,
    'Orkhan Mustafayev': 92,
    'Sabina Muradzada': 94,
    'Samir Suleymanov': 88,
    'Sevinj Amanova': 81,
    'Ujar Ismayilzada': 82,
    'Ulvi Hasanov': 82,
    'Shargiyya Mahmudzada': 87
}

names = list(marks.keys())

for name in names:
    print(name.upper())

values = list(marks.values())
print(values)

# 91 - 100 ==> A
# 81 - 90  ==> B
# 71 - 80  ==> C
# 61 - 70  ==> D
# 0 -  60  ==> E [else, other, remaning, rest]

for v in values:
    if v > 90:
        print('GRADE A', v)
    elif v > 80:
        print('GRADE B', v)
    elif v > 70:
        print('GRADE C', v)
    elif v > 60:
        print('GRADE D', v)
    else:
        print('GRADE E', v)

print('=======================================')

for v in values:
    if v >= 91 and v <= 100:
        print('GRADE A', v)
    if v >= 81 and v <= 90:
        print('GRADE B', v)
    if v >= 71 and v <= 80:
        print('GRADE C', v)
    if v >= 61 and v <= 70:
        print('GRADE D', v)
    if v <= 50:
        print('GRADE E', v)





