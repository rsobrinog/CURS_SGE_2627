# Adaptació de sistemes ERP-CRM

# Tipus d’empresa i necessitats de l’empresa

Abans d’adaptar un ERP-CRM cal fer una anàlisi prèvia de dos aspectes:

* **Tipus d’empresa:** sector d’activitat, mida, model de negoci (vegeu la classificació d’empreses del RA1).  
* **Necessitats concretes:** quins processos vol digitalitzar l’empresa, quins departaments necessiten suport i quina informació necessiten consultar o generar.

**Exemples:**

* Un **taller mecànic** necessita gestionar ordres de reparació, peces de recanvi i pressupostos.  
* Una **botiga online** necessita catàleg de productes amb variants, gestió d’estoc i comandes web.  
* Una **consultoria** necessita gestionar projectes, hores imputades i facturació per hores.

El resultat d’aquesta anàlisi sol ser un document de requeriments que servirà de base per decidir quins mòduls activar i quines adaptacions caldrà fer.

# Selecció dels mòduls del sistema ERP-CRM

Un cop identificades les necessitats, cal seleccionar els mòduls de l’ERP-CRM (Odoo) que les cobreixen:

* **Vendes, Compres, Inventari:** gestió comercial i logística bàsica.  
* **Fabricació (MRP):** empreses que produeixen béns.  
* **Projectes:** empreses de serveis que factura per hores o fites.  
* **Comptabilitat i finances:** obligatori per a la majoria d’empreses.  
* **CRM:** gestió comercial i d’oportunitats de venda.  
* **RRHH:** gestió d’empleats, nòmines, assistència.  
* **TPV (Point of Sale):** venda directa al públic.

**Criteris de selecció:**

* Cobertura real de la necessitat identificada.  
* Dependències entre mòduls (vegeu RA2: un mòdul de vendes depèn de productes i contactes).  
* Cost de les llicències (en el cas de mòduls Enterprise).  
* Complexitat d’implantació i formació necessària per als usuaris.

No cal activar mòduls que no aporten valor a l’empresa: cada mòdul actiu suposa més complexitat, més manteniment i, en el cas d’Odoo Enterprise, més cost.

# Possibilitats d’adaptació d’un ERP-CRM

Un ERP-CRM com Odoo es pot adaptar a diferents nivells, de menys a més tècnic:

1. **Configuració (Settings):** paràmetres i opcions dels mòduls, sense necessitat de programar.  
2. **Adaptació sense codi (no-code):** eines com **Odoo Studio**, que permeten crear camps, vistes, automatismes, informes i dashboards de forma visual.  
3. **Adaptació amb Developer Mode:** accés directe a la definició tècnica de camps, vistes i accions (edició d’XML), com es va veure a la pràctica de creació de camps personalitzats.  
4. **Desenvolupament de mòduls propis:** codi Python i XML per a funcionalitats a mida que no es poden aconseguir amb les eines anteriors.  
5. **Integració amb sistemes externs:** connectar l’ERP-CRM amb altres aplicacions mitjançant APIs.

Com més amunt es puja en aquesta llista, més potent és l’adaptació però també més coneixement tècnic i manteniment requereix.

# Taules i vistes que cal adaptar

* **Taules (models):** cada entitat de negoci d’Odoo és un model (`product.template`, `res.partner`, `sale.order`...), que correspon a una taula de la base de dades PostgreSQL.  
* **Tipus de vistes principals:**  
  * **Formulari (form):** entrada i edició d’un registre.  
  * **Llista/arbre (list/tree):** llistat de registres.  
  * **Kanban:** targetes visuals, útil per a fluxos de treball (p. ex. embuts de vendes).  
  * **Cerca (search):** filtres i agrupacions disponibles en un llistat.  
  * **Calendari:** esdeveniments amb data.  
  * **Pivot i Gràfic (graph):** anàlisi i visualització de dades agregades.

Odoo utilitza **herència de vistes** (`<xpath>`) per adaptar una vista sense modificar-ne directament la definició original, cosa que evita conflictes en actualitzar mòduls.

# Adaptació de consultes

Hi ha diverses maneres d’obtenir informació concreta d’un ERP-CRM:

* **Vista de cerca (search view):** afegir filtres i opcions d’agrupació (`group by`) perquè els usuaris puguin consultar dades des de la interfície sense necessitat de programar.  
* **Consultes ORM (domini):** des del codi Python o des de l’Odoo shell, es poden fer consultes amb un domini, per exemple `[('list_price', '>', 500)]` per buscar productes amb preu superior a 500€.  
* **Consultes SQL directes:** en casos avançats (informes, depuració), es pot consultar directament la base de dades PostgreSQL amb `psql` per obtenir dades que no són fàcils d’extreure des de la interfície.

Adaptar consultes és imprescindible per obtenir informació que l’ERP-CRM no mostra per defecte (p. ex. productes sense estoc, clients sense activitat recent).

# Interfícies d’entrada de dades i processos

