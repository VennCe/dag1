print('start met csv uitlees applicatie')

import pandas

#library - Dependency - Packages
df = pandas.read_csv('pokemon.csv')
print(df["Name"])


for r,rij in df.interrows ():
    print (rij["Name"])
    print 
