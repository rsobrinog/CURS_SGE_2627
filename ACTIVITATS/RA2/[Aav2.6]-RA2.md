# Activitat 2.6 — Serveis d'accés al sistema ERP-CRM

## Objectiu

Conèixer i configurar diferents serveis d'accés a un sistema ERP-CRM: accés per xarxa local, usuaris de portal, i entendre què cal per exposar-lo de forma segura a internet.

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

### 1. Accés per xarxa local

Si no ho heu fet ja a l'activitat 2.3, compartiu l'accés a la vostra instal·lació d'Odoo a través de la xarxa local (IP + port, regles de firewall) i comproveu-ho des d'un altre dispositiu.

### 2. Usuari de tipus Portal

1. Creeu un contacte (client) nou.
2. Convertiu-lo en usuari de tipus **Portal** (des de la fitxa del contacte, "Concedir accés al portal" o equivalent).
3. Accediu a Odoo amb aquest usuari (en una finestra privada del navegador) i compareu què pot veure respecte a un usuari intern normal.
4. Expliqueu (3-4 línies) per a quins casos d'ús serveix un usuari de portal.

### 3. Accés extern segur (HTTPS)

Sense necessitat de fer-ho realment, expliqueu per escrit:

1. Per què **no** és recomanable exposar directament el port 8069 d'Odoo a internet tal com està configurat per defecte.
2. Quins elements caldria afegir (proxy invers, certificat SSL/TLS...) per exposar-lo de manera segura amb HTTPS.
3. Quina alternativa hi hauria si no es vol exposar el servidor directament a internet (pista: vegeu la teoria del RA2, apartat de serveis d'accés).

## Com entregar-ho

Captures dels apartats 1 i 2, i les respostes escrites de l'apartat 3.
