# Activitat 2.7 — Entorns de desenvolupament, proves i explotació

## Objectiu

Practicar la separació d'entorns (desenvolupament, preproducció/proves, producció) en una instal·lació d'Odoo, tal com es descriu a la teoria del RA2.

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat

Partint d'una de les vostres bases de dades d'Odoo ja creades (amb dades):

### 1. Crear els tres entorns

1. Dupliqueu la base de dades des del **Gestor de bases de dades** d'Odoo (Database Manager) per crear-ne dues còpies més, de manera que tingueu:
   * `empresa_PROD` (la base de dades "real")
   * `empresa_PRE` (còpia per a proves abans de passar canvis a producció)
   * `empresa_DEV` (còpia per a desenvolupar/provar mòduls i configuracions noves)

### 2. Provar un canvi a l'entorn de desenvolupament

1. A `empresa_DEV`, instal·leu o configureu alguna cosa nova (un mòdul, un camp personalitzat del RA4/RA5, o un canvi de configuració).
2. Comproveu que funciona correctament **només** en aquest entorn.

### 3. Passar el canvi a preproducció i, finalment, a producció

1. Repetiu el mateix canvi a `empresa_PRE` i verifiqueu-lo de nou (simulant que és l'últim pas abans de producció).
2. Un cop verificat, apliqueu el canvi a `empresa_PROD`.

### 4. Reflexió

Responeu per escrit (4-5 línies): quins avantatges té aquesta manera de treballar (DEV → PRE → PROD) enfront de fer els canvis directament a la base de dades de producció? Poseu un exemple concret de problema que aquesta pràctica evitaria.

## Com entregar-ho

Captura del Database Manager amb les tres bases de dades creades, captures del canvi provat a cada entorn, i la reflexió de l'apartat 4.
