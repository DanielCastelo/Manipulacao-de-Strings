from ExtratorArgumentos import ExtratorArgumentosUrl
'''
meuNome = "Daniel"
#..........0123456 - Cada letra tem um índice, em uma palavra, a primeira letra tem índice 0, a segunda, indice 1, e assim por diante

subString = meuNome[4] #acessando a letra do índice(index) 4, no caso, a letra e.
print("Substring letra: " + subString)

subString2 = meuNome[2:5] #os dois pontos : indicam intervalo/fatiamento, acessando os trechos entre 2 e 5, ou seja, vai acessar os indices 2,3 e 4, pois o 5, é onde ele finaliza e para de acessar.
print("Substring trecho/fatia: " + subString2)

sobreMim = "Sobre mim: Meu nome é Daniel e minha idade é 23 anos"
subString3 = sobreMim[45:] #aqui pegamos o "23 anos", como não há final no intervalo, o python vai acessar todos os índices que estão depois do 45.
print("Substring frase: " + subString3)

print(sobreMim)

----------------------------------------------------------
colocar url aqui quando comenta-la
 ----------------------------------------------------
teste = "moedadestino"
index = len(teste) #len é uma função do python que retorna o tamanho de uma string
#substring = url[index:]
print(index)


#url = "moedaorigem=real&moedadestino=dolar"
url = "https://bytebank.com/cambio?moedaoriGem=moedadestino&moedadestino=dolar&valor=1500"
#                find
argumentosUrl = ExtratorArgumentosUrl(url) #extrator de argumentos recebe a url como parametro
moedaOrigem, moedaDestino = argumentosUrl.ExtrairArgumentos() #ExtrairArgumentos é a classe que está sendo acessada pelo argumentosUrl
valor = argumentosUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)


urlByteBank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com.br"
url3 = "https://bytebank.com/cambio/teste/teste" # se o retorno do find abaixo for 0, então essa url é confiáveç contra invasoes.

print(url3.find(urlByteBank))

'''

#index = url.find("moedadestino") + len("moedadestino") +1 #len é uma função do python que retorna o tamanho de uma string
#substring = url[index:]
#print(substring)

#string = "byte bank byte byte "
#stringnova = string.replace("byte", "Daniel", 1)
#função replace substitui o primeiro valor da string que ele recebeu (byte), pelo segundo valor que ele recebeu  (daniel),
# o numero é a quantidade de substituições que ele fará, caso nao haja número, todos serão substituídos.
#print(stringnova)

url = "https://bytebank.com/cambio?moedaorigem=real&moedasdestino=dolar&valor=700"


argumentosUrl = ExtratorArgumentosUrl(url) #extrator de argumentos recebe a url como parametro
moedaOrigem, moedaDestino = argumentosUrl.ExtrairArgumentos() #ExtrairArgumentos é a classe que está sendo acessada pelo argumentosUrl
valor = argumentosUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)

# aqui vamos comparar instancias:

url2 = "https://bytebank.com/cambio?moedaorigem=real&moedasdestino=dolar&valor=1700"


#argumentosUrl = ExtratorArgumentosUrl(url)
#argumentosUrl2 = ExtratorArgumentosUrl(url2)
#print(id(argumentosUrl))
#print(id(argumentosUrl2))
#print(argumentosUrl==argumentosUrl2)