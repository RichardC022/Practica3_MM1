#Importamos las librerias necesarias
import simpy
import random


class SimulacionMM1:

    def __init__(self, lambd, mu, tiempo_total=1000):


        self.lambd = lambd
        self.mu = mu
        self.tiempo_total = tiempo_total


        self.tiempos_espera = []     
        self.tiempos_sistema = []    
        self.tamanios_cola = []       


    def proceso_cliente(self, env, servidor):

        llegada = env.now


        self.tamanios_cola.append(len(servidor.queue))


        with servidor.request() as req:
            yield req

            espera = env.now - llegada
            self.tiempos_espera.append(espera)

            tiempo_servicio = random.expovariate(self.mu)
            yield env.timeout(tiempo_servicio)

            self.tiempos_sistema.append(env.now - llegada)


    def generador_llegadas(self, env, servidor):
        while True:

            tiempo_entre_llegadas = random.expovariate(self.lambd)
            yield env.timeout(tiempo_entre_llegadas)
            env.process(self.proceso_cliente(env, servidor))

    # --------------------------------------------------------
    # Metodo principal: arranca el entorno y corre la simulacion
    # --------------------------------------------------------
    def ejecutar_simulacion(self):
        # Creamos el entorno de SimPy
        env = simpy.Environment()

        # Creamos un solo servidor (capacidad = 1) -> esto es M/M/1
        servidor = simpy.Resource(env, capacity=1)

        # Arrancamos el generador de llegadas
        env.process(self.generador_llegadas(env, servidor))

        # Corremos la simulacion hasta el tiempo total
        env.run(until=self.tiempo_total)

        return self.obtener_metricas_simuladas()

    # --------------------------------------------------------
    # Calculamos los promedios simulados
    # --------------------------------------------------------
    def obtener_metricas_simuladas(self):
        espera_promedio = 0
        if len(self.tiempos_espera) > 0:
            espera_promedio = sum(self.tiempos_espera) / len(self.tiempos_espera)

        cola_promedio = 0
        if len(self.tamanios_cola) > 0:
            cola_promedio = sum(self.tamanios_cola) / len(self.tamanios_cola)

        sistema_promedio = 0
        if len(self.tiempos_sistema) > 0:
            sistema_promedio = sum(self.tiempos_sistema) / len(self.tiempos_sistema)

        return {
            "espera_promedio": espera_promedio,      
            "cola_promedio": cola_promedio,          
            "sistema_promedio": sistema_promedio,    
            "total_clientes": len(self.tiempos_espera)
        }



if __name__ == "__main__":
    sim = SimulacionMM1(2.0, 3.0, tiempo_total=500)
    resultados = sim.ejecutar_simulacion()
    print("Metricas simuladas:")
    for k, v in resultados.items():
        print(f"  {k} = {v}")