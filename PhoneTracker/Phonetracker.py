import phonenumbers
from phonenumbers import geocoder, carrier, timezone
# enter Person Mobile Number
Number = input("Enter Your Mobile Number With Area Code +... :- ")

mobileNumber = phonenumbers.parse(Number)

#Show Time Zone Of mobileNumber
timezone = timezone.time_zones_for_number(mobileNumber)

#Show Service Provider Name Like vi,jio
serviceProvider = carrier.name_for_number(mobileNumber, "en")

#Show Mobile Phone Location 

mobileLocation = geocoder.description_for_number(mobileNumber, "en")

# Print above All Information On display 

print("\nMobile Number Is :- ", Number)

print("\nCurrent timezone :- ", timezone)

print("\nService Provider :- ", serviceProvider)

print("\nCurrent Location :- ", mobileLocation)