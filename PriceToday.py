import requests
from tkinter import *

def get_price():
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    req = req.json()

    dolar_price = req['USDBRL']['bid']
    euro_price = req['EURBRL']['bid']
    btc_price = req['BTCBRL']['bid']

    textf = f"\nDolar Price: R$ {dolar_price}\n\nEuro Price: R$ {euro_price}\n\nBTC Price: R$ {btc_price}\n"

    text_price_result['text'] = textf

window = Tk()
window.title("Price Dolar/Euro/BTC")
window.geometry('300x250')

text_price = Label(window, text="Click in the button to view the price")
text_price.grid(column=0, row=0, padx=50, pady=10)

button = Button(window, text="Search", command=get_price)
button.grid(column=0, row=1, padx=50, pady=10)

text_price_result = Label(window, text='')
text_price_result.grid(column=0, row=3, padx=50, pady=10)

window.mainloop()