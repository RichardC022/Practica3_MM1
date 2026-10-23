package Practica3_MM1.APE_4.model;

/**
 * Estados epidemiológicos posibles de un individuo dentro del modelo SIR.
 */
public enum Estado {

    /** El individuo puede contraer la enfermedad. */
    SUSCEPTIBLE,

    /** El individuo está infectado y puede transmitir la enfermedad. */
    INFECTADO,

    /** El individuo ya superó la enfermedad y no vuelve a ser susceptible. */
    RECUPERADO
}
