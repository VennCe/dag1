print ('Start api uitlees applicatie')

import requests

paginaresult =  requests.get('https://catfact.ninja/facts')
print (paginaresult)

feitjes =  paginaresult.json()
print (" Eerste feitje is " + feitjes["data"] [0] ["fact"])


