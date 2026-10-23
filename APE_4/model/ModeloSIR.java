package Practica3_MM1.APE_4.model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * Motor de simulación estocástica basada en agentes para un modelo SIR.
 *
 * <p>La simulación avanza en pasos discretos. En cada paso, cada individuo
 * susceptible puede contagiarse al entrar en contacto con algún individuo
 * infectado y cada individuo infectado puede recuperarse. Los cambios se
 * calculan con los estados existentes al inicio del paso y se aplican al
 * final, de modo que los nuevos infectados no transmiten la enfermedad
 * durante el mismo paso.</p>
 *
 * <p>{@code beta} es la probabilidad de transmisión por cada contacto entre
 * un individuo infectado y uno susceptible dentro de un paso. {@code gamma}
 * es la probabilidad de recuperación de un individuo infectado en un paso.
 * Son probabilidades discretas por paso, no tasas continuas equivalentes de
 * forma directa a los parámetros de las ecuaciones diferenciales del modelo
 * SIR.</p>
 */
public class ModeloSIR {

    /** Población total usada por la configuración de la práctica. */
    public static final int POBLACION_POR_DEFECTO = 100;

    /** Número de individuos infectados al inicio de la simulación. */
    public static final int INFECTADOS_INICIALES_POR_DEFECTO = 5;

    /** Probabilidad de transmisión por contacto y por paso. */
    public static final double BETA_POR_DEFECTO = 0.30;

    /** Probabilidad de recuperación por paso. */
    public static final double GAMMA_POR_DEFECTO = 0.10;

    private final List<Individuo> poblacion;
    private final double beta;
    private final double gamma;
    private final Random random;
    private int tiempoActual;

    /**
     * Crea un modelo SIR con la configuración de la práctica y un generador
     * pseudoaleatorio sin semilla fija.
     */
    public ModeloSIR() {
        this(POBLACION_POR_DEFECTO, INFECTADOS_INICIALES_POR_DEFECTO,
                BETA_POR_DEFECTO, GAMMA_POR_DEFECTO, new Random());
    }

    /**
     * Crea un modelo SIR con la configuración de la práctica y una semilla
     * reproducible.
     *
     * @param semilla semilla del generador pseudoaleatorio
     */
    public ModeloSIR(long semilla) {
        this(POBLACION_POR_DEFECTO, INFECTADOS_INICIALES_POR_DEFECTO,
                BETA_POR_DEFECTO, GAMMA_POR_DEFECTO, new Random(semilla));
    }

    /**
     * Crea un modelo SIR con parámetros personalizados y un generador
     * pseudoaleatorio sin semilla fija.
     *
     * @param poblacionTotal      número total de individuos; debe ser positivo
     * @param infectadosIniciales número de infectados al inicio;
     *                            debe estar entre 0 y {@code poblacionTotal}
     * @param beta                probabilidad de transmisión por contacto
     * @param gamma               probabilidad de recuperación por paso
     * @throws IllegalArgumentException si algún parámetro está fuera de rango
     */
    public ModeloSIR(int poblacionTotal, int infectadosIniciales, double beta, double gamma) {
        this(poblacionTotal, infectadosIniciales, beta, gamma, new Random());
    }

    /**
     * Crea un modelo SIR con parámetros personalizados y una semilla
     * reproducible.
     *
     * @param poblacionTotal      número total de individuos; debe ser positivo
     * @param infectadosIniciales número de infectados al inicio;
     *                            debe estar entre 0 y {@code poblacionTotal}
     * @param beta                probabilidad de transmisión por contacto
     * @param gamma               probabilidad de recuperación por paso
     * @param semilla             semilla del generador pseudoaleatorio
     * @throws IllegalArgumentException si algún parámetro está fuera de rango
     */
    public ModeloSIR(int poblacionTotal, int infectadosIniciales, double beta,
            double gamma, long semilla) {
        this(poblacionTotal, infectadosIniciales, beta, gamma, new Random(semilla));
    }

