# Documentación del proyecto <!-- Última modificación: 2026-10-27 -->
<!-- Última modificación: 2026-10-27 -->
## Alcance de esta entrega <!-- Última modificación: 2026-10-27 -->
- Se documentan el Paso 1 y los apartados 2.1 y 2.2 del TP3: limpieza del catálogo y auditoría con expresiones regulares, incluida la normalización previa. <!-- Última modificación: 2026-10-27 -->
- El proyecto es un trabajo de análisis en notebooks; esta entrega no agrega backend, API ni pantallas de interfaz. <!-- Última modificación: 2026-10-27 -->
## Feature: carga y revisión del catálogo <!-- Última modificación: 2026-10-27 -->
- Nombre: Paso 1, cargar y revisar libros. <!-- Última modificación: 2026-10-27 -->
- Ruta y acceso: abrir `notebooks/TP3_ayala_cerana_colombo_ibarbia.ipynb` en Jupyter y ejecutar sus celdas en orden. <!-- Última modificación: 2026-10-27 -->
- Propósito: preparar el catálogo para las consignas posteriores, conservando los datos originales salvo los registros eliminados por las reglas exactas indicadas aquí. <!-- Última modificación: 2026-10-27 -->
- Información mostrada: conteos de limpieza, grupos de sinopsis repetidas, registros disponibles y pares candidatos con títulos, autores compartidos y métricas de similitud. <!-- Última modificación: 2026-10-27 -->
- Acciones e interacciones: ejecutar la instalación de dependencias, cargar el archivo, inspeccionar los resultados y revisar manualmente cada candidato numerado. <!-- Última modificación: 2026-10-27 -->
- Navegación relacionada: el Paso 1 y los apartados 2.1 y 2.2 del Paso 2 aparecen en orden; los apartados 2.3 a 2.7 todavía no forman parte de esta implementación. <!-- Última modificación: 2026-10-27 -->
- Permisos: no hay autenticación ni permisos de aplicación; la persona que ejecuta Jupyter debe poder leer el archivo de entrada local. <!-- Última modificación: 2026-10-27 -->
- Carga: la celda busca `data/catalogo_tp3.jsonl` desde la raíz o `../data/catalogo_tp3.jsonl` desde `notebooks/`; también acepta las rutas hermanas originales y un archivo cargado en Colab. <!-- Última modificación: 2026-10-27 -->
- Vacío: si no hay pares que superen los filtros, la tabla de candidatos queda vacía; los ejemplos de separación requieren que sus libros estén presentes en el catálogo. <!-- Última modificación: 2026-10-27 -->
- Error: si no se encuentra el archivo o falta una dependencia, la celda muestra el error de ejecución de Python/Jupyter y el notebook no continúa hasta corregirlo. <!-- Última modificación: 2026-10-27 -->
- Conexión con backend: no existe backend ni API; las celdas leen y transforman datos localmente con pandas. <!-- Última modificación: 2026-10-27 -->
## Feature: auditoría con expresiones regulares (Paso 2.1) <!-- Última modificación: 2026-10-27 -->
- Nombre y acceso: Paso 2, apartado 2.1; abrir `notebooks/TP3_ayala_cerana_colombo_ibarbia.ipynb` y ejecutar las celdas después del Paso 1. <!-- Última modificación: 2026-10-27 -->
- Pantalla: no tiene una interfaz propia; el punto de entrada y los resultados son celdas del notebook. <!-- Última modificación: 2026-10-27 -->
- Propósito: medir patrones explícitos de URL, correo y teléfono en sinopsis etiquetadas y revisar sus falsos positivos. <!-- Última modificación: 2026-10-27 -->
- Información mostrada: tamaño y composición de las particiones, precisión, recall y cantidad marcada por patrón y combinación, falsos positivos y un ejemplo exploratorio limpio de desarrollo cuando la prueba no tiene falsos positivos. <!-- Última modificación: 2026-10-27 -->
- Acciones e interacciones: ejecutar las celdas; no requiere ingresar valoraciones ni confirmar decisiones. <!-- Última modificación: 2026-10-27 -->
- Navegación relacionada: usa el catálogo disponible tras el Paso 1; conserva `desarrollo` y `prueba` para los apartados siguientes. <!-- Última modificación: 2026-10-27 -->
- Permisos y carga: no hay autenticación; se lee `data/muestra_etiquetada.csv` desde la carpeta de datos localizada por el notebook, con 500 filas y la columna `contaminado`. <!-- Última modificación: 2026-10-27 -->
- Comportamiento: divide por libro en 70 % desarrollo y 30 % prueba con `random_state=42` y estratificación; las métricas usan solo prueba. Los falsos positivos de desarrollo se muestran por separado y no alteran esas métricas. <!-- Última modificación: 2026-10-27 -->
- Resultados verificados: URL precision 1,00 y recall 0,13 (4 marcados); correo 1,00 y 0,07 (2); teléfono 1,00 y 0,03 (1); combinación OR 1,00 y 0,23 (7). La prueba no tuvo falsos positivos. En desarrollo, el libro limpio `que-pasaria-si` menciona `http://www.xkcd.com` y coincide con URL. <!-- Última modificación: 2026-10-27 -->
- Respuesta a la pregunta del enunciado: las URLs explícitas aportaron más detecciones en prueba (4 de 30 libros contaminados; recall global 0,13), seguidas por correo (2 de 30; 0,07) y teléfono (1 de 30; 0,03). Las etiquetas no distinguen tipos, así que no se calcula recall específico por tipo; otras contaminaciones sin esas señales tampoco son detectadas por estas regex. <!-- Última modificación: 2026-10-27 -->
- Vacío y error: si no hay falsos positivos de prueba, se informa ese resultado y se muestra por separado el ejemplo de desarrollo; si falta el CSV o scikit-learn, Jupyter muestra el error de lectura o importación y no continúa. <!-- Última modificación: 2026-10-27 -->
- Límites: las regex detectan formas explícitas; no cubren enlaces disimulados que se tratarán en 2.2. La muestra tiene 20 % de contaminados, por lo que la precisión medida no se extrapola directamente al catálogo. <!-- Última modificación: 2026-10-27 -->
- Backend e integraciones: no hay backend, API ni servicios externos; la ejecución es local y no escribe archivos. <!-- Última modificación: 2026-10-27 -->
## Feature: normalización previa a la búsqueda (Paso 2.2) <!-- Última modificación: 2026-10-27 -->
- Nombre y acceso: Paso 2, apartado 2.2; ejecutar las celdas de `notebooks/TP3_ayala_cerana_colombo_ibarbia.ipynb` después del apartado 2.1. <!-- Última modificación: 2026-10-27 -->
- Pantalla: no tiene una interfaz propia; el punto de entrada, las métricas y los ejemplos son celdas del notebook. <!-- Última modificación: 2026-10-27 -->
- Propósito: recuperar señales de URL disimuladas mediante normalización y comparar sus resultados con las regex aplicadas al texto original. <!-- Última modificación: 2026-10-27 -->
- Información mostrada: precisión, recall y libros marcados por URL, correo, teléfono y combinación, en las versiones original y normalizada; falsos positivos de prueba; dos enlaces recuperados en desarrollo; un dominio con homógrafos que sigue sin detectar; y sinopsis limpias que contienen caracteres invisibles. <!-- Última modificación: 2026-10-27 -->
- Acciones e interacciones: ejecutar las celdas; no requiere ingresar datos ni aprobar decisiones. <!-- Última modificación: 2026-10-27 -->
- Navegación relacionada: reutiliza `muestra`, `desarrollo` y `prueba` del Paso 2.1; el apartado 2.3 todavía está pendiente. <!-- Última modificación: 2026-10-27 -->
- Permisos y carga: no hay autenticación; se usa `data/muestra_etiquetada.csv` y la misma partición fija por libro, 70 % desarrollo y 30 % prueba, con `random_state=42` y estratificación por `contaminado`. <!-- Última modificación: 2026-10-27 -->
- Comportamiento: `normalizar(texto)` devuelve una copia en minúsculas con NFKD, sin combinantes ni caracteres de categoría `Cf`; convierte los homógrafos cirílicos `е` y `а` observados en desarrollo, reemplaza `[.]`, `punto` y `barra`, compacta `h t t p s` y `w w w`, y normaliza espacios alrededor de signos. Conserva las sinopsis originales. <!-- Última modificación: 2026-10-27 -->
- Evaluación: las mismas regex de Paso 2.1 se aplican al original y a la copia normalizada; las métricas usan únicamente la partición de prueba. Los ejemplos cualitativos se seleccionan de desarrollo. <!-- Última modificación: 2026-10-27 -->
- Resultados verificados: original: URL precision 1,00 y recall 0,13 (4 marcados); correo 1,00 y 0,07 (2); teléfono 1,00 y 0,03 (1); combinación 1,00 y 0,23 (7). Normalizado: URL 1,00 y 0,23 (7); correo 1,00 y 0,07 (2); teléfono 1,00 y 0,03 (1); combinación 1,00 y 0,33 (10). No hubo falsos positivos en prueba. <!-- Última modificación: 2026-10-27 -->
- Ejemplos: «España, terra incognita» recupera `https://` con letras y signos separados; «Los crímenes del invisible» recupera `www.` con letras separadas. «Más Allá 13» convierte `е` y `а` cirílicas, pero su dominio desnudo no coincide con las regex aprobadas. <!-- Última modificación: 2026-10-27 -->
- Invisibles y límites: «Hispania» contiene SOFT HYPHEN U+00AD y «Martín Lutero II» contiene WORD JOINER U+2060; ambos siguen sin marca porque esos caracteres no son evidencia por sí solos. Las URLs sin `http(s)://` ni `www.` no se detectan; no se amplió la regex del Paso 2.1. <!-- Última modificación: 2026-10-27 -->
- Vacío y error: si no hay falsos positivos normalizados, se informa ese resultado; si falta el CSV o una dependencia, Jupyter muestra el error de lectura o importación y no continúa. <!-- Última modificación: 2026-10-27 -->
- Backend e integraciones: no hay backend, API ni servicios externos; la ejecución es local y no escribe archivos. <!-- Última modificación: 2026-10-27 -->
## Datos y reglas implementadas <!-- Última modificación: 2026-10-27 -->
- Entrada: `data/catalogo_tp3.jsonl`, versionado en el repositorio; el notebook selecciona `slug`, `title`, `authors` y `synopsis`. <!-- Última modificación: 2026-10-27 -->
- Datos de apoyo: `data/muestra_etiquetada.csv`, `data/ejemplo_preferencias.csv` y `data/ejemplo_sospechosos.csv` quedan disponibles para las consignas posteriores del TP3. <!-- Última modificación: 2026-10-27 -->
- Documentación fuente: el enunciado DOCX y PDF se conserva en `docs/TP3/`; no hace falta para ejecutar los notebooks. <!-- Última modificación: 2026-10-27 -->
- Se normalizan espacios consecutivos de la sinopsis, sin quitar puntuación ni caracteres. <!-- Última modificación: 2026-10-27 -->
- Se descartan sinopsis vacías, slugs repetidos y sinopsis idénticas ya normalizadas, conservando el primer registro de cada caso repetido. <!-- Última modificación: 2026-10-27 -->
- En la corrida verificada se encontraron 1 sinopsis vacía, 0 slugs repetidos y 98 registros adicionales con sinopsis idéntica; quedaron 8.648 registros. <!-- Última modificación: 2026-10-27 -->
- Para revisión aproximada se comparan libros que comparten al menos un autor identificable; se excluyen las etiquetas genéricas `Varios Autores` y `Anónimo`. <!-- Última modificación: 2026-10-27 -->
- Levenshtein normalizado del título debe ser al menos 0,80 y Jaccard de palabras de la sinopsis al menos 0,75 para mostrar un par candidato. <!-- Última modificación: 2026-10-27 -->
- Los 66 pares resultantes son sugerencias para revisión manual; se aprobaron las fusiones de los candidatos 1, 7, 8, 11 y 31. <!-- Última modificación: 2026-10-27 -->
- En cada fusión se conserva la primera ficha del catálogo y se elimina la segunda; la tabla del notebook muestra títulos, autores, puntajes y motivos. <!-- Última modificación: 2026-10-27 -->
- El candidato 7 se fusiona: comparte autor y Jaccard de sinopsis 1,00, es decir, el mismo conjunto de palabras tras convertirlas a minúsculas; se conserva la primera ficha del catálogo aunque la otra especifique Granada. <!-- Última modificación: 2026-10-27 -->
- El apartado 2.2 del Paso 2 conserva las sinopsis originales, normaliza una copia para buscar señales disimuladas y mide las mismas regex sobre la partición fija de prueba. <!-- Última modificación: 2026-10-27 -->
- El notebook presenta además dos pares separados por representar volúmenes o contenidos distintos y muestra cinco filas de ejemplo del catálogo final. <!-- Última modificación: 2026-10-27 -->
- En la corrida final se quitaron 1 sinopsis vacía, 0 slugs duplicados, 98 sinopsis exactas repetidas y 5 fichas por fusión aprobada; quedaron 8.643 libros. <!-- Última modificación: 2026-10-27 -->
## Operación y despliegue <!-- Última modificación: 2026-10-27 -->
- Dependencias: instalar las incluidas en `requirements.txt`, entre ellas `python-Levenshtein` y `scikit-learn`, y abrir el notebook con Jupyter. <!-- Última modificación: 2026-10-27 -->
- Persistencia: los pasos 1, 2.1 y 2.2 muestran resultados dentro del notebook y no escriben cambios en el catálogo ni exportan sospechosos. <!-- Última modificación: 2026-10-27 -->
- Seguridad e integraciones: no se envían datos a servicios externos ni se agregan credenciales. <!-- Última modificación: 2026-10-27 -->
- Despliegue: no aplica; el notebook se ejecuta localmente para la entrega académica. <!-- Última modificación: 2026-10-27 -->
