## **Instal·lació Odoo amb Docker en Linux**

### **1\. Preparación del entorno**

Actualizar paquetes:

**sudo apt update && sudo apt upgrade \-y**

Instalar Docker y Docker Compose:

**sudo apt install docker.io docker-compose \-y**  
**sudo systemctl enable docker**  
**sudo systemctl start docker**

### **2\. Crear directorios de trabajo**

Carpeta principal para Odoo:

**mkdir \~/odoo-docker && cd \~/odoo-docker**

### **3\. Configurar `docker-compose.yml`**

Dentro de la carpeta de Odoo crear el archivo docker-compose.yml

| services:   odoo:     image: odoo:19     depends\_on:       \- db     ports:       \- "8069:8069"     environment:       \- HOST=db       \- USER=odoo       \- PASSWORD=odoo   db:     image: postgres:15     environment:       \- POSTGRES\_USER=odoo       \- POSTGRES\_PASSWORD=odoo       \- POSTGRES\_DB=postgres     volumes:       \- odoo-db-data:/var/lib/postgresql/data volumes:   odoo-db-data: |
| :---- |

### **4\. Levantar los contenedores**

Ejecutar:

**docker compose up \-d**

Verificar que los contenedores estén corriendo:

**docker ps**

### **5\. Acceder a Odoo**

Abrir navegador en:

**http://localhost:8069**

Configurar la base de datos inicial usando **admin** para las contraseñas y **mydb** como nombre de la base de datos y comenzar a usar Odoo.

