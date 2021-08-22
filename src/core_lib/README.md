# Config MongoDB:
- Crear indice para username

FIELDS 
{ "username": "text" }

OPTIONS
{ unique: true, name: "usrnameUniqueIndex" }

- Crear indice para token

FIELDS 
{ "token": "text" }

OPTIONS
{ unique: true, name: "tokenUniqueIndex" }