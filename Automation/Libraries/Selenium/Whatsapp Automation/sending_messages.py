import pywhatkit

phone_number = input("Enter the phone number: ")

pywhatkit.sendwhatmsg(phone_number, "Hi!", 13, 17, 10, True)