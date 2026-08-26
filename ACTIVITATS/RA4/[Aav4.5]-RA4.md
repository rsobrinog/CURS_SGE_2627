# Pràctica 8 – Procediments emmagatzemats de servidor (Server Actions)


## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

## 1. Crear una Server Action manual

1. Anar a `Settings > Technical > Actions > Server Actions`.
2. Crear una nova acció sobre el model `Product Template` de tipus **"Execute Python Code"** que marqui el producte com a fràgil (`record.write({'x_fragile': 'yes'})`) si el seu preu de venda (`list_price`) és superior a 500€.
3. Afegir aquesta acció al menú contextual del formulari de producte (des del menú "⚙" / "Actions").
4. Provar-la sobre un producte amb preu superior a 500€ i comprovar que el camp canvia correctament.

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra el codi Python de l'acció i el resultat sobre el producte.

## 2. Crear una tasca planificada (Scheduled Action / Cron)

1. Anar a `Settings > Technical > Automation > Scheduled Actions`.
2. Crear una tasca planificada que s'executi cada dia i que arxivi (`active = False`) els productes marcats sense moviments recents (o una condició similar simplificada, a definir).
3. Configurar la freqüència d'execució (Interval Number / Interval Unit) i la data de la propera execució.
4. Executar-la manualment (botó "Run Manually") per comprovar-ne el funcionament.

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra la configuració de la tasca planificada i el resultat de la seva execució.
