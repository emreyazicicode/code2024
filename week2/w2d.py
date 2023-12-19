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

Average = lambda Values: sum(Values) / len(Values)
#* POLO SATAN STORELARIN ORTALAMA TOTAL_SALES


polo_satan_storelar = [
    i['total_sales']
    for i in stores
    if 'polo' in i['products']
]


polo_satan_storelar = [i['total_sales'] for i in stores if 'polo' in i['products']]
print(Average( polo_satan_storelar) ) 
polo_hec_satmayan_storelar = [i['total_sales'] for i in stores if not 'polo' in i['products']]
print( Average( polo_hec_satmayan_storelar) )


# =======================================================
x = 'socks'
x_satan_storelar = [i['total_sales'] for i in stores if x in i['products']]
x_hec_satmayan_storelar = [i['total_sales'] for i in stores if not x in i['products']]

sales = round(Average( x_satan_storelar), -2)
notsales = round(Average( x_hec_satmayan_storelar), -2)
print(x, sales, notsales)
# =======================================================

print('=' * 80)
for x in ['socks', 'polo']:

    x_satan_storelar = [i['total_sales'] for i in stores if x in i['products']]
    x_hec_satmayan_storelar = [i['total_sales'] for i in stores if not x in i['products']]

    sales = round(Average( x_satan_storelar), -2)
    notsales = round(Average( x_hec_satmayan_storelar), -2)
    print(x, sales, notsales)


def flatten(xss):
    return [x for xs in xss for x in xs]

unique = lambda lst: list(set(lst))

product_list = [i['products'] for i in stores] 
product_list = flatten( product_list )
product_list = unique( product_list )

print(product_list)






product_salesandnotsales = {}

print('=' * 80)
for x in product_list:
    x_satan_storelar = [i['total_sales'] for i in stores if x in i['products']]
    x_hec_satmayan_storelar = [i['total_sales'] for i in stores if not x in i['products']]

    sales = int(round(Average( x_satan_storelar), -2))
    notsales = int(round(Average( x_hec_satmayan_storelar), -2))
    salesandnotsales = (sales, notsales)
    product_salesandnotsales[ x ] = salesandnotsales


print(product_salesandnotsales)