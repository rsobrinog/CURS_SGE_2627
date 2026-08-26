# Activitat 5.7

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

# Enunciat

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
