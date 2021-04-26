# Desarrollo de una versión Web de Catálogo de Datos
Servicio Web implementado para el catálogo de datos de la UGI

### Componentes Implementados:
- navegation bar con opcion de regreso a inicio <a link reference : inicio.
- Search bar.
- Search hacia la base de datos
- Formulario donde alimente tabla de dominios y que linkee las tablas asociadas
- Diseno del footer
- Cards por Dominio
- Table View
- Descarga de muestra de datos (20 registros)


### Mejoras de exploración

- dato critico
- cantidad de registros de la tabla
- muestra de datos top mil
- tablas asociadas a las unidades de analizis
- historica, data por a;o, desde cuando tiene la data


### TABLAS DE CONSUMO DEL ORACLE
- LISTADO_COMENTARIO

- LISTADO_OBJECT

- LISTADO_DICCIONARIO 

- Tablas del Catálogo


### Observaciones a mejorar 01
1) mas visual (stand by)
2) darle una proyeccion para incluir las unidades 
3) descripcion del dominio en la vista tablas

### Observaciones a mejorar 02
1) " Disponible en DataLake MEF " -- Icono
2) Cabecera y cuadro uniforme en los dominios
3) Los numeros grandes que sean legibles a lectura
4) Incorporarle botones de navegacion, retroceder
5) Columna fija de navegacion por dataset
6) anadir Barra vertical y horizontal en las tablas 
7) Anadir filtro en la vista de tablas para busquedas mas rapidas por el usuario.
8) Ordenar alfabeticamente los dominios
9) mismos tama;os en los box de los dominios (Completar com cuadros vacios las estructuras de 3 en el home)
10) Verificar la compatibilidad con las herramientas de OGTI (Con Tooru)

### Observaciones a mejorar 03
METADATOS Y CATALOGACIÓN
- En la exploración de campos se recomienda colocar la descripción de los campos.
- Los campos de códigos, colocar dominio de valores (en los que corresponda)
- Colocar un diagrama de relaciones de tablas y campos
- Identificar la fecha y hora de la última actualización de cada tabla, tipo de recurso ( Oracle, SQL, información no relacional, otros)
- Tener información del número de consultas realizadas o utilizadas por cada tabla
- Auditoría de que usuarios han bajado o utilizado la información
- Establecer procedimiento referente a la protección de datos personales, datos sensibles, enmascaramiento de campos.
- No solo colocar buscador de información, sino una sección de filtros por otros metadatos.
