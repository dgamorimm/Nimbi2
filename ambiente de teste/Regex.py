import re

#1

txt = "The rain in Spain"
#Encontre todos os caracteres minúsculos em ordem alfabética entre "a" e "m":
x = re.findall("[a-m]", txt)
print("1. {}".format(x))

##########################################################################################
#2

txt = "That will be 59 dollars"
#Encontre todos os caracteres de dígitos:
x = re.findall("\d", txt)
print("2. {}".format(x))

##########################################################################################
#3

txt = "hello world"
#Procure uma sequência que comece com "he", seguida de dois (qualquer) caracteres e um "o":
x = re.findall("he..o", txt)
print("3. {}".format(x))

##########################################################################################
#4

txt = "hello world"
#Verifique se a sequência começa com 'hello':
x = re.findall("^hello", txt)
if (x):
  print("4. Sim, a cadeia começa com 'hello'")
else:
  print("4. Sem correspondência")