* **Interfícies d’entrada de dades:** formularis adaptats (camps nous, seccions reorganitzades) perquè l’usuari introdueixi la informació de manera còmoda i sense errors.  
* **Processos (automatitzacions):** Odoo permet automatitzar accions mitjançant:  
  * **Automated Actions** (`base.automation`): s’executen quan es compleix una condició (creació, modificació d’un registre, o pas del temps).  
  * L’acció associada pot ser canviar el valor d’un camp, enviar un correu, crear una activitat o executar codi Python.

Per exemple: quan es crea un producte sense indicar el material, assignar-li automàticament el valor "No especificat".

# Personalització d’informes

Els informes imprimibles d’Odoo (factures, comandes, albarans...) es generen amb plantilles **QWeb** (HTML/XML combinat amb dades del model) que es converteixen a PDF.

**Per personalitzar un informe:**

1. Localitzar l’informe original a `Settings > Technical > Reporting > Reports`.  
2. **Duplicar-lo** (mai modificar directament l’original, per no perdre’l en futures actualitzacions).  
3. Editar la plantilla QWeb afegint o traient camps, per exemple `<span t-field="line.product_id.x_material"/>`.  
4. Generar el PDF per comprovar el resultat.

**Odoo Studio** permet fer aquesta mateixa tasca de manera visual, sense editar directament l’XML.

# Panells de control (Dashboards)

Els panells de control permeten visualitzar de manera resumida la informació més rellevant del negoci:

* Es construeixen normalment a partir de **vistes Pivot** (taules dinàmiques) i **vistes Gràfic** (graph): barres, línies, pastís.  
* L’app **Dashboards/Spreadsheet** d’Odoo permet combinar diversos gràfics i indicadors (KPI) en un únic tauler.  
* **Odoo Studio** també permet crear dashboards personalitzats sense programar.

Un bon dashboard mostra només la informació clau per prendre decisions (p. ex. vendes del mes, ticket mitjà, productes més venuts), evitant sobrecarregar l’usuari de dades.

# Procediments emmagatzemats de servidor

A diferència d’un ERP tradicional basat en procediments emmagatzemats de la base de dades (PL/pgSQL), Odoo centralitza la lògica de negoci al servidor d’aplicació (Python/ORM). Les eines equivalents són:

* **Server Actions** (`ir.actions.server`): codi Python que s’executa des d’un botó, un menú o de forma automàtica en resposta a un esdeveniment.  
* **Scheduled Actions / Cron** (`ir.cron`): tasques planificades que s’executen periòdicament (p. ex. cada dia), útils per a processos batch com arxivar registres antics o enviar recordatoris.

Aquestes eines permeten adaptar el comportament del sistema sense necessitat de crear un mòdul complet.

# Proves

Abans de donar per bona una adaptació cal verificar-ne el funcionament:

* **Proves funcionals:** el camp/vista/automatització fa el que s’espera.  
* **Proves de regressió:** l’adaptació no ha trencat cap funcionalitat existent.  
* **Entorn de proves:** sempre que sigui possible, provar primer en un entorn de desenvolupament o preproducció (vegeu RA2) abans d’aplicar el canvi a producció.

Es recomana portar un registre senzill de les proves fetes: acció realitzada, resultat esperat, resultat obtingut i si és correcte o no.

# Documentació de les operacions i incidències

* **Documentació de les operacions:** cal registrar quines adaptacions s’han fet (camps, vistes, informes, dashboards, automatitzacions), per poder-les mantenir, reproduir en un altre entorn, o desfer si cal.  
* **Documentació d’incidències:** quan una adaptació provoca un error, cal registrar-ne la data, la descripció, els passos per reproduir-la, el missatge d’error i la solució aplicada.  
* Aquesta documentació és la mateixa bona pràctica ja vista al RA1 i RA2, aplicada ara al context de la personalització del sistema.

# Integració amb altres sistemes de gestió

Sovint l’ERP-CRM no és l’únic sistema de l’empresa: cal integrar-lo amb botigues online, TPV, sistemes de facturació externs, etc.

**Per què integrar:**

* Evitar la duplicitat de dades i els errors de doble entrada.  
* Automatitzar processos entre sistemes (p. ex. una comanda feta a la botiga online genera automàticament una comanda de venda a Odoo).

**Mecanismes d’integració:**

* **XML-RPC / JSON-RPC:** protocols natius d’Odoo per accedir-hi des d’aplicacions externes (autenticació, lectura i escriptura de dades).  
* **API REST:** moltes aplicacions externes (botigues online, TPV) exposen una API REST que es pot connectar amb Odoo mitjançant un mòdul pont o un script.  
* **Connectors ja existents:** Odoo disposa de connectors oficials o de tercers per a plataformes populars (Shopify, PrestaShop, Amazon, etc.).  
* **Fitxers d’intercanvi:** en integracions més senzilles, exportació/importació periòdica de fitxers (CSV, EDI).

**Aspectes a decidir en una integració:**

* Quines dades es sincronitzen i en quin sentit (unidireccional o bidireccional).  
* Amb quina freqüència (temps real, per lots cada hora, diari).  
* Com es resolen els conflictes quan el mateix registre es modifica als dos sistemes.
