package model;

/**
 * Representa los posibles estados epidemiológicos de un individuo en el modelo SIR.
 */
public enum Estado {
    /** Individuo sano pero propenso a contraer la enfermedad. */
    SUSCEPTIBLE,
    
    /** Individuo infectado capaz de contagiar la enfermedad a un susceptible. */
    INFECTADO,
    
    /** Individuo recuperado con inmunidad que ya no contagia ni puede ser infectado. */
    RECUPERADO
}