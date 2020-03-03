import re #re é a biblioteca que lida com expressões regulares

email1 = "Meu número é 9848-3865"
email2 = "o em 99848-3865 fale comigesse é meu número"
email3 = "9948-3865 é o meu celulare"
email4 = "afhshfshf 99845-3596 ajfjhfhsd 48579-2585 ahfhafjhdhfj 85595-8957"

#padrao = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
padrao2 = "[0-9]{4,5}[-]*[0-9]{4}"

#retorno = re.search(padrao2,email2) #metodo serch recebe o padrao procurado e onde ele deve buscar a ocorrência
#print(retorno.group())
retorno = re.findall(padrao2,email4) #metodo findall encontra todas as ocorrencias que se encaixam no padrão, diferente do search que para após encontrar a primeira
#findall retorna em forma de lista
print(retorno) #findall nao necessita do group()