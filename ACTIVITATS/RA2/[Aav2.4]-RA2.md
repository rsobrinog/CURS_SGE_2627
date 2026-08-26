# Activitat 2.4 — Procés d'instal·lació documentat pas a pas

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

Munteu una **instal·lació nova** d'Odoo (una carpeta i un `docker-compose.yml` diferents dels que ja teniu, perquè no interfereixi amb les vostres bases de dades actuals).

Per a **cada pas** del procés, ompliu una fitxa amb aquest format:

* **Pas:**
* **Acció/comanda executada:**
* **Resultat obtingut:**
* **Captura de pantalla:**

Els passos mínims a documentar són:

1. Comprovació dels requisits previs (SO, Docker instal·lat i en marxa).
2. Creació del fitxer `docker-compose.yml` (contenidors `odoo` i `db`).
3. Creació del fitxer `odoo.conf`.
4. Aixecar els contenidors (`docker compose up -d`).
5. Primer accés des del navegador i creació de la base de dades de l'empresa (Master Password i contrasenya de l'usuari `admin`).
6. Instal·lació d'un primer mòdul (p. ex. Contactes).
7. Comprovació que tot funciona: crear un registre de prova (un contacte).
