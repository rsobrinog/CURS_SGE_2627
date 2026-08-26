# Activitat 3.3 — Definició de camps i consultes d'accés a dades

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

Continuem amb el supòsit de **Ray Ban** (activitats 3.1/3.2): magatzems de Madrid i Barcelona, components, fabricació d'ulleres de sol i clients.

## 1. Definició de camps

1. Afegiu un camp nou `x_lot_fabricacio` (Char) al producte "Ulleres de sol", per identificar el lot de fabricació.
2. Afegiu un camp `x_magatzem_origen` (Selection: Madrid/Barcelona) als components (Vidres, Muntura).

**ADJUNTAR CAPTURA DE PANTALLA** dels camps creats i visibles al formulari de producte.

## 2. Consultes d'accés a dades (filtres i agrupacions)

1. A la vista de moviments d'estoc (Inventari > Informació > Moviments), creeu un **filtre personalitzat** que mostri només els moviments del magatzem de Barcelona dels últims 30 dies.
2. **Agrupeu** aquest llistat per producte.
3. A la vista de productes, creeu un filtre que mostri només els productes amb l'estoc actual **per sota** del mínim establert.

**ADJUNTAR CAPTURA DE PANTALLA** de cada filtre/agrupació configurat i del resultat.

## 3. Consulta directa (Odoo shell o SQL)

1. Des de l'Odoo shell (o amb una consulta SQL via `psql`), obteniu el **total d'unitats fabricades** al magatzem de Barcelona.
2. Obteniu la llista de components amb estoc per sota del mínim, ordenada de menor a major estoc.

**ADJUNTAR CAPTURA DE PANTALLA** de les comandes executades i el resultat.
