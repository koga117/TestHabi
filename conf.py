# Importa las librerías necesarias
import sphinx_rtd_theme

# Define la configuración del proyecto
project = "API de Inmuebles"
author = "chen Casas"
html_theme = "sphinx_rtd_theme"

# Define las extensiones que se usarán
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
]

# Define el orden de los miembros de las clases
autodoc_member_order = "bysource"

# Define el sufijo de los archivos fuente
source_suffix = ".rst"

# Define el documento principal
master_doc = "index"

# Define la ruta a los archivos estáticos
# html_static_path = ["_static"]

# Define las opciones del tema
html_baseurl = "https://example.com/docs/"

# Indica a Sphinx que busque el módulo "api" para generar la documentación
autodoc_modules = ["api"]
