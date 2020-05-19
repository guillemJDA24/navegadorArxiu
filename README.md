# Operacions de S.O sobre fitxers i directoris

![](https://i.imgur.com/REp4oMM.jpg)


En la carpeta fitxers hi ha tot de fitxers. Fareu un programa que faci el següent:

- llisti els arxius del directori fitxers i li demanem a l'usuari quin vol llegir

Un cop l'usuari determini quin fitxer vol fareu:

- mostrar el contingut per pantalla.
- avisar a l'usuari que s'executarà una operació sobre els arxius.

Si l'usuari confirma que vol fer l'operació, executereu l'operació que hi ha escrita en l'arxiu.

Els arxius només contenen una línia on pot haver de dues a tres paraules. A l'estil:
```text=
moure c.txt x1.txt
```

L'operació pot ser:
- **borrar** : s'ha de borrar l'arxiu que diu a continuació
- **copiar** : s'ha de copiar l'arxiu escrit a continuació al nom escrit al final.
- **moure**: s'ha de moure l'arxiu escrit a continuació al nom escrit al final.

Es valora que tingueu en compte errors i els gestioneu. Possibles errors:

- si el fitxer no existeix
- si no es té permisos per llegir o escriure  en el directori que toqui.

I aviseu degudament a l'usuari.

Aquí teniu exemples de com es fan diverses operacions amb els arxius:

## Llistar arxius en un directori 
```python3=
#!/usr/bin/python

import os, sys

# Open a file
path = "/var/www/html/"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file
``` 

## Comprovar arxiu existeix

```python3=
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```
## Borrar arxius
```python3=
import os
os.remove("demofile.txt")
```

## Copiar arxius
```python3=
from shutil import copyfile
copyfile(src, dst)
```

## Moure arxius

```python3=
import os
import shutil

#Qualsevol de les tres maneres serveix
os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
```

