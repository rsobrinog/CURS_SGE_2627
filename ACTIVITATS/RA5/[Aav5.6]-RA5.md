# Activitat 5.6

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 


# Enunciat

Continuem amb el mòdul **AI Chip Manager** (activitat 5.1, amb els camps `coste` i `fecha_fabricacion` ja afegits a la part 2).

## 1. Camp calculat (processament de dades)

Afegiu un nou camp `antiguitat_dies` (Integer, `compute`) que calculi els dies transcorreguts des de `fecha_fabricacion` fins avui.

* Ha d'utilitzar el decorador `@api.depends('fecha_fabricacion')`.
* Si `fecha_fabricacion` és buit, el valor ha de ser `0`.

Mostreu aquest camp (readonly) al formulari i al llistat.

**ADJUNTAR CAPTURA DE PANTALLA**

Del codi del mètode `compute` i del camp mostrat a un xip amb data de fabricació informada.

## 2. Informe personalitzat (QWeb)

Creeu un informe imprimible en PDF que llisti tots els xips d'un mateix proveïdor, mostrant: nom, personalitat, habilitat, cost i antiguitat en dies.

1. Declareu l'acció d'informe (`ir.actions.report`) al `manifest`.
2. Creeu la plantilla QWeb corresponent dins de `report/`.
3. Genereu el PDF des de la vista de llista de xips (seleccionant-ne uns quants i fent servir Print).

**ADJUNTAR CAPTURA DE PANTALLA**

De l'XML de la plantilla QWeb i del PDF generat.
