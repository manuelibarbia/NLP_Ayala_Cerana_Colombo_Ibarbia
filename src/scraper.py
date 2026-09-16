import os
import time
import random
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse

# --- CONFIGURACIÓN DE RUTAS ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# --- CONSTANTES ---
URL_CATEGORIA = "https://ww3.lectulandia.co/genero/drama/"
URL_BASE = "https://ww3.lectulandia.co"
MAX_LIBROS = 150
CATEGORIA = "Drama"


def limpiar_texto(valor):
    """Normaliza espacios y representa los valores ausentes como texto vacío."""
    if valor is None:
        return ""
    return " ".join(str(valor).split())


def url_libro_valida(url):
    """Comprueba que la URL sea HTTP(S) y apunte a una ficha de libro."""
    parsed = urlparse(url)
    return (
        parsed.scheme in {"http", "https"}
        and bool(parsed.netloc)
        and parsed.path.startswith("/book/")
    )


def validar_libro(libro):
    """Devuelve un registro limpio si tiene los campos mínimos requeridos."""
    registro = {campo: limpiar_texto(libro.get(campo, "")) for campo in libro}
    if not registro["titulo"]:
        return None
    if not url_libro_valida(registro["url_libro"]):
        return None
    if not registro["categoria_origen"] or not registro["fecha_extraccion"]:
        return None
    return registro

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Iniciando extracción - Categoría Drama")
    fecha_hoy = date.today().isoformat()
    
    with sync_playwright() as p:
        # Iniciamos el navegador (headless=True para que corra en segundo plano)
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()

        # =========================================================
        # PASO 1: Descubrimiento de URLs usando Playwright
        # (Consigna: Recorrer la categoría para obtener los enlaces)
        # =========================================================
        enlaces_libros = []
        enlaces_vistos = set()
        num_pagina = 1

        while len(enlaces_libros) < MAX_LIBROS:
            url_actual = URL_CATEGORIA if num_pagina == 1 else f"{URL_CATEGORIA}page/{num_pagina}/"
            print(f"Revisando grilla, página {num_pagina}...")
            
            try:
                page.goto(url_actual, timeout=60000)
                # Consigna: Implementar pausas para no saturar el servidor
                time.sleep(random.uniform(1.0, 2.5))
                
                soup = BeautifulSoup(page.content(), "html.parser")
                tarjetas = soup.select("article.card h2 a.title")
                
                for tarjeta in tarjetas:
                    if len(enlaces_libros) < MAX_LIBROS:
                        link_relativo = tarjeta.get('href')
                        if not link_relativo:
                            continue
                        link_completo = urljoin(URL_BASE, link_relativo)
                        
                        # Consigna: Evitar libros duplicados
                        if link_completo not in enlaces_vistos:
                            enlaces_libros.append(link_completo)
                            enlaces_vistos.add(link_completo)
            except Exception as e:
                print(f"⚠️ Error en la página {num_pagina}: {e}")
                break

            num_pagina += 1

        print(f"Descubrimiento completado: {len(enlaces_libros)} enlaces obtenidos.")

        # =========================================================
        # PASO 2: Extracción de metadatos y sinopsis con BeautifulSoup
        # (Consignas: Uso de BeautifulSoup y Manejo de Errores)
        # =========================================================
        print("Iniciando extracción de fichas individuales...")
        datos_libros = []
        urls_registradas = set()
        
        for i, url in enumerate(enlaces_libros):
            print(f"[{i+1}/{MAX_LIBROS}] Extrayendo: {url}")
            
            try:
                page.goto(url, timeout=60000)
                # Consigna: Pausa entre visitas a las fichas
                time.sleep(random.uniform(1.0, 2.5))
                
                soup = BeautifulSoup(page.content(), "html.parser")
                
                # Consigna: Manejo de errores en la extracción (try/except por campo)
                try:
                    titulo = soup.select_one('main h1').get_text(" ", strip=True)
                except Exception:
                    titulo = ""
                    
                try:
                    autores_tags = soup.select('#autor a')
                    autores = ", ".join([a.text.strip() for a in autores_tags])
                except Exception:
                    autores = ""
                    
                try:
                    generos_tags = soup.select('#genero a')
                    generos = ", ".join([g.text.strip() for g in generos_tags])
                except Exception:
                    generos = ""
                    
                try:
                    serie = soup.select_one('#serie a').text.strip()
                except Exception:
                    serie = ""
                    
                try:
                    sinopsis_container = soup.select_one('#sinopsis')
                    if sinopsis_container:
                        # Limpieza de saltos de línea HTML
                        for br in sinopsis_container.find_all("br"):
                            br.replace_with(" ")
                        sinopsis = sinopsis_container.get_text(" ", strip=True)
                    else:
                        sinopsis = ""
                except Exception:
                    sinopsis = ""
                
                # Agregamos los datos al diccionario
                libro_sin_validar = {
                    "titulo": titulo,
                    "autores": autores,
                    "generos": generos,
                    "serie": serie,
                    "sinopsis": sinopsis,
                    "url_libro": url,
                    "categoria_origen": CATEGORIA,
                    "fecha_extraccion": fecha_hoy
                }

                libro = validar_libro(libro_sin_validar)
                if libro is None:
                    print(f"Registro descartado por falta de datos válidos: {url}")
                    continue
                if libro["url_libro"] in urls_registradas:
                    print(f"Registro duplicado descartado: {url}")
                    continue

                datos_libros.append(libro)
                urls_registradas.add(libro["url_libro"])
                
            except Exception as e:
                # Consigna: Control de errores para que la ejecución no se detenga
                print(f"Error general cargando la ficha {url}: {e}")

        print("Extracción de metadatos completada.")

        # =========================================================
        # PASO 3: Guardado de resultados
        # (Consigna: Generar el archivo libros.csv)
        # =========================================================
        print("Guardando datos en libros.csv...")
        
        ruta_csv = os.path.join(DATA_DIR, "libros.csv")
        df = pd.DataFrame(datos_libros)
        df.to_csv(ruta_csv, index=False, encoding='utf-8')
        
        print(f"Extracción finalizada Dataset guardado en: {ruta_csv}")

        browser.close()

if __name__ == "__main__":
    main()
