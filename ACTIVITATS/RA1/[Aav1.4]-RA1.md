# Activitat 1.4 — Verificació dels requisits previs a la instal·lació

## Objectiu

Verificar que el sistema operatiu i el gestor de dades d'un equip compleixen els requisits necessaris abans d'instal·lar un ERP-CRM (Odoo).

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

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
