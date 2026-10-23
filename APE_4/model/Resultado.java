package Practica3_MM1.APE_4.model;

/**
 * Fotografía inmutable de la población en un instante de la simulación.
 * Contiene el tiempo transcurrido y el número de individuos en cada estado.
 */
public final class Resultado {

    private final int tiempo;
    private final int susceptibles;
    private final int infectados;
    private final int recuperados;

    /**
     * Crea un resultado con los valores indicados.
     *
     * @param tiempo       paso de simulación
     * @param susceptibles número de individuos susceptibles
     * @param infectados   número de individuos infectados
     * @param recuperados  número de individuos recuperados
     * @throws IllegalArgumentException si algún contador es negativo
     */
    public Resultado(int tiempo, int susceptibles, int infectados, int recuperados) {
        if (tiempo < 0) {
            throw new IllegalArgumentException("El tiempo no puede ser negativo.");
        }
        if (susceptibles < 0 || infectados < 0 || recuperados < 0) {
            throw new IllegalArgumentException("Los contadores de estados no pueden ser negativos.");
        }
        this.tiempo = tiempo;
        this.susceptibles = susceptibles;
        this.infectados = infectados;
        this.recuperados = recuperados;
    }

    /**
     * @return paso de simulación al que corresponde este resultado
     */
    public int getTiempo() {
        return tiempo;
    }

    /**
     * @return número de individuos susceptibles
     */
    public int getSusceptibles() {
        return susceptibles;
    }

    /**
     * @return número de individuos infectados
     */
    public int getInfectados() {
        return infectados;
    }

    /**
     * @return número de individuos recuperados
     */
    public int getRecuperados() {
        return recuperados;
    }
}
