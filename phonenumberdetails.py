import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
#phoneNumber = phonenumbers.parse("+9779848429695")

#print(phoneNumber)

###############region
#phoneNumber = phonenumbers.parse("+9779848429695")
#timeZone = timezone.time_zones_for_number(phoneNumber)

#print(timeZone)


####################extract phonenumber
#text = "My contact number is 9848438498, 9848343434 and 9876543210"

#numbers = phonenumbers.PhoneNumberMatcher(text, "IN")

#for i in numbers:
 #   print(i)

#############Carier and region
phoneNumber = phonenumbers.parse("+977988429695")


# Getting carrier of a phone number
#Carrier = carrier.name_for_number(phoneNumber, 'en')
  
# Getting region information
#Region = geocoder.description_for_number(phoneNumber, 'en')

#print(Carrier)
#print(Region)

valid = phonenumbers.is_valid_number(phoneNumber)
  
# Checking possibility of a number
possible = phonenumbers.is_possible_number(phoneNumber)
  
# Printing the output
print(valid)
print(possible)
