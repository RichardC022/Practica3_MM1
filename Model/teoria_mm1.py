"""
Módulo encargado del cálculo de las métricas teóricas para un modelo de colas M/M/1.
"""

from dataclasses import dataclass
from typing import Dict, Any, Union


@dataclass
class MetricasTeoricas:
    lambda_param: float
    mu_param: float
    rho: float
    L: float
    Lq: float
    W: float
    Wq: float

    def a_dict(self) -> Dict[str, float]:
        """Convierte las métricas a un diccionario para facilitar su uso en vistas o tablas."""
        return {
            "lambda": self.lambda_param,
            "mu": self.mu_param,
            "rho": self.rho,
            "L": self.L,
            "Lq": self.Lq,
            "W": self.W,
            "Wq": self.Wq,
        }


class TeoriaMM1:
    """Clase para calcular y validar las métricas teóricas de un sistema M/M/1[cite: 1, 2]."""

    def __init__(self, lambda_param: float, mu_param: float):
        """
        Inicializa las tasas del sistema.
        
        :param lambda_param: Tasa promedio de llegada de clientes (lambda).
        :param mu_param: Tasa promedio de servicio del servidor (mu)[cite: 2].
        """
        if lambda_param <= 0 or mu_param <= 0:
            raise ValueError("Las tasas lambda y mu deben ser mayores que cero.")
        
        self.lambda_param = float(lambda_param)
        self.mu_param = float(mu_param)

    def es_estable(self) -> bool:
        """
        Verifica si el sistema es estable (lambda < mu).
        
        :return: True si el sistema es estable, False en caso contrario.
        """
        return self.lambda_param < self.mu_param

    def calcular_utilizacion(self) -> float:
        """
        Calcula la utilización del servidor: rho = lambda / mu[cite: 2].
        """
        return self.lambda_param / self.mu_param

    def calcular_metricas(self) -> MetricasTeoricas:
        """
        Calcula las medidas teóricas del sistema M/M/1[cite: 2].
        
        L = lambda / (mu - lambda)[cite: 2]
        Lq = lambda^2 / (mu * (mu - lambda))[cite: 2]
        W = 1 / (mu - lambda)[cite: 2]
        Wq = lambda / (mu * (mu - lambda))[cite: 2]
        
        :return: Objeto MetricasTeoricas con los resultados.
        :raises ValueError: Si el sistema no es estable (lambda >= mu)[cite: 3].
        """
        if not self.es_estable():
            raise ValueError(
                f"El sistema no es estable (lambda={self.lambda_param} >= mu={self.mu_param}). "
                "La cola crecería indefinidamente[cite: 3]."
            )

        lam = self.lambda_param
        mu = self.mu_param

        rho = self.calcular_utilizacion()
        L = lam / (mu - lam)
        Lq = (lam ** 2) / (mu * (mu - lam))
        W = 1 / (mu - lam)
        Wq = lam / (mu * (mu - lam))

        return MetricasTeoricas(
            lambda_param=lam,
            mu_param=mu,
            rho=rho,
            L=L,
            Lq=Lq,
            W=W,
            Wq=Wq
        )


def obtener_metricas_teoricas(lambda_param: float, mu_param: float) -> Union[Dict[str, float], None]:
    """
    Función de conveniencia para el controlador o fábrica de escenarios[cite: 4].
    Calcula y retorna un diccionario con los resultados teóricos.
    """
    try:
        modelo = TeoriaMM1(lambda_param, mu_param)
        metricas = modelo.calcular_metricas()
        return metricas.a_dict()
    except ValueError as e:
        print(f"[Error TeoriaMM1]: {e}")
        return None


# Bloque para pruebas rápidas directas del módulo
if __name__ == "__main__":
    escenarios = [
        {"nombre": "Escenario 1 (Estable)", "lambda": 2.0, "mu": 3.0},[cite: 4]
        {"nombre": "Escenario 2 (Mayor utilización)", "lambda": 2.5, "mu": 3.0},[cite: 4]
        {"nombre": "Escenario 3 (Cerca de saturación)", "lambda": 2.9, "mu": 3.0},[cite: 4]
        {"nombre": "Escenario Inestable", "lambda": 3.5, "mu": 3.0},
    ]

    print("=== PRUEBA DE CÁLCULOS TEÓRICOS M/M/1 ===\n")
    for esc in escenarios:
        print(f"--- {esc['nombre']} ---")
        try:
            modelo = TeoriaMM1(esc["lambda"], esc["mu"])
            m = modelo.calcular_metricas()
            print(f"  Utilización (rho) : {m.rho:.4f}")
            print(f"  Clientes sistema (L): {m.L:.4f}")
            print(f"  Clientes cola (Lq)  : {m.Lq:.4f}")
            print(f"  Tiempo sistema (W)  : {m.W:.4f}")
            print(f"  Tiempo cola (Wq)    : {m.Wq:.4f}")
        except ValueError as err:
            print(f"  Error: {err}")
        print()