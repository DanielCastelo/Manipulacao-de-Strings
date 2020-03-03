class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.UrlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem,moedaDestino = self.ExtrairArgumentos()
        representacaostring2 = "Valor: " + self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representacaostring = "Valor: {}\n Moeda Origem: {}\n Moeda Destino: {}\n ".format(self.extraiValor(), moedaOrigem, moedaDestino)
        return representacaostring

    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url

    @staticmethod
    def UrlEhValida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False
    def ExtrairArgumentos(self):

        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaorigem()

            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        '''
                    # self.url.find(moedadestino) + len(moedadestino, 15) + 1
                    # o 15 foi colocado pois o find, para de procurar após encontrar o caractere, caso nao tivesse o
                    # 15, a busca iaparar após o primeiro =, que é do real, mas colocando o índice 15, a busca começa depois do real
                    # assim ele irá fazer a busca até o final da strinh encontrando o = do dolar
                    '''
        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaorigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialvalor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialvalor:]
        return valor
