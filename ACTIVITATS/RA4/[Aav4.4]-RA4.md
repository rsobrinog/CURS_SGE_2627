# Pràctica 7 – Informes i panells de control personalitzats

## Avaluació

Aquesta activitat s'avalua amb APTE / NO APTE. 

## Enunciat
## Part 1: Informe personalitzat

1. Activar Developer Mode (si no ho està).
2. Anar a `Settings > Technical > Reporting > Reports` i localitzar l'informe **"Quotation / Order"** (pressupost/comanda de venda).
3. **Duplicar-lo** (per no modificar ni perdre l'informe original) i editar la plantilla QWeb associada.
4. Afegir una línia nova dins de la taula de línies de comanda amb el camp `x_material` del producte:
   `<span t-field="line.product_id.x_material"/>`
5. Generar el PDF d'una comanda de venda per comprovar el resultat.

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra la plantilla QWeb modificada i el PDF resultant.

## Part 2: Panell de control (Dashboard)

1. Anar al mòdul **Vendes** i obrir la vista **Pivot** de comandes de venda.
2. Configurar-la per mostrar el total facturat agrupat per client i per mes.
3. Canviar a vista **Gràfic** (Graph) i triar el tipus de gràfic més adequat (barres, línia o pastís).
4. Si es disposa del mòdul **Dashboards/Spreadsheet**, afegir aquest gràfic a un tauler nou anomenat "Vendes - Resum".
5. Afegir, com a mínim, dos indicadors (KPI) més al tauler (p. ex. nombre de comandes del mes, ticket mitjà).

**ADJUNTAR CAPTURA DE PANTALLA**

Mostra el panell de control final amb els indicadors i el gràfic.
