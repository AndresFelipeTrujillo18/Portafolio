
package GestionBiblioteca;


public class Biblioteca {
    
    private String nombrelibro;
    private String autorlibro;
    private String codigobarras;
    private String Estado;

    public Biblioteca() {
    }
    
    

    public Biblioteca(String nombrelibro, String autorlibro, String codigobarras) {
        this.nombrelibro = nombrelibro;
        this.autorlibro = autorlibro;
        this.codigobarras = codigobarras;
        this.Estado = "Disponible";
    }

    public String getNombrelibro() {
        return nombrelibro;
    }

    public void setNombrelibro(String nombrelibro) {
        this.nombrelibro = nombrelibro;
    }

    public String getAutorlibro() {
        return autorlibro;
    }

    public void setAutorlibro(String autorlibro) {
        this.autorlibro = autorlibro;
    }

    public String getCodigobarras() {
        return codigobarras;
    }

    public void setCodigobarras(String codigobarras) {
        this.codigobarras = codigobarras;
    }

    public String isEstado() {
        return Estado;
    }

    public void setEstado(String Estado) {
        this.Estado = "Prestado";
    }

    @Override
    public String toString() {
        return "Biblioteca{" + "nombrelibro=" + nombrelibro + ", autorlibro=" + autorlibro + ", codigobarras=" + codigobarras + ", Estado=" + Estado + '}';
    }

    public String getEstado() {
        return Estado;
    }
    
    
}


