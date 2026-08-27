# Activitat 5.10

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


Activitat teòrica/escrita. No cal Odoo obert, però podeu fer servir el mòdul **AI Chip Manager** (activitat 5.1) com a exemple per respondre.

## 1. Arquitectura MVC d'Odoo

Responeu per escrit:

1. Quines són les tres capes de l'arquitectura d'Odoo i quina responsabilitat té cadascuna?
2. Per al mòdul AI Chip Manager, indiqueu **quin fitxer o quina part del codi** correspon a cada capa (Model, Vista, Controlador).
3. Què és l'ORM i quin paper té entre la capa Model i la base de dades PostgreSQL?

## 2. Recorregut d'una acció d'usuari

Descriviu, pas a pas, què passa internament quan un usuari:

1. Obre el menú "AI Chips" i se li mostra el llistat de xips.
2. Prem "Nou", omple el formulari i fa clic a "Desar".

Per a cada pas, indiqueu quina capa/component intervé (menú/acció, vista, controlador, ORM, base de dades).

## 3. Components d'un mòdul

Feu una taula amb dues columnes: **Component** (manifest, models, views, security, report, static, controllers) i **Responsabilitat**, explicant en una frase què fa cadascun dins l'arquitectura general.

**LLIURAR** un document (mitja pàgina - una pàgina) amb les respostes als tres apartats.
