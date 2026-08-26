# Pràctica 6 – Consultes i processos automatitzats


## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

Es continua treballant sobre Odoo en **Developer Mode**, sobre la mateixa base de dades utilitzada a la Pràctica 4 (camp `x_material` ja creat).

## 1. Adaptar una vista de cerca (search view)

1. Anar a `Inventory > Products > Products`.
2. Des del menú "Bug", editar la **Search View** del llistat de productes (`Edit View: Search`).
3. Afegir un filtre nou basat en el camp `x_material`:
   `<filter name="amb_material" string="Amb material" domain="[('x_material','!=',False)]"/>`
4. Afegir una opció d'agrupar per (`group by`) pel mateix camp.
5. Comprovar el filtre i l'agrupació al llistat de productes.

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra l'XML de la vista de cerca i el resultat de filtrar/agrupar al llistat.

## 2. Consultes amb domini (ORM)

Des de l'Odoo shell (`docker exec -it <contenidor_odoo> odoo shell -d <bbdd>` o equivalent), executa consultes per obtenir:

* Els productes amb `x_material` buit:
  `env['product.template'].search([('x_material','=',False)])`
* Els contactes (`res.partner`) creats en els últims 30 dies:
  `env['res.partner'].search([('create_date','>=', (datetime.today()-timedelta(days=30)))])`

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra les comandes executades i el resultat obtingut.

## 3. Consulta SQL directa

Des de `psql` (dins del contenidor de PostgreSQL), escriu una consulta SQL que retorni el nom i el preu dels productes amb el camp `x_material` informat:

`SELECT name, list_price, x_material FROM product_template WHERE x_material IS NOT NULL;`

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra la consulta i el resultat.

## 4. Automatitzar un procés (Automated Action)

1. Activar les accions automatitzades: `Settings > Technical > Automation > Automated Actions`.
2. Crear una automatització sobre el model `Product Template` que, quan es creï un producte sense el camp `x_material` informat, li assigni automàticament el valor `"No especificat"`.
3. Configurar el disparador (**Trigger**) com "On Creation" i afegir l'acció d'actualitzar el camp.
4. Comprovar-ho creant un producte nou sense omplir aquest camp.

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra la configuració de l'acció automatitzada i la comprovació feta sobre el producte creat.
