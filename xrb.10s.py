#!/usr/bin/env python
# coding=utf-8
#
# <bitbar.title>NANO coin Ticker</bitbar.title>
# <bitbar.version>v1.1</bitbar.version>
# <bitbar.author>dizda</bitbar.author>
# <bitbar.author.github>dizda</bitbar.author.github>
# <bitbar.desc>Displays current NANO stats from Binance and CMC</bitbar.desc>
#
# by dizda

import urllib2
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

req_binance = urllib2.Request('https://api.binance.com/api/v1/ticker/24hr?symbol=NANOBTC', headers={ 'User-Agent': 'Mozilla/5.0' })
req_cmc = urllib2.Request('https://api.coinmarketcap.com/v1/ticker/nano/?convert=BTC', headers={ 'User-Agent': 'Mozilla/5.0' })
binance = urllib2.urlopen(req_binance).read()
cmc = urllib2.urlopen(req_cmc).read()

import json
result_binance = json.loads(binance)
result_cmc = json.loads(cmc)

def flow():
    if result_cmc[0]['percent_change_1h'] > '0':
        print (' %.8f ($%.2f) | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QAyQACAALwzISXAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACkSBTjB+AAAALNJREFUOMvVk70NAjEMhb87WYiGBZAQU7ABNSVSWpZgEEagsJDoKBELUCEKFuBuCKTw0xyQC0lICe5i+/k9/wT+3opUUJQhcAUqa8I5ZQT4tANwioGTCkQZA9vmOQE2oUJFhL0DXBz33RpKUfCLfLTQJMx9IlEWuQr6QB3prGtNS1lwiMvEYo7ekNsKRBkB+y+rH1hDFVOwy7ids+gbVzrsM6CXeYDTF85xroB1ZoHb73ymB5RhJkpZTihGAAAAAElFTkSuQmCC color=#000000'% (float(result_binance['lastPrice']), float(result_cmc[0]['price_usd'])) )
    else:
        print (' %.8f ($%.2f) | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QABACnAADQ9FZaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACQ1FZwK3gAAAMRJREFUOMvNkjEKAjEQRZ+jKNjYKh5AbzCdjVcQj+BFPIKlp7EMeAJrUbASQVCEr80uG9cNbqe/Cgn/5WUI/DqNfBHM+kCzbs+lPUAr2pwBq5qABbB+M8gszkDvS/kOdAG5VBgEM4ApsP0CGLukjxlEoA0wSZR3Lo0qhxhZDIBDAmDA0wsBLD51CZeOwLKivHbprZx6AkAHuEXbD5fawYwywMqAzOKeDTTPvKqcTGZBMLsGs0utn5gADYEHcKp9e9ni//MCDtNCE3qjsIwAAAAASUVORK5CYII= color=#000000'% (float(result_binance['lastPrice']), float(result_cmc[0]['price_usd'])) )

#print (' %.8f | color=#000000'% float(result_binance['lastPrice']))
flow()

print '---'

print ('buy: %.8f | color=blue'% float(result_binance['bidPrice']))
print ('sell: %.8f | color=red'% float(result_binance['askPrice']))

print '---'
print ('vol: %.0f BTC (%s) | color=#000000'% (float(result_cmc[0]['24h_volume_btc']), locale.currency(float(result_cmc[0]['24h_volume_usd']), grouping=True)))
print ('change-24h: %.1f%% | color=#000000'% float(result_cmc[0]['percent_change_24h']))
print '---'

print ('high:   %.8f | color=#000000'% float(result_binance['highPrice']))
print ('low:    %.8f | color=#000000'% float(result_binance['lowPrice']))
print ('price:  $%.2f | color=#000000'% float(result_cmc[0]['price_usd']))
print ('rank:   #%.0f | color=#000000'% float(result_cmc[0]['rank']))

print '---'

print 'Show CoinMarketCap | color=#123def href=https://coinmarketcap.com/currencies/nano/'
print 'Show KuCoin | color=purple href=https://www.kucoin.com/#/trade.pro/XRB-BTC'
print 'Show Binance | color=#ff9933 href=https://www.binance.com/tradeDetail.html?symbol=NANO_BTC'