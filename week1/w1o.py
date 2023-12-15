
# Production
levels = {
    'high': 'High quality',
    'med': 'Medium quality',
    'low': 'Low quality'
}


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

#   output     # input
students = [
    'Ahmet',   # 0
    'Mehmet',  # 1
    'Ali'      # 2
]

print( students[ 1 ])
print( marks['Anar Gasimov'] )

print("===================")
for m in marks:
    val = marks[m]
    if val > 90:
        print(m, val, 'A')
    elif val > 80:
        print(m, val, 'B')
    # .....
    # HOME WORK



