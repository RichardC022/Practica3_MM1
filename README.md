# Practica3_MM1 — Simulación de Colas M/M/1

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![SimPy](https://img.shields.io/badge/SimPy-4.x-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![Licencia](https://img.shields.io/badge/licencia-MIT-lightgrey)

## 1. Descripción del proyecto

Elaboración de una aplicación de consola que calcula las métricas analíticas de un sistema de colas **M/M/1** (ρ, L, Lq, W, Wq) y las compara contra los resultados de una **simulación de eventos discretos con SimPy**, permitiendo además validar la estabilidad del sistema (λ < μ); como interfaz, ofrece un menú interactivo con tres escenarios predefinidos y visualiza la evolución de la cola y los tiempos de espera mediante gráficas de Matplotlib.

## 2. Tecnologías utilizadas

- **Python 3.10+** — lenguaje principal.
- **SimPy 4.x** — simulación de eventos discretos.
- **Matplotlib 3.x** — gráficas de cola y tiempos de espera.
- **Librería estándar** — `random` (variables exponenciales), `dataclasses` y `typing`.
- **Git / GitHub** — control de versiones y trabajo por ramas.

> Sin base de datos, Docker ni servicios externos. No maneja credenciales ni secretos; se recomienda usar un entorno virtual aislado y no ejecutar como root.

## 3. Instalación

```bash
git clone https://github.com/RichardC022/Practica3_MM1.git
cd Practica3_MM1
python3 -m venv venv
source venv/bin/activate # Linux       # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 4. Uso

```bash
python main.py
```

El menú permite elegir entre tres escenarios (estable, mayor utilización y cerca de saturación) o salir. Al seleccionar uno, muestra la tabla Teórico vs. Simulado y las gráficas. Módulos con prueba individual: `python Model/teoria_mm1.py`, `python Model/simulacion_mm1.py`.

Validaciones: parámetros > 0, estabilidad `λ < μ`, y entradas inválidas no detienen el programa.

## 5. Configuración

No requiere variables de entorno ni `.env`. La configuración vive en el código: escenarios en `Controller/factory_escenarios.py` y horizonte de simulación (`tiempo_total = 1000`) en `Controller/controlador_mm1.py`.

## 6. Estructura del proyecto

```
Practica3_MM1/
├── main.py                  # Punto de entrada
├── requirements.txt         # Dependencias (simpy, matplotlib)
├── Docs/                    # Documentación adicional
├── Controller/              # Control: bucle principal y fábrica de escenarios
├── Model/                   # Dominio: teoría M/M/1 y simulación SimPy
└── View/                    # Presentación: menú, tabla y gráficas
```

## 7. Información adicional

- **Funcionalidades clave:** métricas analíticas M/M/1, simulación SimPy, validación de estabilidad, tabla comparativa, gráficas, escenarios preconfigurados y manejo de errores.
- **Capturas de pantalla:** _pendiente_ (menú, tabla y gráficas).
- **Documentación de la API:** sin API HTTP; interfaces en `TeoriaMM1`, `SimulacionMM1`, `FactoryEscenarios` y `VistaMM1`.
- **Contribución:** fork → rama `feature/...` → Pull Request a `main`.
- **Licencia:** MIT (agregar archivo `LICENSE` si aún no existe).
