
package GestionBiblioteca;

import javax.swing.JOptionPane;


public class main {
    
    public static void main(String[] args) {
        GestorBiblioteca gestor = new GestorBiblioteca();
        int op = 0;
        
        while (op!= 7) {
            String input = JOptionPane.showInputDialog(null, "--------Menu de opciones--------\n" 
            + "\n 1.Agregar Libro"
            + "\n2. Buscar libro por titulo" 
            + "\n3. Buscar libro por autor"        
            + "\n4. Actualizar estado"
            + "\n5. Eliminar libro"
            + "\n6. Mostrar libros"
            + "\n7. Salir del programa"
             + "\nSeleccione una opción: ", 
                   "Gestion de biblioteca",
                   JOptionPane.QUESTION_MESSAGE);        
            
            if (input == null) {
                break;
            }
            
            if(esNumerico(input)) {
                op = Integer.parseInt(input);
            } else {
               JOptionPane.showMessageDialog(null, "Entrada no valida. Digite un numero del 1 al 6 ");
               continue;
            }
            
            switch(op) {
                case 1:
                    String nombre = JOptionPane.showInputDialog("Ingrese el nombre del libro");
                    if(nombre == null || nombre.isEmpty()) {
                        mostrarMensaje("Nombre no puede estar vacio");
                        break;
                    }        
                    String autor = JOptionPane.showInputDialog("Ingrese el nombre del autor");
                    if(autor == null || autor.isEmpty()) {
                        mostrarMensaje("Autor no puede estar vacio");
                        break;
                    }
                    String codigobarras = JOptionPane.showInputDialog("Ingrese el ISBN del libro");
                    if(codigobarras == null || codigobarras.isEmpty()) {
                        mostrarMensaje("ISBN no puede estar vacio");
                        break;
                    }

                    
                    gestor.agregarlibro(new Biblioteca(nombre, autor, codigobarras));
                    break;
                case 2:
                String nombreBuscar = JOptionPane.showInputDialog("Ingrese el nombre del libro");
                if (nombreBuscar == null || nombreBuscar.isEmpty()) {
                    mostrarMensaje("Nombre no puede estar vacio");
                    break;
                }
                
                Biblioteca libroencontrado = gestor.buscarlibro(nombreBuscar);
                if(libroencontrado != null) {
                    mostrarMensaje("Libro encontrado: \n " + libroencontrado );
                }else {
                    mostrarMensaje("Libro no encontrado");
                }
                break;
                
                case 3:                 
                String autorBuscar = JOptionPane.showInputDialog("Ingrese el nombre del autor del libro");
                if (autorBuscar == null || autorBuscar.isEmpty()) {
                    mostrarMensaje("Nombre no puede estar vacio");
                    break;
                }
                
                Biblioteca autorencontrado = gestor.buscarautor(autorBuscar);
                if(autorencontrado != null) {
                    mostrarMensaje("Libro encontrado: \n " + autorencontrado );
                }else {
                    mostrarMensaje("Autor no encontrado");
                }
                break;
                
                case 4:
                String libroEstado = JOptionPane.showInputDialog("Ingrese el nombre del libro");
                if (libroEstado == null || libroEstado.isEmpty()) {
                    mostrarMensaje("Nombre del libro no puede estar vacio");
                }
                
                              
                Biblioteca libroestado = gestor.buscarlibro(libroEstado);
                
                String estado = JOptionPane.showInputDialog("Ingrese el estado del libro 1. Disponible a prestado 2. Prestado a Disponible");
                
                if(estado.equalsIgnoreCase("1")) {
                      Biblioteca bi = new Biblioteca();
                    bi.setEstado(estado);
                    
                } 
            }
            
            
            
            
        }
    }
    
    private static void mostrarMensaje(String mensaje) {
        JOptionPane.showMessageDialog(null, mensaje);
    }
    
     private static boolean esNumerico(String str) {
        return str != null && str.matches("\\d+");
    }
}
