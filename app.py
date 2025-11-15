import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path

DATA_PATH = Path(__file__).parent / "vehicles_us.csv"


@st.cache_data
def load_data(path: Path):
	return pd.read_csv(path)


def main():
	st.header("Exploración del dataset `vehicles_us.csv`")

	try:
		df = load_data(DATA_PATH)
	except Exception as e:
		st.error(f"Error leyendo el dataset: {e}")
		return

	st.write(f"Dataset cargado: {len(df)} filas × {len(df.columns)} columnas")

	# Selección de columna para graficar
	numeric_columns = [c for c in ["price", "odometer", "model_year"] if c in df.columns]
	col = st.selectbox("Elegir columna para el histograma", numeric_columns, index=0)

	if st.button(f"Construir histograma de `{col}`"):
		# Normalizar / limpiar la columna seleccionada
		series = pd.to_numeric(df[col], errors="coerce").dropna()

		if col == "price":
			series = series[series > 0]
		elif col == "odometer":
			series = series[series >= 0]
		elif col == "model_year":
			current_year = pd.Timestamp.now().year
			series = series[(series > 1900) & (series <= current_year + 1)]

		if series.empty:
			st.warning(f"No hay datos válidos en la columna `{col}` después de limpiar")
		else:
			hist_df = series.to_frame(name=col)
			fig = px.histogram(hist_df, x=col, nbins=50, title=f"Histograma — {col}")
			st.write(f"Histograma de la columna `{col}` (n={len(series)})")
			st.plotly_chart(fig, use_container_width=True)

	# --- Gráfico de dispersión (scatter) ---
	st.markdown("---")
	# Opciones para scatter: elegir ejes X e Y entre columnas numéricas disponibles
	numeric_cols_all = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
	# Fallback to common numeric columns if numeric detection is too strict
	if not numeric_cols_all:
		numeric_cols_all = [c for c in ["price", "odometer", "model_year"] if c in df.columns]
	if len(numeric_cols_all) >= 2:
		x_default = numeric_cols_all[0]
		y_default = numeric_cols_all[1]
	else:
		x_default = numeric_cols_all[0] if numeric_cols_all else None
		y_default = None

	x_col = st.selectbox("Eje X (scatter)", options=numeric_cols_all, index=0 if x_default else 0)
	y_col = st.selectbox("Eje Y (scatter)", options=numeric_cols_all, index=1 if len(numeric_cols_all) > 1 else 0)

	if st.button("Construir gráfico de dispersión"):
		if x_col is None or y_col is None or x_col == y_col:
			st.warning("Por favor selecciona dos columnas numéricas distintas para X y Y.")
		else:
			# Preparar datos: conversión segura a numérico y dropna en ambas columnas
			scatter_df = df[[x_col, y_col]].copy()
			scatter_df[x_col] = pd.to_numeric(scatter_df[x_col], errors="coerce")
			scatter_df[y_col] = pd.to_numeric(scatter_df[y_col], errors="coerce")
			scatter_df = scatter_df.dropna()

			if scatter_df.empty:
				st.warning("No hay datos válidos para construir el scatter después de limpiar.")
			else:
				# Si hay muchos puntos, muestrear para mantener la interactividad
				max_points = 5000
				if len(scatter_df) > max_points:
					sample_indices = scatter_df.sample(max_points, random_state=0).index
					scatter_df = scatter_df.loc[sample_indices]

				# Colorear por 'type' si existe (usar índices coincidentes)
				color_col = "type" if "type" in df.columns else None
				if color_col:
					scatter_df[color_col] = df.loc[scatter_df.index, color_col]
					fig_scatter = px.scatter(scatter_df, x=x_col, y=y_col, color=color_col, title=f"Scatter: {x_col} vs {y_col}")
				else:
					fig_scatter = px.scatter(scatter_df, x=x_col, y=y_col, title=f"Scatter: {x_col} vs {y_col}")
				st.write(f"Gráfico de dispersión `{x_col}` vs `{y_col}` (muestra n={len(scatter_df)})")
				st.plotly_chart(fig_scatter, use_container_width=True)


if __name__ == "__main__":
	main()

