import requests
import itertools
class Dicionario:
    def __init__(self,totalNames,maxNumbers):
        self.urlBase = 'https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking'
        if totalNames:
            self.totalNames = int(totalNames)
        else:
            self.totalNames = 1000

        if maxNumbers:
            self.maxNumbers = int(maxNumbers)
        else:
             self.maxNumbers = 4
        
    def getNames(self):
        url = f"{self.urlBase}?qtd={self.totalNames}"
        return requests.get(url)
    
    def generateHashs(self):
        hashs=[]
        names = self.getNames().json()
        number = '1234567890'
        num = [''.join(p) for p in itertools.product(number, repeat=self.maxNumbers)]
        for name in names:
            for n in num:
                hashs.append((f"{name['nome'][0].upper()}{name['nome'][1:].lower()}{n}"))
        return hashs 

if __name__ == "__main__":
    d = Dicionario(100,4)
    hashs = d.generateHashs()
    file= open("dict.txt","w+")
    for hash in hashs:
        file.write(f"{hash}\n")
    file.close()
