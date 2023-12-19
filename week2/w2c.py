import pprint as pp
from ozkutuphane import *

classroom_marks = [30, 40, 90, 80, 50, 55, 57, 68, 87, 78, 93, 100, 0, 17, 46, 49, 23, 88]

#! 50





yenimarks = classroom_marks[:] #* CLONE

#* the marks which passed the class
sinifigecennotlar = [i for i in classroom_marks if i >= 50]
print(sinifigecennotlar)
sinifigecennotlar_average = Average( sinifigecennotlar )
print("passed ortalamasi", sinifigecennotlar_average)

failed = [i for i in classroom_marks if i < 50]
print(failed)
failed_average = Average( failed )
print("failed ortalamasi", failed_average)



def grade( mark: int) -> str:
    if mark >= 90: return 'A'
    elif mark >= 80: return 'B'
    elif mark >= 70: return 'C'
    elif mark >= 60: return 'D'
    elif mark >= 50: return 'E'
    elif mark >= 35: return 'F'
    return 'G'
Average = lambda Values: sum(Values) / len(Values)
classroom_marks = [30, 40, 90, 80, 50, 55, 57, 68, 87, 78, 93, 100, 0, 17, 46, 49, 23, 88]
genel_ortalama = Average( classroom_marks )
ortalama_ustunde = [grade(i) for i in classroom_marks if i > genel_ortalama]
print("ortalama_ustunde", ortalama_ustunde)

ortalama_altinda = [grade(i) for i in classroom_marks if i < genel_ortalama]
print("ortalama_altinda", ortalama_altinda)

classroom_grades = [grade(i) for i in classroom_marks]
print("classroom_grades", classroom_grades)

for g in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    print("TUM, HEPSI, ALL", g, classroom_grades.count(g))








stores = [
    {'name': 'store1', 'total_sales': 300000, 'staff_count': 5} ,
    {'name': 'store2', 'total_sales': 250000, 'staff_count': 3} ,
    {'name': 'store3', 'total_sales': 600000, 'staff_count': 12} ,
    {'name': 'store4', 'total_sales': 450000, 'staff_count': 7} ,
    {'name': 'store5', 'total_sales': 750000, 'staff_count': 10} ,
    {'name': 'store6', 'total_sales': 950000, 'staff_count': 13} ,
    {'name': 'store7', 'total_sales': 150000, 'staff_count': 2} ,
    {'name': 'store8', 'total_sales': 400000, 'staff_count': 8} ,
    {'name': 'store9', 'total_sales': 500000, 'staff_count': 9} 
]

#! LIST OF DICTIONARIES
#! -----------> list of keys and values
pp.pprint(stores)


satislar = [i['total_sales'] for i in stores]
print(satislar)
avg_satis = Average(satislar)
print("Average satis", Average(satislar))

personal = [i['staff_count'] for i in stores]
avg_personal_count = Average( personal )
print("avg_personal_count", avg_personal_count)


problemli_storelar = [
    i['name'] 
    for i in stores 
    if i['staff_count'] > avg_personal_count 
        and 
    i['total_sales'] < avg_satis
]
print("problemli_storelar", problemli_storelar)



print('=' * 80)
yeniliste = [q['total_sales'] for q in stores]
print(yeniliste)
print("TOTAL GAIN FOR COMPANY", sum(yeniliste))
# SELECT x,y,z FROM 




yeniliste = [q['name'] for q in stores if q['total_sales'] > avg_satis]


print("GAIN OF COMPANY", sum( [i['total_sales'] for i in stores] ))
print("TOTAL EMPLOYEES", sum( [i['staff_count'] for i in stores] ))

avg_sales_per_person = sum( [i['total_sales'] for i in stores] ) / sum( [i['staff_count'] for i in stores] )
print(avg_sales_per_person)


below_avg_sales_per_person = [
    i['name']                      #* what to extract , output
    for i in stores                #* source
    if i['total_sales'] / i['staff_count'] > avg_sales_per_person  #* condition
]

print(below_avg_sales_per_person)


