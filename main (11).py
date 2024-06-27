#Enigma 

mapa = {
 "6" : "F",
 "5" : "E",
 "50" : "L",
 "1" : "I",
 "26" : "Z",
 "MM" : "2000",
 "R" : "18"
}

mensagem = '6550126MMR'

letras = ""
i = 0 

while i < len(mensagem):
    if mensagem[i:i+2] in mapa:
        letras += mapa[mensagem[i:i+2]]
        i += 2
    elif mensagem[i] in mapa:
        letras += mapa [mensagem[i]]
        i += 1

print(letras [0:5] + " " + letras [5:7] + letras [7 + 2:])
  