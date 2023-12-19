stores = [
    {'name': 'store1', 'total_sales': 300000, 'staff_count': 5, 'products': ['tshirt', 'shoes', 'socks', 'polo']} ,
    {'name': 'store2', 'total_sales': 250000, 'staff_count': 3, 'products': ['tshirt', 'shoes', 'underwear', 'jumper', 'short', 'cardigan']} ,
    {'name': 'store3', 'total_sales': 600000, 'staff_count': 12, 'products': ['tshirt', 'shoes', 'socks', 'jeans', 'short']} ,
    {'name': 'store4', 'total_sales': 450000, 'staff_count': 7, 'products': ['tshirt', 'shoes', 'socks', 'pants']} ,
    {'name': 'store5', 'total_sales': 750000, 'staff_count': 10, 'products': ['pants', 'socks']} ,
    {'name': 'store6', 'total_sales': 950000, 'staff_count': 13, 'products': ['tshirt', 'pants', 'socks', 'polo']} ,
    {'name': 'store7', 'total_sales': 150000, 'staff_count': 2, 'products': ['tshirt', 'shoes', 'sweather']} ,
    {'name': 'store8', 'total_sales': 400000, 'staff_count': 8, 'products': ['tshirt', 'shoes', 'socks', 'polo']} ,
    {'name': 'store9', 'total_sales': 500000, 'staff_count': 9, 'products': ['tshirt', 'shoes', 'socks', 'shirt', 'short']} ,
]


#* EXTRACTING MORE THAN ONE COLUMN, information
information = [
    (i['name'], i['staff_count'], len(i['products']) )  #* KAC TANE / ADET PRODUCT
    for i in stores
]

information2 = [
    {'name': i['name'], 'staff_count': i['staff_count'], '#ofproducts': len(i['products']) }
    for i in stores
]

print(information)
print(information2)

