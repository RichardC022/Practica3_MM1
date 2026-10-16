# ------------------------------------------------------------
# Esta clase se encarga de TODA la interaccion con el usuario:
# menu, tabla comparativa y graficas con matplotlib.
# ------------------------------------------------------------

import matplotlib.pyplot as plt


class VistaMM1:

    # --------------------------------------------------------
    # Menu principal
    # --------------------------------------------------------
    def mostrar_menu(self):
        print("===================================")
        print("   SIMULACION M/M/1 CON SIMPY")
        print("===================================")
        print("1. Escenario estable           (lambda=2.0, mu=3.0)")
        print("2. Escenario mayor utilizacion (lambda=2.5, mu=3.0)")
        print("3. Escenario cerca saturacion  (lambda=2.9, mu=3.0)")
        print("0. Salir")
        print("===================================")

    def pedir_opcion(self):
        # Pedimos al usuario que elija una opcion del menu
        try:
            return int(input("Elige una opcion: "))
        except ValueError:
            return -1

    # --------------------------------------------------------
    # Tabla comparativa teorico vs simulado
    # --------------------------------------------------------
    def mostrar_tabla_comparativa(self, nombre, teorico, simulado):
        print("\n--- Resultados del escenario:", nombre, "---")
        print("{:<20} {:<15} {:<15}".format("Metrica", "Teorico", "Simulado"))
        print("-" * 52)

        print("{:<20} {:<15.4f} {:<15.4f}".format(
            "Rho", teorico["rho"], "-"))
        print("{:<20} {:<15.4f} {:<15.4f}".format(
            "L  (sistema)", teorico["L"], "-"))
        print("{:<20} {:<15.4f} {:<15.4f}".format(
            "Lq (cola)", teorico["Lq"], simulado["cola_promedio"]))
        print("{:<20} {:<15.4f} {:<15.4f}".format(
            "W  (sistema)", teorico["W"], simulado["sistema_promedio"]))
        print("{:<20} {:<15.4f} {:<15.4f}".format(
            "Wq (cola)", teorico["Wq"], simulado["espera_promedio"]))
        print("-" * 52)
        print("Total de clientes simulados:", simulado["total_clientes"])
        print("Tiempo promedio de espera simulado:", round(simulado["espera_promedio"], 4))
        print("Tamanio promedio de cola simulado:", round(simulado["cola_promedio"], 4))

    # --------------------------------------------------------
    # Grafica de la evolucion de la cola
    # --------------------------------------------------------
    def graficar_cola(self, tamanios_cola):
        plt.figure(figsize=(10, 4))
        plt.plot(tamanios_cola, color="steelblue")
        plt.title("Evolucion del tamanio de la cola")
        plt.xlabel("Numero de llegada")
        plt.ylabel("Clientes en cola")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # Grafica de los tiempos de espera por cliente
    # --------------------------------------------------------
    def graficar_tiempos_espera(self, tiempos_espera):
        plt.figure(figsize=(10, 4))
        plt.plot(tiempos_espera, color="indianred")
        plt.title("Tiempos de espera por cliente")
        plt.xlabel("Cliente")
        plt.ylabel("Tiempo de espera")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # Mensaje generico
    # --------------------------------------------------------
    def mostrar_mensaje(self, mensaje):
        print(mensaje)


# ------------------------------------------------------------
# Bloque de prueba rapida
# ------------------------------------------------------------
if __name__ == "__main__":
    vista = VistaMM1()
    vista.mostrar_menu()
    vista.graficar_cola([0, 1, 2, 3, 2, 1, 0, 0, 1, 2])
    vista.graficar_tiempos_espera([0.1, 0.3, 0.2, 0.5, 0.1, 0.0, 0.4])