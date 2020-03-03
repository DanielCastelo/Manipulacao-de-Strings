'''
argumento = "www.bytebank.com/cambio?moedaorigem=real"
#............0123456789   12 15
subString = argumento[5:11]
print(subString)

-----------------------------------------
Função Find - encontra o argumento do caractere passado

argumento = "www.bytebank.com/cambio?moedaorigem=real"
#                        11
index = argumento.find("=") #função find encontra o argumento do caractere passado (nesse caso, o =)
substring = argumento[index + 1:] #usando o index para retornar o indíce que querermos, assim retornaria o "=real", mas soma-se o +1 para pegar o próximo índice, assim retornando apenas "real"
print(substring)
'''

#Função split - transforma uma string em um vetor, recebe um separador como argumento

argumento = "moedaorigem=real"
#                        11
listaargumentos = argumento.split("=") #= é o separador, e vai criar um vetor, com "moedaorigem" e "real" separados
print(listaargumentos)
