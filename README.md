# Wikipedia Web Scraper

Este repositorio contiene un script en Python que extrae el título, las secciones y los párrafos seleccionados de **cualquier página de Wikipedia**. El objetivo es permitir que los usuarios analicen el contenido de cualquier página de Wikipedia de manera automática y seleccionen las secciones de interés.

## Descripción

Este script utiliza `requests` para obtener el contenido HTML de una página de Wikipedia, y `BeautifulSoup` (de la biblioteca `bs4`) para analizar la estructura de la página y extraer:

- **Título de la página**.
- **Secciones**: Extrae todas las secciones principales (`<h2>`) de la página.
- **Párrafos seleccionados**: El usuario puede elegir las secciones de las que desea extraer párrafos, y el programa devuelve esos párrafos en orden.

Es un web scraper general diseñado para ser utilizado con cualquier página de Wikipedia.

## Requisitos

- Python 3.x
- Paquetes adicionales: `requests`, `beautifulsoup4`

Puedes instalarlos ejecutando:

```bash
pip install requests beautifulsoup4
