# Activitat 2.5 — Actualització del sistema ERP-CRM

## Objectiu

Practicar el procés d'actualització de mòduls d'Odoo, seguint les bones pràctiques (backup previ, entorn de proves).

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

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

## Com entregar-ho

Captures del backup, de l'actualització del mòdul (abans/després del canvi) i de la instal·lació del mòdul nou, més la resposta escrita de l'apartat 4.
