from shutil import copyfile

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
print (fitxerr)
resposta=input('vols executar el contingut del arxiu? ')
if resposta == 'si':
  pro = fitxerr.split(' ')
  if pro[0]=='moure':
    if os.path.exists(path+'/'+pro[1]):
      os.replace(path+'/'+pro[1] , path+'/'+pro[2])
    else:
      print('no existeix')
      
      
  elif pro[0]=='borrar':
    os.remove(path+'/'+pro[1])
  elif pro[0]=='copiar':
    copyfile(src, dst)