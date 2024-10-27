
package Cola;


public class Cliente {
    
    private String nombre;
    private String metodo;

    public Cliente(String nombre, String metodo) {
        this.nombre = nombre;
        this.metodo = metodo;
    }
    
    public String getNombre() {
        return nombre;
    }

    public String getMetodo() {
        return metodo;
    }

    @Override
    public String toString() {
        return "nombre: " + nombre + ", metodo: " + metodo;
    }
    
    
}
