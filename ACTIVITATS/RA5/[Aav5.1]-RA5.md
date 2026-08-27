# Activitat 5.1

## MÒDUL: Desenvolupament d'aplicacions multiplataforma

RA5:  Desenvolupa components per a un sistema ERP-CRM analitzant i utilitzant el llenguatge de programació incorporat.

## RECURSOS

 - Teoria RA5

## CONDICIONS DE TREBALL

 - Treball individual.
 - Entregar al Moodle l'enllaç del github.
 - Github:
   - Treballar en el mateix repositori de la **RA1**.
   - Crear una branca (al terminal) de nom **ra5** i ubicar-se a la branca (**git checkout ra5**).
   - Al acabar l'activitat, fusionar la branca **ra5** a la branca **main** del github.    

## AVALUACIÓ

 - Activitat avaluable amb nota de 0 a 100.
 - Entregar l'activitat a la data indicada.
 - Treballar a la branca **ra5**.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT

# Part 1

Cybertech necessita un mòdul específic que s’encarregui de la configuració dels xips amb característiques humanes.

El mòdul és molt simple, tindrà:

* Un camp per introduir text amb el nom del processador  
* Un camp amb un desplegable amb 3 proveïdors  
* Un camp amb un desplegable amb 5 personalitats  
* Un camp amb un desplegable amb 5 habilitats professionals

**Manifest**
```py
{  
    'name': 'AI Chip Manager',  
    'version': '1.0',  
    'summary': 'Gestión de personalidades y habilidades para chips de IA en androides',  
    'author': 'Franc',  
    'category': 'Custom',  
    'depends': ['base'],  
    'data': [  
        'security/ir.model.access.csv',  
        'views/ai_chip_views.xml',  
    ],  
    'installable': True,  
    'application': True,  
}
```

**Init**

```py
from . import models
```

**Model**

```py
from odoo import models, fields

class AIChip(models.Model):  
    _name = 'ai.chip'  
    _description = 'AI Chip'

    name = fields.Char(string="Nombre del Chip", required=True)

    proveedor = fields.Selection([  
        ('nvidia', 'NVIDIA'),  
        ('amd', 'AMD'),  
        ('intel', 'Intel'),  
    ], string="Proveedor")

    personality = fields.Selection([  
        ('creativa', 'Creativa'),  
        ('analitica', 'Analítica'),  
        ('empatica', 'Empática'),  
        ('directa', 'Directa'),  
        ('visionaria', 'Visionaria'),  
    ], string="Personalidad")

    skill = fields.Selection([  
        ('comunicacion', 'Comunicación'),  
        ('programacion', 'Programación'),  
        ('gestion', 'Gestión'),  
        ('ventas', 'Ventas'),  
        ('analisis', 'Análisis'),  
    ], string="Habilidad")
```

**Init**
```py
from . import ai_chip
```

**Vista**

```xml
<?xml version="1.0" encoding="UTF-8"?\>  
<odoo>
    <!-- ACCIÓN PRINCIPAL -->  
    <record id="action_ai_chip" model="ir.actions.act_window"\>  
        <field name="name">AI Chips</field>  
        <field name="res_model">ai.chip</field>  
        <field name="view_mode">list,form</field>  
    </record>

    <!-- MENÚ RAÍZ -->  
    <menuitem id="menu_ai_chip_root"  
              name="AI Chips"  
              sequence="10"  
              web_icon="base/static/description/icon.png"/>

    <!-- SUBMENÚ -->  
    <menuitem id="menu_ai_chip"  
              name="Gestión de Chips"  
              parent="menu_ai_chip_root"  
              action="action_ai_chip"  
              sequence="20"/>

    <!-- VISTA FORMULARIO -->  
    <record id="view_ai_chip\_form" model="ir.ui.view">  
        <field name="name">ai.chip.form</field>  
        <field name="model">ai.chip</field>  
        <field name="arch" type="xml">  
            <form string\="Chip de IA">  
                <sheet>  
                    <group>  
                        <field name="name"/>  
                        <field name="proveedor"/>  
                        <field name="personality"/>  
                        <field name="skill"/>  
                    </group>  
                </sheet>  
            </form>  
        </field>  
    </record>

    <!-- VISTA LISTA -->  
    <record id="view_ai_chip_list" model="ir.ui.view">  
        <field name="name">ai.chip.list</field>  
        <field name="model">ai.chip</field>  
        <field name="arch" type="xml">  
            <list>  
                <field name="name"/>  
                <field name="proveedor"/>  
                <field name="personality"/>  
                <field name="skill"/>  
            </list>  
        </field>  
    </record>
</odoo>
```


**Security**

```py
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink  
access_ai_chip,access_ai_chip,model_ai_chip,,1,1,1,1
```


# Part 2

Añadir los campos:

`coste` → fields.Float   
`fecha_fabricacion` → fields.Date

Aquí la idea es conectar nuestro módulo a otros ya existentes de Odoo.

`proveedores` → fields.Many2one (Aquí se requerirà acceso a contactos)  
`robots` → fields.Many2one (Aquí se requerirà acceso a productos, inventario)  
