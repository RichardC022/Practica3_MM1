# controller/controlador_mm1.py
# ------------------------------------------------------------
# El controlador une el MODELO con la VISTA.
# - Pide opcion a la vista.
# - Pide escenario a la fabrica.
# - Calcula teoria (modelo).
# - Ejecuta simulacion (modelo).
# - Muestra resultados y graficas (vista).
# ------------------------------------------------------------

from model.teoria_mm1 import TeoriaMM1
from model.simulacion_mm1 import SimulacionMM1
from view.vista_mm1 import VistaMM1
from controller.factory_escenarios import FactoryEscenarios


class ControladorMM1:

    def __init__(self):
        # Instanciamos la vista y la fabrica
        self.vista = VistaMM1()
        self.factory = FactoryEscenarios()

    def ejecutar(self):
        # Bucle principal del programa
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == 0:
                self.vista.mostrar_mensaje("Saliendo del programa...")
                break

            # Pedimos a la fabrica el escenario correspondiente
            datos = self.factory.crear_escenario(opcion)

            if datos is None:
                self.vista.mostrar_mensaje("Opcion invalida, intenta de nuevo.")
                continue

            # 1) Calculamos los valores teoricos
            teoria = TeoriaMM1(datos["lambd"], datos["mu"])

            if not teoria.verificar_estabilidad():
                self.vista.mostrar_mensaje("El sistema NO es estable (lambda >= mu).")
                continue

            metricas_teoricas = teoria.obtener_todas_las_metricas()

            # 2) Ejecutamos la simulacion con SimPy
            sim = SimulacionMM1(datos["lambd"], datos["mu"], tiempo_total=1000)
            metricas_simuladas = sim.ejecutar_simulacion()

            # 3) Mostramos la tabla comparativa
            self.vista.mostrar_tabla_comparativa(
                datos["nombre"], metricas_teoricas, metricas_simuladas
            )

            # 4) Mostramos las graficas
            self.vista.graficar_cola(sim.tamanios_cola)
            self.vista.graficar_tiempos_espera(sim.tiempos_espera)


if __name__ == "__main__":
    app = ControladorMM1()
    app.ejecutar()