# First I use terminal to download 'forex-python' package
# Import all necesarry libraries

from forex_python.converter import CurrencyRates

#Create objects.
# I used the input function to allow user to input there answer. I used the int function to input dollar amount as integer. 

c = CurrencyRates()
amount = int(input("Enter the amount: "))
from_currency = input("From Currency: ")
to_currency = input("To currency: ")

# Use variables to execute code

print(from_currency, "To", to_currency,amount)
result = c.convert(from_currency, to_currency, amount)
print(result)
