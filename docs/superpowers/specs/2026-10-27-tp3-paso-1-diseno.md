# TP3 — Diseño del Paso 1: cargar y revisar los libros

## Intención

Preparar el catálogo del TP3 siguiendo el Paso 1 del enunciado y dejar evidencia reproducible de la limpieza y de las decisiones sobre sinopsis y obras repetidas. El notebook se construirá para que el grupo pueda ejecutarlo y revisar las decisiones con el lector del trabajo.

## Alcance

- Añadir la sección «Paso 1 Cargar y revisar los libros» al notebook `notebooks/TP3_ayala_cerana_colombo_ibarbia.ipynb`, siguiendo el formato de los notebooks TP1 y TP2.
- Cargar `catalogo_tp3.jsonl`; conservar `slug`, `title`, `authors` y `synopsis`; eliminar registros sin sinopsis y duplicados de `slug`.
- Normalizar las secuencias de espacios en blanco a un espacio, sin quitar otros caracteres.
- Mostrar y contabilizar duplicados exactos de sinopsis normalizada. Por la consigna, conservar un registro por sinopsis y, si hay más de uno, conservar el primero en el orden original del JSONL.
- Encontrar candidatos a obras repetidas entre registros con al menos un autor identificable en común. Normalizar títulos y usar la similitud de Levenshtein; usar Jaccard sobre las palabras de las sinopsis como segundo filtro. Los umbrales aprobados para generar candidatos son 0,80 para el título y 0,75 para la sinopsis. Los puntajes no deciden una unión automáticamente.
- Mostrar los candidatos y pedir aprobación antes de excluir una versión por similitud aproximada. Registrar dos uniones y dos separaciones con sus títulos, autores, puntajes y motivos.
- Mostrar cinco registros finales y cantidades eliminadas por cada motivo; reconciliar los totales con el tamaño final del catálogo.
- Crear `documentacion.md` en la raíz del único repositorio disponible. El proyecto no tiene backend, interfaz de usuario ni rutas API; la ficha documentará el notebook como punto de entrada y dejará esas áreas explícitamente como no aplicables.

## Fuera de alcance

- Implementar el Paso 2 o pasos posteriores del TP3.
- Cambiar los datos fuente de la carpeta `TP3`, incluirlos en Git o modificar notebooks de TP1 y TP2.
- Quitar enlaces, puntuación, caracteres invisibles u otros elementos de las sinopsis; pueden ser evidencia para el Paso 2.
- Eliminar libros por puntajes aproximados sin revisión y aprobación humana.

## Enfoques considerados

1. **Notebook con el proceso visible (elegido):** concentrar la carga, las métricas, las tablas y las decisiones en el notebook que pide el TP. Sigue la organización que ya usa el repositorio y facilita estudiar cada operación junto al resultado.
2. **Extraer la lógica a módulos de `src/`:** separaría el código de análisis, pero dispersaría el procedimiento que la entrega pide explicar y ejecutar en el notebook. No se elige para este paso.

## Decisiones de implementación

- Los datos requeridos se versionan en `data/`; el notebook los busca con `data/` desde la raíz del repo y `../data/` desde `notebooks/`. Se mantienen como respaldo las rutas hermanas originales y el directorio actual para archivos cargados en Colab.
- La normalización del título aplicará Unicode NFKC, minúsculas, puntuación como separador y espacios simples; conservará acentos. La normalización de la sinopsis se limitará a colapsar espacios en blanco.
- Se excluirán los autores genéricos `Varios Autores` y `Anónimo` al buscar autor compartido, porque no identifican a una misma persona. Los duplicados exactos de sinopsis se contabilizan aparte.
- Tras revisar la tabla, el usuario aprobó unir los candidatos 1 («Comentarios psicológicos sobre las enseñanzas de Gurdjieff y Ouspensky»), 8 («Ella, Hija de la Sabiduría»), 11 («El príncipe y el mendigo» / «Príncipe y mendigo») y 31 («El contrato social» / «Contrato social»). Se conserva la primera ficha de cada par.
- El candidato 7 («Manual para viajeros por Andalucía y lectores en casa. Granada» / «Manual para viajeros por Andalucía y lectores en casa») se deja separado porque el primer título especifica una región. Sus sinopsis tienen las mismas palabras al ignorar mayúsculas, por lo que Jaccard da 1,00; las diferencias de mayúsculas se conservan en la deduplicación exacta.
- La consigna da como ejemplos que deben separarse «Conversaciones con Dios I/II» y «La escultura del siglo XIX/XX»; el notebook los muestra con sus puntajes y motivos.
- La verificación comprobará que no queden sinopsis vacías, que `slug` y sinopsis normalizada sean únicos después de las decisiones aprobadas, que el muestreo final tenga cinco registros y que las cantidades por motivo cierren con el total.

## Límites

La regla de conservar un registro por sinopsis puede quitar volúmenes diferentes cuando el catálogo reutiliza el mismo texto promocional. La consigna lo solicita expresamente; el notebook mostrará los registros afectados y contará esas eliminaciones por separado de las uniones manuales de obras.
