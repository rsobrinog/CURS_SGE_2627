# Activitat 1.4 — Verificació dels requisits previs a la instal·lació

## MÒDUL: Desenvolupament d'aplicacions multiplataforma

RA1: Identifica sistemes de planificació de recursos empresarials i de gestió de relacions amb clients (ERP-CRM) reconeixent-ne les característiques i verificant la configuració del sistema informàtic. 

## RECURSOS

 - Teoria RA1

## CONDICIONS DE TREBALL

 - Treball individual
 - Entregar al Moodle l'enllaç del github
 - Github:
   - Continuar amb el repositori de l'activitat **Aav1.3**.
   - Treballar a la branca **ra1**.
   - Al acabar l'activitat, fusionar la branca **ra1** a la branca **main** del github.    

## AVALUACIÓ

 - Activitat avaluable amb **A** (Apte) o **NA** (No Apte).
 - Condicions per a **Apte**:
   - 100% de l'activitat demanada.
   - Treballar amb branca i l'ús de commits.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT

Al vostre ordinador (o a una màquina virtual / contenidor que tingueu preparat), comproveu i anoteu la informació següent:

1. **Sistema operatiu i versió**
   `cat /etc/os-release` (Linux) o l'equivalent al vostre sistema.

2. **Versió de Python instal·lada**
   `python3 --version`

3. **PostgreSQL instal·lat i versió** (si no hi és, indiqueu-ho)
   `psql --version`

4. **Espai lliure en disc**
   `df -h`

5. **Disponibilitat dels ports que farà servir Odoo**
   * Port `5432` (PostgreSQL): `sudo lsof -i :5432` (o `netstat -ano | findstr 5432` a Windows)
   * Port `8069` (Odoo): `sudo lsof -i :8069` (o equivalent)

### Checklist

Ompliu aquesta taula amb els 5 punts anteriors:

| Requisit | Valor obtingut | Compleix (Sí/No) |
| :---- | :---- | :---- |
| Sistema operatiu | | |
| Versió de Python | | |
| PostgreSQL instal·lat/versió | | |
| Espai lliure en disc | | |
| Port 5432 lliure | | |
| Port 8069 lliure | | |

Si algun requisit **no** es compleix, indiqueu quina acció caldria fer per solucionar-ho (sense necessitat d'arribar a instal·lar-ho encara).

## Com entregar-ho

Captura de pantalla de cada comanda executada i la checklist omplerta.
