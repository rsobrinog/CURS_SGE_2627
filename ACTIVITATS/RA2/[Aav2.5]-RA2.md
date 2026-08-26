# Activitat 2.5 — Actualització del sistema ERP-CRM

## MÒDUL: Desenvolupament d'aplicacions multiplataforma

RA2: Implanta sistemes ERP-CRM interpretant la documentació tècnica i identificant les diferents opcions i mòduls.

## RECURSOS

 - Teoria RA2

## CONDICIONS DE TREBALL

 - Treball individual.
 - Entregar al Moodle l'enllaç del github.
 - Github:
   - Treballar en el mateix repositori de la **RA1**.
   - Crear una branca (al terminal) de nom **ra2** i ubicar-se a la branca (**git checkout ra2**)
   - Al acabar l'activitat, fusionar la branca **ra2** a la branca **main** del github.    

## AVALUACIÓ

 - Activitat avaluable amb **A** (Apte) o **NA** (No Apte).
 - Condicions per a **Apte**:
   - 100% de l'activitat demanada.
   - Entregar l'activitat a la data indicada.
   - Treballar amb branca i l'ús de commits.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT

Utilitzeu una de les instal·lacions d'Odoo que ja teniu (per exemple, la de l'activitat 2.4).

### 1. Backup previ

1. Feu una còpia de seguretat de la base de dades abans de fer cap canvi, seguint el procediment de `pg_dump` ja vist a la teoria del RA2.

### 2. Actualitzar un mòdul ja instal·lat

1. Feu un petit canvi (per exemple, un camp nou o un canvi de text a una vista) en un mòdul que ja tingueu instal·lat (podeu reutilitzar un mòdul propi del RA5, o bé simular el canvi editant una vista des del Developer Mode com al RA4).
2. Actualitzeu el mòdul des d'**Apps** (botó "Actualitzar" o, en mode desenvolupador, "Actualitzar llista d'aplicacions").
3. Comproveu que el canvi s'ha aplicat correctament.

### 3. Instal·lar un mòdul nou

1. Instal·leu un mòdul que encara no tinguéssiu (p. ex. Projectes, si no el teníeu).
2. Comproveu que no ha trencat cap funcionalitat existent (proveu algun procés que ja funcionava abans, com crear una comanda de venda).

### 4. Reflexió

Responeu per escrit (5-6 línies):

* Quina diferència hi ha entre **actualitzar un mòdul** i **actualitzar la versió d'Odoo** (per exemple, de la versió 17 a la 18)?
* Quins riscos té actualitzar la versió major d'Odoo, i com es podrien mitigar?
