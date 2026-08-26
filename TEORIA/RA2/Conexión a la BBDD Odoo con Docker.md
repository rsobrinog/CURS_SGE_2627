# **Conexión a la BBDD Odoo con Docker**

## **1\. Comandos en Docker**

* Listar contenedores activos:   
  docker ps  
* Abrir un shell dentro del contenedor de la base de datos:  
  docker exec \-it odoo-docker-test-db-1 bash  
* Sin conectarnos a la base de datos:

  * Listar bases de datos en el contenedor:  
    docker exec \-it odoo-docker-test-db-1 psql \-U odoo \-l  
  * Conectarse al contenedor:

  docker exec \-it odoo-docker-test-db-1 psql \-U odoo \-d mydb


  ## **2\. Comandos básicos en psql (ya dentro del contenedor)**

* Listar todas las bases de datos disponibles desde el shell del contenedor:   
  psql \-U odoo \-l  
  Esto muestra todas las bases de datos. Ejemplos típicos: `postgres`, `template0`, `template1`, y la base de datos real de Odoo (por ejemplo `mydb`, `odoo`, `odoo19`).  
* Conectarse a la base de datos correcta:  
  psql \-U odoo \-d nombre\_de\_la\_base

Ejemplo: psql \-U odoo \-d mydb

* Salir del cliente psql:  
   \\q  
* Reiniciar el buffer de consulta si el prompt cambia a `mydb-#`:  
   \\r  
* Ver en qué base de datos estás conectado:   
  SELECT current\_database();


  ## **3\. Exploración de la base de datos**

* Listar todas las tablas del esquema actual:   
  \\dt  
* Listar tablas de todos los esquemas:   
  \\dt *.*  
* Ver la estructura de una tabla concreta:   
  \\d res\_partner


  ## **4\. Consultas SQL útiles**

* Ver algunos registros de la tabla res\_partner:   
  SELECT id, name, email, is\_company, customer\_rank FROM res\_partner LIMIT 10;  
* Ver algunos registros de la tabla res\_partner:   
  `select id, name, description, description_sale, categ_id, list_price, volume, weight, company_id from produt_tmplate order by id;`;


  ## **5\. Tips**

* `docker exec … psql` → entrar a la base de datos correcta  
* `\dt` → listar tablas  
* `\d nombre_tabla` → ver estructura  
* `SELECT …` → consultar registros  
* `\q` y `\r` → salir o reiniciar cuando el prompt cambia a `-#`

