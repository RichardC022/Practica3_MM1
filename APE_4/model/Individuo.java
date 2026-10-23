package Practica3_MM1.APE_4.model;

/**
 * Representa a una persona dentro de la población simulada.
 * Cada individuo tiene un identificador inmutable y un estado epidemiológico.
 */
public class Individuo {

    private final int id;
    private Estado estado;

    /**
     * Crea un individuo con el identificador y estado inicial indicados.
     *
     * @param id            identificador único e inmutable del individuo
     * @param estadoInicial estado epidemiológico inicial
     * @throws IllegalArgumentException si {@code estadoInicial} es {@code null}
     */
    public Individuo(int id, Estado estadoInicial) {
        if (estadoInicial == null) {
            throw new IllegalArgumentException("El estado inicial no puede ser null.");
        }
        this.id = id;
        this.estado = estadoInicial;
    }

    /**
     * @return identificador único del individuo
     */
    public int getId() {
        return id;
    }

    /**
     * @return estado epidemiológico actual del individuo
     */
    public Estado getEstado() {
        return estado;
    }

    /**
     * Actualiza el estado epidemiológico del individuo.
     *
     * @param nuevoEstado nuevo estado; no puede ser {@code null}
     * @throws IllegalArgumentException si {@code nuevoEstado} es {@code null}
     */
    public void setEstado(Estado nuevoEstado) {
        if (nuevoEstado == null) {
            throw new IllegalArgumentException("El nuevo estado no puede ser null.");
        }
        this.estado = nuevoEstado;
    }
}
