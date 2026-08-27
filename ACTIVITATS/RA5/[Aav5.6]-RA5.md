# Activitat 5.6

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

- Activitat avaluable amb **A** (Apte) o **NA** (No Apte).
 - Condicions per a **Apte**:
   - 100% de l'activitat demanada.
   - Entregar l'activitat a la data indicada.
   - Treballar amb branca i l'ús de commits.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT 


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
