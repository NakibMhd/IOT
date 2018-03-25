#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
import cryptocompare

crypto = ''

print(cryptocompare.get_coin_list(format=False))

while crypto != 'exit':
    crypto = input('De quelle cryptomonnaie souhaitez-vous connaitre le prix ? ')
    print(cryptocompare.get_price(crypto))