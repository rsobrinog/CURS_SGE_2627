# Pràctica 4.4 – Informes i panells de control personalitzats

## MÒDUL: Desenvolupament d'aplicacions multiplataforma

RA4: Adapta sistemes ERP-CRM identificant els requeriments d'un supòsit empresarial i utilitzant les eines proporcionades per aquests.

## RECURSOS

 - Teoria RA4

## CONDICIONS DE TREBALL

 - Treball individual.
 - Entregar al Moodle l'enllaç del github.
 - Github:
   - Treballar en el mateix repositori de la **RA1**.
   - Crear una branca (al terminal) de nom **ra4** i ubicar-se a la branca (**git checkout ra4**).
   - Al acabar l'activitat, fusionar la branca **ra4** a la branca **main** del github.    

## AVALUACIÓ

- Activitat avaluable amb **A** (Apte) o **NA** (No Apte).
 - Condicions per a **Apte**:
   - 100% de l'activitat demanada.
   - Entregar l'activitat a la data indicada.
   - Treballar amb branca i l'ús de commits.
 - Entregar en format **.md** (markdown) amb la mateixa nomenclatura que el de l'activitat actual.

## ENUNCIAT
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
