# Activitat 3.7 — Verificació del rendiment del sistema ERP-CRM

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

Continuem amb el supòsit de **Ray Ban**.

### 1. Mesurar el temps de resposta d'una consulta

1. Escolliu una operació "pesada" (p. ex. carregar tots els moviments d'estoc, o generar l'informe de l'activitat 3.5 amb totes les línies).
2. Mesureu quant triga a completar-se (amb el cronòmetre, o observant el temps de resposta al navegador).
3. Repetiu la mateixa operació amb un filtre que redueixi el nombre de registres (p. ex. només l'últim mes) i compareu els temps.

### 2. Ús de recursos del servidor

Mentre feu l'operació pesada de l'apartat 1, executeu en un altre terminal:

```
docker stats
```

Anoteu el consum de CPU i memòria dels contenidors `odoo` i `db` durant l'operació.

### 3. Revisió del log

Consulteu el fitxer de log d'Odoo (`/var/log/odoo/odoo-server.log`) i localitzeu-hi qualsevol avís (`WARNING`) o consulta lenta que hi aparegui durant les proves anteriors.

### 4. Proposta de millora

Basant-vos en el que heu observat, proposeu **una millora concreta** de rendiment (p. ex. afegir un filtre per defecte, crear un índex a la base de dades per a un camp molt consultat, paginar els resultats, etc.) i expliqueu per què ajudaria.

## Com entregar-ho

Captures dels temps mesurats, del `docker stats` durant l'operació pesada, del fragment de log rellevant, i la proposta de millora.
