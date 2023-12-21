import datetime
import re

dates = [
    '19.12.2023',
    '21-05-2023',
    '17/1/2023',
    '19 Jan 2023',
]


datetime_formats = [
    "%Y-%m-%d",          # Year-Month-Day
    "%d/%m/%Y",          # Day/Month/Year
    "%m/%d/%Y",          # Month/Day/Year (U.S. format)
    "%Y%m%d",            # YearMonthDay without separators
    "%B %d, %Y",         # Full month name, day, year
    "%d %B %Y",          # Day full month name year
    "%Y-%m-%dT%H:%M:%S", # ISO 8601 format
    "%H:%M:%S",          # Hours:Minutes:Seconds
    "%I:%M %p",          # Hours:Minutes AM/PM
    "%a, %d %b %Y %H:%M:%S" # Abbreviated weekday, Day Abbreviated month Year Hours:Minutes:Seconds
]


swapped_datetime_regexes = {
    r"(\d{4})-(\d{2})-(\d{2})": "%Y-%m-%d",                      
    r"(\d{4})\.(\d{2})\.(\d{2})": "%Y.%m.%d",                      
    r"(\d{2})\.(\d{2})\.(\d{4})": "%d.%m.%Y",
    r"(\d{2})\-(\d{2})\-(\d{4})": "%d-%m-%Y",
    r"(\d{1,2})\/(\d{1,2})\/(\d{4})": "%d/%m/%Y",
    r"(\d{2})/(\d{2})/(\d{4})": "%d/%m/%Y",                      
    r"(\d{2})/(\d{2})/(\d{4})": "%m/%d/%Y",                      
    r"(\d{4})(\d{2})(\d{2})": "%Y%m%d",                          
    r"(\w+) (\d{2}), (\d{4})": "%B %d, %Y",                      
    r"(\d{2}) (\w+) (\d{4})": "%d %b %Y",                        
    r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})": "%Y-%m-%dT%H:%M:%S", 
    r"(\d{2}):(\d{2}):(\d{2})": "%H:%M:%S",                      
    r"(\d{2}):(\d{2}) ([AP]M)": "%I:%M %p",                      
    r"(\w+), (\d{2}) (\w+) (\d{4}) (\d{2}):(\d{2}):(\d{2})": "%a, %d %b %Y %H:%M:%S"
}


def findMatchingDatePattern( given: str ) -> str:
    for r in swapped_datetime_regexes:
        if re.match(r, given):
            return r
    return None



for d in dates:
    matching_regex = findMatchingDatePattern(d)
    matching_format = swapped_datetime_regexes[ matching_regex ]
    parsed_date = datetime.datetime.strptime(d, matching_format)
    print([d, matching_regex, matching_format, parsed_date])


# =============================================================================
print("*" * 80)

colors = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKCYAN': '\033[96m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'BOLD': '\033[1m',
}

import random

ENDC= '\033[0m'

print(colors['OKCYAN'] + "MERHABA" + ENDC + " Ahmet")


s = ""
for i in range(80):
    colorname = random.choice(list(colors.keys()))
    s = s + colors[colorname] + "*" + ENDC

print(s)


possible_dates = [
    "13.13.2023", #! PATLADI, ERROR, ERROR OCCURED, HATA VERDI!!!
    "3.1.2023",  # CONTNUE
    "13.3.2023"
    #* 10.000 dates
]



#* IGNORE !!!
for d in possible_dates:
    try:
        datepattern = "%d.%m.%Y"
        constructed_date = datetime.datetime.strptime( d, datepattern )
        print("constructed_date", constructed_date)
    except Exception as e:
        print("BIR HATA OLUSTU ==>", colors['OKCYAN'] + d + ENDC, colors['FAIL'] + str(e) + ENDC)


print("SELAM")


def checkDateValid( datestring: str, format: str ) -> bool:
    try:
        datetime.datetime.strptime(datestring, format)
        return True
    except:
        return False

for d in possible_dates:
    print(d, checkDateValid(d, "%d.%m.%Y"))

# ========================================================================================
    
import json

#* HOW TO READ A JSON DATA FROM A JSON FILE
JSONDOSYASIOKU = lambda filename: json.load( open(filename, 'r') )

print( JSONDOSYASIOKU('w2.json') )

#! open('w2.json', 'r')   
#! r = read
#! w = write
#! a = append
#! w2.json dosyasinin, "OKUMAK" icin "AÇ"


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


#* HOW TO WRITE A DICTIONARY OR A LIST TO A JSON FILE
with open('w2my.json', 'w') as json_file:
    json.dump(stores, json_file, indent=4)

#* JUMP = EXPORT  


