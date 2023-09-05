print('start van de craping applicatie')

from bs4 import BeautifulSoup
import requests

pagina = requests.get ('https://www.bitcoinmeester.nl/')

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')
tabel =  heeldehtml.find('div')
#print(tabel.prettify ())

bitcoinnprijs= heeldehtml.find(id="price1")
print ('Prijs van de bitcoin = ' + bitcoinnprijs)