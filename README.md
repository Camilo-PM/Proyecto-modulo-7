# Proyecto-modulo-7

Breve proyecto de análisis exploratorio y visualización interactiva sobre un dataset de vehículos usados.

Descripción
- Esta aplicación usa `Streamlit` para ofrecer una interfaz web sencilla que permite explorar el CSV `vehicles_us.csv`.
- Funcionalidad principal:
	- Cargar el dataset `vehicles_us.csv` (ubicado en el mismo directorio del repositorio).
	- Construir histogramas interactivos de columnas numéricas (por defecto `price`, `odometer`, `model_year`).
	- Construir gráficos de dispersión (scatter) entre dos columnas numéricas seleccionables; opcionalmente colorear por `type` si existe.

Archivos importantes
- `app.py` — aplicación Streamlit principal (leer el CSV, UI, histograma y scatter).
- `vehicles_us.csv` — dataset usado por la app.
- `Notebooks/EDA.ipynb` — notebook de exploración original.
- `requirements.txt` — dependencias con versiones fijadas (`streamlit`, `pandas`, `plotly`).

Cómo ejecutar (PowerShell)
1. Activar el entorno virtual (si existe `.venv` en la raíz del workspace):
```powershell
& "${PWD}\.venv\Scripts\Activate.ps1"
```
2. Instalar dependencias:
```powershell
pip install -r requirements.txt
```
3. Ejecutar la app Streamlit:
```powershell
streamlit run app.py
```

Ejecutar el notebook (Notebooks/EDA.ipynb)
- Iniciar Jupyter Lab/Notebook:
```powershell
jupyter lab
```
- Abrir `Notebooks/EDA.ipynb` en el navegador y ejecutar las celdas en orden.
- Ejemplo rápido de análisis (celdas de ejemplo que puedes usar en el notebook):
```python
import pandas as pd
df = pd.read_csv('vehicles_us.csv')
df.describe()
df['price'].dropna().astype(float).describe()
```

Notas de uso
- En la app puedes elegir la columna para el histograma mediante un `selectbox`.
- El histograma y el scatter limpian valores no numéricos y filtran rangos razonables (por ejemplo `price > 0`).
- Para scatter con muchos puntos, la app muestrea hasta 5000 puntos para mantener la interactividad.

Recomendaciones
- Usa Python 3.10+ si es posible.
- Si prefieres que la app no muestree los puntos o que use otro umbral, modifica `app.py` en la sección del scatter.

Contacto / siguiente paso
- Si quieres que agregue más visualizaciones (mapas, series temporales) o un pequeño `src/` con pruebas, dime y lo implemento.

