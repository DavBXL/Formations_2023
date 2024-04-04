"""
Currency Converter
As the name suggests, the project's aim is pretty simple to convert the value of money from one unit to another,
which is from one currency to another. This is one of the perfect beginner Python projects on the list,
and it requires basic coding and Python library knowledge. Like, Forex is one of the free public Python packages for
money conversion or exchange rates. It offers numerous functions, including a list of all exchange rates,
the price of Bitcoin in all currency pairs, the ability to convert amounts to Bitcoins, etc.
"""

from forex_python.converter import CurrencyRates
c = CurrencyRates()
c.get_rates('USD')

amount = int(input("Amount: "))
currency_from = str(input("From: Currency code: "))
currency_to = str(input("To: Currency code: "))

