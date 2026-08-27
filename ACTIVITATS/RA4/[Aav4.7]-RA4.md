# Pràctica 4.7 – Integració amb un altre sistema de gestió empresarial

## MÒDUL: Desenvolupament d'aplicacions multiplataforma

RA4: Adapta sistemes ERP-CRM identificant els requeriments d'un supòsit empresarial i utilitzant les eines proporcionades per aquests.

## RECURSOS

 - Teoria RA4

## CONDICIONS DE TREBALL

 - Treball individual.
 - Entregar al Moodle l'enllaç del github.
 - Github:
   - Treballar en el mateix repositori de la **RA1**.
   - Crear una branca (al terminal) de nom **ra4** i ubicar-se a la branca (**git checkout ra4**).
   - Al acabar l'activitat, fusionar la branca **ra4** a la branca **main** del github.    

## AVALUACIÓ

- Activitat avaluable amb **A** (Apte) o **NA** (No Apte).
 - Condicions per a **Apte**:
   - 100% de l'activitat demanada.
   - Entregar l'activitat a la data indicada.
   - Treballar amb branca i l'ús de commits.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT

## 1. Accés extern via XML-RPC

Amb Odoo en marxa (Docker), escriu un petit script en Python que es connecti a la instància via **XML-RPC** utilitzant la llibreria `xmlrpc.client`.

El script ha de:

* Autenticar-se amb la base de dades, l'usuari i la contrasenya.
* Llegir (`search_read`) els 5 primers productes (`product.template`) mostrant el nom i el preu.
* Crear un nou contacte (`res.partner`) amb nom i correu electrònic.

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra el codi del script i la seva execució (sortida per consola).

## 2. Simulació d'integració amb un sistema extern

Imagina que cal connectar Odoo amb un sistema de facturació extern (o un ecommerce com PrestaShop/WooCommerce). Respon per escrit:

1. Quines dades caldria sincronitzar en cada sentit (Odoo → sistema extern i sistema extern → Odoo).
2. Quin mecanisme faries servir (API REST del sistema extern combinada amb XML-RPC/JSON-RPC d'Odoo, un connector ja existent, fitxers d'intercanvi CSV, etc.) i per què.
3. Amb quina freqüència s'hauria de sincronitzar (temps real, cada hora, diari) i com es gestionarien els conflictes si el mateix registre es modifica als dos sistemes.

**LLIURAR** un document breu (mitja pàgina) amb la resposta a aquests tres punts.
