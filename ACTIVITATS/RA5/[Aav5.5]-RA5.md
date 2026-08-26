# Activitat 5.5


## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 


# Enunciat

Cybertech vol que comproveu que sabeu treballar amb l'ORM d'Odoo directament en codi, sense passar per la interfície web. Farem servir el mòdul **AI Chip Manager** creat a l'activitat 5.1.

Totes les operacions s'han de fer des de l'**Odoo shell**:

`docker exec -it <contenidor_odoo> odoo shell -d <bbdd>`

## 1. Consulta (Read)

1. Escriviu una comanda que retorni tots els xips del proveïdor `nvidia`.
2. Escriviu una comanda `search_read` que retorni només el nom i la personalitat de tots els xips amb habilitat `programacion`.

## 2. Inserció (Create)

Creeu, per codi (no des de la interfície), tres xips nous amb proveïdor, personalitat i habilitat diferents entre ells.

## 3. Modificació (Write)

1. Modifiqueu, per codi, el proveïdor de tots els xips amb personalitat `analitica` perquè passin a tenir proveïdor `amd`.
2. Comproveu el canvi tornant a fer una consulta.

## 4. Eliminació (Unlink)

1. Afegiu un camp `active` (Boolean, per defecte `True`) al model `ai.chip` si encara no en té.
2. Arxiveu (poseu `active = False`) tots els xips amb habilitat `ventas`, **sense** utilitzar `unlink()`.
3. Expliqueu per escrit (2-3 línies) per què en aquest cas és millor arxivar que fer `unlink()`.

**ADJUNTAR CAPTURA DE PANTALLA**

De cada comanda executada a l'Odoo shell i del resultat obtingut.
