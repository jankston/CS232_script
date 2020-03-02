import PySimpleGUI as sg      
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas

plt.rcParams['figure.figsize'] = (15.0, 7.0)

'''
If the following error message is received then the daily API request limit has been reached...I think:
"Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY."
'''

AVkey = 'KP0ZNVW9NVIN2CKB'

#aesthetics
sg.theme('SystemDefault')
plt.style.use('fivethirtyeight')

# pysimplegui layout
layout = [[sg.Text('Enter a stock symbol (eg. TSLA, MSFT, etc)',)],
         [sg.InputText()],     
         [sg.Submit('Plot'), sg.Cancel()]]     

window = sg.Window('Intraday Stock Graph', layout)    

event, values = window.read()    
window.close()

text_input = values[0]

ts = TimeSeries(key=AVkey, output_format='pandas')
data, meta_data = ts.get_intraday(symbol=text_input, interval='1min', outputsize='full')

plt.ylabel('Price per share ($)')
data['4. close'].plot()
plt.title('Intraday Times Series for the ' + text_input + ' security')
plt.show()