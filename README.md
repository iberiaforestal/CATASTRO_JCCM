# Informe de Afecciones Ambientales por Parcela

Esta aplicación permite generar informes de afecciones ambientales para parcelas específicas, consultando capas WMS oficiales y generando un informe en PDF.

## Características

- Formulario para ingresar datos del solicitante y de la parcela.
- Visualización de mapa interactivo con capas WMS:
  - ZEPAs
  - LICs
  - Vías Pecuarias
  - Montes Públicos
  - Catastro
- Generación de informe en PDF con los datos ingresados y las afecciones consultadas.
- Descarga del informe PDF y del mapa interactivo.

## Requisitos

- Python 3.7 o superior
- Paquetes listados en `requirements.txt`

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/informe_afecciones_app.git
   cd informe_afecciones_app
   ```

2. Crea un entorno virtual (opcional):

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta la aplicación:

```bash
streamlit run app.py
```

## Despliegue

Puedes subir el proyecto a [Streamlit Cloud](https://streamlit.io/cloud).

## Licencia

MIT
