# BasurClasf
Programa que se sirve de un modelo de ML para clasificar basura y otorgar instrucciones respecto a esto en una pagina web

## Instrucciones de ejecucion
### Preparar el entorno

    1. Crea una carpeta llamada `mi_sitio` y entra a ella desde la terminal.
    2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
    3. Instala Django:
    ```bash
    pip install django
    ```
    4. Guarda las dependencias:
    ```bash
    pip freeze > requirements.txt
    ```
### Correr el servidor
    Ejecuta `python manage.py runserver` y verifica que abre en `http://127.0.0.1:8000/`.