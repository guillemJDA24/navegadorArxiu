
import os, sys

# Open a file
path = "fitxers"
dirs = os.listdir( path )
# This would print all the files and directories
for file in dirs:
  print (file)
nom=input('arxiu a obrir: ')
fitxer = open(path+'/'+nom,'r')
fitxerr=fitxer.read()
print (fitxerr.read())
resposta=input('vols executar el contingut del arxiu?')
if resposta == 'si':
  pro = fitxer.read().split(' ')
  print (pro[0])