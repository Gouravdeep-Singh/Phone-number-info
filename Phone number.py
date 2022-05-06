import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter Your no. with +__: ")
phone=phonenumbers.parse(number)

time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")#en is passed as which ever is the company their name should be in english
reg=geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(reg)