    private ModeloSIR(int poblacionTotal, int infectadosIniciales, double beta,
            double gamma, Random random) {
        validarParametros(poblacionTotal, infectadosIniciales, beta, gamma);

        this.beta = beta;
        this.gamma = gamma;
        this.random = random;
        this.poblacion = new ArrayList<>(poblacionTotal);
        this.tiempoActual = 0;

        for (int i = 0; i < poblacionTotal; i++) {
            Estado estadoInicial = i < infectadosIniciales
                    ? Estado.INFECTADO
                    : Estado.SUSCEPTIBLE;
            poblacion.add(new Individuo(i, estadoInicial));
        }
    }

    /**
     * Ejecuta un paso completo de la simulación de forma estocástica.
     *
     * <p>Primero guarda una copia de los estados y separa a los susceptibles
     * e infectados existentes al inicio. Después evalúa los contagios y las
     * recuperaciones, registra los cambios y finalmente los aplica. El tiempo
     * aumenta exactamente una unidad por llamada.</p>
     */
    public void avanzarPaso() {
        List<Estado> estadosIniciales = new ArrayList<>(poblacion.size());
        List<Integer> indicesSusceptibles = new ArrayList<>();
        List<Integer> indicesInfectados = new ArrayList<>();

        for (int i = 0; i < poblacion.size(); i++) {
            Estado estado = poblacion.get(i).getEstado();
            estadosIniciales.add(estado);

            if (estado == Estado.SUSCEPTIBLE) {
                indicesSusceptibles.add(i);
            } else if (estado == Estado.INFECTADO) {
                indicesInfectados.add(i);
            }
        }

        boolean[] nuevosContagios = new boolean[poblacion.size()];
        for (int indiceSusceptible : indicesSusceptibles) {
            for (int indiceInfectado : indicesInfectados) {
                if (random.nextDouble() < beta) {
                    nuevosContagios[indiceSusceptible] = true;
                    break;
                }
            }
        }

        boolean[] recuperaciones = new boolean[poblacion.size()];
        for (int indiceInfectado : indicesInfectados) {
            if (random.nextDouble() < gamma) {
                recuperaciones[indiceInfectado] = true;
            }
        }

        for (int i = 0; i < poblacion.size(); i++) {
            if (nuevosContagios[i]) {
                poblacion.get(i).setEstado(Estado.INFECTADO);
            } else if (recuperaciones[i]) {
                poblacion.get(i).setEstado(Estado.RECUPERADO);
            }
        }

        tiempoActual++;
    }

    /**
     * Obtiene una fotografía del estado actual de la población.
     *
     * @return resultado con el tiempo actual y los contadores de cada estado
     */
    public Resultado obtenerResultadoActual() {
        int susceptibles = 0;
        int infectados = 0;
        int recuperados = 0;

        for (Individuo individuo : poblacion) {
            switch (individuo.getEstado()) {
                case SUSCEPTIBLE:
                    susceptibles++;
                    break;
                case INFECTADO:
                    infectados++;
                    break;
                case RECUPERADO:
                    recuperados++;
                    break;
                default:
                    throw new IllegalStateException("Estado epidemiológico desconocido.");
            }
        }

        return new Resultado(tiempoActual, susceptibles, infectados, recuperados);
    }

    /**
     * @return paso de simulación actual; comienza en cero
     */
    public int getTiempoActual() {
        return tiempoActual;
    }

    /**
     * @return probabilidad de transmisión por contacto y por paso
     */
    public double getBeta() {
        return beta;
    }

    /**
     * @return probabilidad de recuperación por paso
     */
    public double getGamma() {
        return gamma;
    }

    /**
     * @return número total de individuos de la población
     */
    public int getPoblacionTotal() {
        return poblacion.size();
    }

    private static void validarParametros(int poblacionTotal, int infectadosIniciales,
            double beta, double gamma) {
        if (poblacionTotal <= 0) {
            throw new IllegalArgumentException("La población total debe ser positiva.");
        }
        if (infectadosIniciales < 0 || infectadosIniciales > poblacionTotal) {
            throw new IllegalArgumentException(
                    "La cantidad de infectados iniciales debe estar entre 0 y la población total.");
        }
        if (!Double.isFinite(beta) || beta < 0.0 || beta > 1.0) {
            throw new IllegalArgumentException("Beta debe ser una probabilidad entre 0 y 1.");
        }
        if (!Double.isFinite(gamma) || gamma < 0.0 || gamma > 1.0) {
            throw new IllegalArgumentException("Gamma debe ser una probabilidad entre 0 y 1.");
        }
    }
}
