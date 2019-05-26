#! /usr/bin/env python3

import pandas as pd

df = pd.read_csv('2008.csv', usecols = ['ArrDelay','Origin'] )

print(df[df['Origin'] == 'SFO'][['ArrDelay','Origin']].head(3))

print('Henrique Pontes')

