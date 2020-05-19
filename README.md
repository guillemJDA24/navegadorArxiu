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
