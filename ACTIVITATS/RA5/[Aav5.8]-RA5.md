# Activitat 5.8

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

# Enunciat

Cybertech ha detectat que un company ha deixat un mètode amb errors al mòdul **AI Chip Manager**. Cal depurar-lo i afegir un tractament d'errors correcte.

## 1. Reproduir i localitzar l'error

Afegiu temporalment aquest mètode (amb errors intencionats) al model `ai.chip` i crideu-lo des d'un botó del formulari:

```python
def action_calcular_cost_unitari(self):
    unitats = self.unitats_fabricades  # camp que NO existeix al model
    cost_unitari = self.coste / unitats
    return cost_unitari
```

1. Executeu-lo i **localitzeu l'error exacte** al fitxer de log (`/var/log/odoo/odoo-server.log`).
2. Anoteu quin tipus d'excepció de Python es produeix i per què.

**ADJUNTAR CAPTURA DE PANTALLA**

De l'error mostrat al navegador i del missatge corresponent al log.

## 2. Corregir amb tractament d'errors

Reescriviu el mètode perquè:

* Faci servir un camp que sí existeix (o creeu-ne un de nou `unitats_fabricades` de tipus Integer).
* Controli la divisió per zero amb `try/except`, mostrant un `UserError` clar si `unitats_fabricades` és `0`.
* Deixi constància amb `logging` de cada càlcul realitzat (info) i de cada error controlat (warning).

```python
import logging
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

def action_calcular_cost_unitari(self):
    for record in self:
        try:
            cost_unitari = record.coste / record.unitats_fabricades
            _logger.info("Cost unitari calculat per %s: %s", record.name, cost_unitari)
        except ZeroDivisionError:
            _logger.warning("Unitats fabricades a 0 pel xip %s", record.name)
            raise UserError("Cal indicar les unitats fabricades abans de calcular el cost unitari.")
    return True
```

**ADJUNTAR CAPTURA DE PANTALLA**

Del codi corregit, del missatge d'error controlat (`UserError`) quan unitats és 0, i del resultat correcte quan unitats és més gran que 0.

## 3. Validació amb `@api.constrains`

Afegiu una restricció perquè el camp `coste` no pugui ser negatiu, llançant una `ValidationError` si ho és.

**ADJUNTAR CAPTURA DE PANTALLA**

De l'error mostrat en intentar desar un cost negatiu.
