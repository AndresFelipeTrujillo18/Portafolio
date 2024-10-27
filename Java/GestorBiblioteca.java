
package GestionBiblioteca;

import java.util.ArrayList;


public class GestorBiblioteca {
    
    
    private ArrayList<Biblioteca> ListaBiblioteca ;
    
    public GestorBiblioteca() {
        
        ListaBiblioteca = new ArrayList<>();
    }
    
    public void agregarlibro(Biblioteca biblioteca) {
        ListaBiblioteca.add(biblioteca);
        mostrarinfo("Información agregado correctamente");
    }
    
    private void mostrarinfo (String mensaje) {
        javax.swing.JOptionPane.showMessageDialog(null, mensaje);
    }
    
    public Biblioteca buscarlibro (String nomlibro) {
        for(Biblioteca biblioteca : ListaBiblioteca) {
            if (biblioteca.getNombrelibro().equals(nomlibro)) {
                return biblioteca;
            }
        }
        return null;
    }
    
        public Biblioteca buscarautor (String nomautor) {
        for(Biblioteca biblioteca : ListaBiblioteca) {
            if (biblioteca.getAutorlibro().equals(nomautor)) {
                return biblioteca;
            }
        }
        return null;
    }
    
    public String actualizarlibro(String nomlibro, String nEstado) {
        Biblioteca biblioteca = buscarlibro(nomlibro);
        
        if (biblioteca != null) {
            biblioteca.setEstado(nEstado);
            mostrarinfo("Estado del libro actualizado correctamente");
;
        } else {
            mostrarinfo("Libro no encontrado");

        }
        return null;
    }
    
    public boolean eliminarlibro(String nomlibro) {
        Biblioteca biblioteca = buscarlibro(nomlibro);
        if (biblioteca != null) {
            ListaBiblioteca.remove(biblioteca);
            mostrarinfo("Libro eliminado del sistema correctamente");
            return true;
        }else {
            mostrarinfo("Libro no encontrado en el sistema");
            return false;
        }
    }
    
    public void mostrarlibros (String nomlibro) {
        if(ListaBiblioteca.isEmpty()) {
            mostrarinfo("La lista se encuentra vacia");
        } else {
            StringBuilder bibliotecas = new StringBuilder();
            
            for (Biblioteca cont : ListaBiblioteca) {
                bibliotecas.append(cont).append(("\n"));
            }
            mostrarinfo(bibliotecas.toString());
        }
    }
}
