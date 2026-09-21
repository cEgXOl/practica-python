# Práctica 3: Python — César Camacho

## Descripción

Resolución de los 20 ejercicios de la Práctica 3 sobre listas, funciones y paquetes, NumPy, diccionarios y pandas, lógica y control de flujo, y bucles.

## Entorno

- Python 3.12
- JupyterLab
- NumPy y pandas (ver `requirements.txt`)

## Estructura del repositorio

| Carpeta | Contenido |
| --- | --- |
| `data/` | Los tres CSV de partida, sin modificar |
| `notebooks/` | Notebook resuelto y ejecutado |
| `src/` | Módulo de funciones auxiliares |
| `outputs/` | CSV generados durante la ejecución |

## Cómo reproducir

Abre una terminal en la raíz de este repositorio. En Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter lab notebooks/practica3_python.ipynb
```

En Linux/macOS, cambia la creación y activación por `python3.12 -m venv .venv` y `source .venv/bin/activate`.
Selecciona en JupyterLab el kernel de `.venv` y ejecuta todas las celdas en orden desde `notebooks/`. Los datos se cargan con rutas relativas como `../data/ventas_retail.csv`.

## Nota sobre las comprobaciones del enunciado

Las cifras orientativas de los ejercicios 15 y 20 usan un criterio de redondeo distinto al que exige el propio ejercicio 15. El notebook conserva el redondeo por pedido solicitado y muestra también cómo se obtienen los importes orientativos al redondear solo después de sumar.
