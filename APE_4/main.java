package Practica3_MM1.APE_4;

import controller.ControladorSimulacion;

/**
 * Punto de entrada principal de la aplicación.
 * Instancia y arranca el controlador con los requerimientos exactos de la práctica.
 */
public class Main {
    public static void main(String[] args) {
        // Parámetros definidos en la guía académica:
        int poblacionTotal = 100;
        int infectadosIniciales = 5;
        double beta = 0.30;
        double gamma = 0.10;
        int pasosSimulacion = 100;

        // Iniciar el flujo MVC
        ControladorSimulacion controlador = new ControladorSimulacion(
                poblacionTotal, 
                infectadosIniciales, 
                beta, 
                gamma, 
                pasosSimulacion
        );
        
        controlador.ejecutar();
    }
}
