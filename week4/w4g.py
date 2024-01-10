
import redis

#* SERVER , IP = '91.102.161.166'

MEMORYDATABASE = redis.Redis('91.102.161.166')

"""
MEMORYDATABASE.set('EmreYazici', 'My name is Emre')
MEMORYDATABASE.set('c001', 'Burak Yildiz')
MEMORYDATABASE.set('c002', 'Ahmet Kaya')
"""

# Standard deviation, ...
#print(MEMORYDATABASE.get('EmreYazici').decode())

for key in MEMORYDATABASE.scan_iter("*"):
    key = key.decode()
    if key not in ['MI_MD5']:
        try:
            print(str(key) + "----->" +  str(MEMORYDATABASE.get(key).decode()))
        except Exception as e:
            print("ERROR", key, e)











