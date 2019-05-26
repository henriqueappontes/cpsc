#! /usr/bin/env python3

import pandas as pd

df = pd.read_csv('2008.csv', usecols = ['Dest'] )

print(df['Dest'].value_counts().head(3))



