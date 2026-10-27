# Diseño del TP3 — Paso 2.2: normalizar antes de buscar

## Intención

Recuperar algunas señales de URL que la regex del Paso 2.1 no ve cuando sus letras, signos o caracteres Unicode están disimulados, y mostrar qué aporta la normalización.

## Alcance

- Implementar solo el apartado 2.2 en el notebook de TP3.
- Agregar `normalizar(texto)`, que produce una copia normalizada y conserva intacta la sinopsis original.
- En la copia: pasar a minúsculas; aplicar NFKD y quitar caracteres combinantes, como en la Unidad 1; eliminar caracteres Unicode de categoría `Cf`; convertir a ASCII los homógrafos cirílicos o griegos visualmente equivalentes que aparezcan en enlaces de desarrollo; normalizar las palabras y signos separados que pide el enunciado, incluidas las formas observadas `h t t p s`, `w w w`, `[.]`, `punto` y `barra`.
- No quitar espacios de toda la sinopsis: compactarlos solo dentro de las secuencias reconocidas de enlace y alrededor de sus signos. Los caracteres invisibles no generan una marca por sí solos; la marca requiere que alguna regex encuentre una señal después de normalizar.
- Reaplicar sin cambios las regex de URL, correo y teléfono aprobadas en el Paso 2.1. Comparar las métricas originales y normalizadas de cada patrón y de su combinación, siempre sobre la misma partición `prueba`.
- Mostrar dos recuperaciones de `desarrollo`: «España, terra incognita» (`h t t p s : / /` y `[.]`) y «Los crímenes del invisible» (`w w w .`). Mostrar el texto original y el normalizado.
- Revisar también ejemplos limpios de desarrollo que contienen caracteres invisibles para explicar por qué quitarlos no basta para declarar contaminación.
- Actualizar `documentacion.md` y el estado de TP3 en `README.md`.
- Verificar ejecutando el notebook completo y revisando las tablas y ejemplos. No agregar tests, aserciones ni dependencias.

## Fuera de alcance

- Cambiar las regex o métricas del Paso 2.1, usar etiquetas de prueba para elegir transformaciones, entrenar modelos o detectar mensajes promocionales sin señales de URL/correo/teléfono.
- Ampliar la regex para detectar dominios desnudos sin `http(s)://` ni `www.`. Ese límite se mantiene explícito para no cambiar el detector aprobado en el paso anterior.
- Marcar un libro solo porque su texto contiene caracteres invisibles.

## Enfoques considerados

1. **Normalización acotada, elegida por el usuario:** trabajar sobre una copia; aplicar las transformaciones Unicode y de enlaces indicadas, mantener la regex existente y medir su efecto con la partición fija. Preserva la evidencia original y permite atribuir las recuperaciones.
2. **Limpieza amplia:** quitar puntuación y espacios de todo el texto y transliterar alfabetos completos. Se descarta porque altera palabras de sinopsis legítimas y puede aumentar falsos positivos sin una señal de enlace.

## Límites

La regex aprobada solo reconoce URLs con protocolo o `www.`. Normalizar un dominio desnudo puede revelar sus caracteres, pero no hará que esa regex lo marque. La muestra puede contener invisibles en texto limpio; se evalúa el resultado de los patrones, no la presencia aislada de esos caracteres.
