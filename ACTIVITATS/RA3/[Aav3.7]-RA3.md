# Activitat 3.7 — Verificació del rendiment del sistema ERP-CRM

## MÒDUL: Desenvolupament d'aplicacions multiplataforma

RA3: Realitza operacions de gestió, consulta i anàlisi de la informació seguint les especificacions de disseny i utilitzant les eines proporcionades pels sistemes ERP-CRM.

## RECURSOS

 - Teoria RA3

## CONDICIONS DE TREBALL

 - Treball individual.
 - Entregar al Moodle l'enllaç del github.
 - Github:
   - Treballar en el mateix repositori de la **RA1**.
   - Crear una branca (al terminal) de nom **ra3** i ubicar-se a la branca (**git checkout ra3**).
   - Al acabar l'activitat, fusionar la branca **ra3** a la branca **main** del github.    

## AVALUACIÓ


 - Activitat avaluable amb **A** (Apte) o **NA** (No Apte).
 - Condicions per a **Apte**:
   - 100% de l'activitat demanada.
   - Entregar l'activitat a la data indicada.
   - Treballar amb branca i l'ús de commits.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT

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
