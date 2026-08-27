# Activitat 5.7

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


Cybertech vol que el mòdul **AI Chip Manager** pugui consultar informació d'una font externa mitjançant una llibreria de Python i una crida a una API.

## 1. Crida a una llibreria/API externa des d'un Server Action

1. Afegiu un camp `tipus_canvi_usd` (Float) al model `ai.chip` (representarà el tipus de canvi EUR→USD del dia, per calcular el cost en dòlars).
2. Creeu una **Server Action** de tipus "Execute Python Code" sobre el model `ai.chip` que:
   * Faci una crida amb la llibreria `requests` a una API pública de tipus de canvi (p. ex. `https://api.exchangerate-api.com/v4/latest/EUR`, o una altra similar accessible sense clau).
   * Extregui el valor corresponent a USD de la resposta JSON.
   * Guardi aquest valor al camp `tipus_canvi_usd` del/dels registre/s seleccionat/s.
3. Afegiu aquesta acció al menú contextual del formulari de xip i proveu-la.

**ADJUNTAR CAPTURA DE PANTALLA**

Del codi de la Server Action i del resultat sobre un xip (camp `tipus_canvi_usd` omplert).

## 2. Crida a un altre mòdul/model propi

Des d'un mètode del model `ai.chip`, feu una crida al model `res.partner` per obtenir el nombre total de contactes de tipus empresa (`is_company = True`) i mostreu el resultat en un `log` (vegeu activitat 5.8 per l'ús de `logging`).

```python
partners = self.env['res.partner'].search_count([('is_company', '=', True)])
```

**ADJUNTAR CAPTURA DE PANTALLA**

Del codi i del resultat visible al log del servidor.
