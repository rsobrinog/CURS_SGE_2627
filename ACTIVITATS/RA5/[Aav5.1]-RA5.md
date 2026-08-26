# Activitat 5.1

# Part 1

Cybertech necessita un mòdul específic que s’encarregui de la configuració dels xips amb característiques humanes.

El mòdul és molt simple, tindrà:

* Un camp per introduir text amb el nom del processador  
* Un camp amb un desplegable amb 3 proveïdors  
* Un camp amb un desplegable amb 5 personalitats  
* Un camp amb un desplegable amb 5 habilitats professionals

**Manifest**

{  
    'name': 'AI Chip Manager',  
    'version': '1.0',  
    'summary': 'Gestión de personalidades y habilidades para chips de IA en androides',  
    'author': 'Franc',  
    'category': 'Custom',  
    'depends': \['base'\],  
    'data': \[  
        'security/ir.model.access.csv',  
        'views/ai\_chip\_views.xml',  
    \],  
    'installable': True,  
    'application': True,  
}

**Init**

from . import models

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

**Model**

from odoo import models, fields

class AIChip(models.Model):  
    \_name \= 'ai.chip'  
    \_description \= 'AI Chip'

    name \= fields.Char(string\="Nombre del Chip", required\=True)

    proveedor \= fields.Selection(\[  
        ('nvidia', 'NVIDIA'),  
        ('amd', 'AMD'),  
        ('intel', 'Intel'),  
    \], string\="Proveedor")

    personality \= fields.Selection(\[  
        ('creativa', 'Creativa'),  
        ('analitica', 'Analítica'),  
        ('empatica', 'Empática'),  
        ('directa', 'Directa'),  
        ('visionaria', 'Visionaria'),  
    \], string\="Personalidad")

    skill \= fields.Selection(\[  
        ('comunicacion', 'Comunicación'),  
        ('programacion', 'Programación'),  
        ('gestion', 'Gestión'),  
        ('ventas', 'Ventas'),  
        ('analisis', 'Análisis'),  
    \], string\="Habilidad")

**Init**

from . import ai\_chip

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

**Vista**

\<?xml version\="1.0" encoding\="UTF-8"?\>  
\<odoo\>

    \<\!-- ACCIÓN PRINCIPAL \--\>  
    \<record id\="action\_ai\_chip" model\="ir.actions.act\_window"\>  
        \<field name\="name"\>AI Chips\</field\>  
        \<field name\="res\_model"\>ai.chip\</field\>  
        \<field name\="view\_mode"\>list,form\</field\>  
    \</record\>

    \<\!-- MENÚ RAÍZ \--\>  
    \<menuitem id\="menu\_ai\_chip\_root"  
              name\="AI Chips"  
              sequence\="10"  
              web\_icon\="base/static/description/icon.png"/\>

    \<\!-- SUBMENÚ \--\>  
    \<menuitem id\="menu\_ai\_chip"  
              name\="Gestión de Chips"  
              parent\="menu\_ai\_chip\_root"  
              action\="action\_ai\_chip"  
              sequence\="20"/\>

    \<\!-- VISTA FORMULARIO \--\>  
    \<record id\="view\_ai\_chip\_form" model\="ir.ui.view"\>  
        \<field name\="name"\>ai.chip.form\</field\>  
        \<field name\="model"\>ai.chip\</field\>  
        \<field name\="arch" type\="xml"\>  
            \<form string\="Chip de IA"\>  
                \<sheet\>  
                    \<group\>  
                        \<field name\="name"/\>  
                        \<field name\="proveedor"/\>  
                        \<field name\="personality"/\>  
                        \<field name\="skill"/\>  
                    \</group\>  
                \</sheet\>  
            \</form\>  
        \</field\>  
    \</record\>

    \<\!-- VISTA LISTA \--\>  
    \<record id\="view\_ai\_chip\_list" model\="ir.ui.view"\>  
        \<field name\="name"\>ai.chip.list\</field\>  
        \<field name\="model"\>ai.chip\</field\>  
        \<field name\="arch" type\="xml"\>  
            \<list\>  
                \<field name\="name"/\>  
                \<field name\="proveedor"/\>  
                \<field name\="personality"/\>  
                \<field name\="skill"/\>  
            \</list\>  
        \</field\>  
    \</record\>

\</odoo\>

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

**Security**

id,name,model\_id:id,group\_id:id,perm\_read,perm\_write,perm\_create,perm\_unlink  
access\_ai\_chip,access\_ai\_chip,model\_ai\_chip,,1,1,1,1

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

# Part 2

Añadir los campos:

`coste` → fields.Float   
`fecha_fabricacion` → fields.Date

Aquí la idea es conectar nuestro módulo a otros ya existentes de Odoo.

`proveedores` → fields.Many2one (Aquí se requerirà acceso a contactos)  
`robots` → fields.Many2one (Aquí se requerirà acceso a productos, inventario)  
