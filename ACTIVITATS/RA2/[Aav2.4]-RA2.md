# Activitat 2.4 — Procés d'instal·lació documentat pas a pas

## Objectiu

Instal·lar un ERP-CRM (Odoo) des de zero, documentant cada pas del procés d'instal·lació.

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

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

## Com entregar-ho

Un document amb les 7 fitxes (o més, si voleu detallar-ho més) completades amb les captures corresponents.
