# Activitat 5.5

## MÒDUL: Desenvolupament d'aplicacions multiplataforma

RA5:  Desenvolupa components per a un sistema ERP-CRM analitzant i utilitzant el llenguatge de programació incorporat.

## RECURSOS

 - Teoria RA5

## CONDICIONS DE TREBALL

 - Treball individual.
 - Entregar al Moodle l'enllaç del github.
 - Github:
   - Treballar en el mateix repositori de la **RA1**.
   - Crear una branca (al terminal) de nom **ra5** i ubicar-se a la branca (**git checkout ra5**).
   - Al acabar l'activitat, fusionar la branca **ra5** a la branca **main** del github.    

## AVALUACIÓ

- Activitat avaluable amb **A** (Apte) o **NA** (No Apte).
 - Condicions per a **Apte**:
   - 100% de l'activitat demanada.
   - Entregar l'activitat a la data indicada.
   - Treballar amb branca i l'ús de commits.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT 

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
