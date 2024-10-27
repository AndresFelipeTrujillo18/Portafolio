
package GestorTelefonico;

import javax.swing.JOptionPane;


public class main {
    
    public static void main(String[] args) {
        GestorContactos gestor = new GestorContactos();
        int op = 0;
        
        while(op!= 6) {
           String input = JOptionPane.showInputDialog(
           null, "-------- Menu de opciones ---------\n"
           
           + "\n1. Agregar contacto"
           + "\n2. Actualizar contacto" 
           + "\n3. Buscar contacto" 
           + "\n4. Eliminar contacto"
           + "\n5. Mostrar lista de contactos"
           + "\n6. Salir del programa"
           + "Seleccione una opción: ", 
                   "Gestion de contactos",
                   JOptionPane.QUESTION_MESSAGE);
           
           if(input == null) {
               break;
           }
           
           if(esNumerico(input)) {
               op = Integer.parseInt(input);
           } else {
               JOptionPane.showMessageDialog(null, "Entrada no válida. Por favor ingrese un numero del 1 al 6");
               continue;
           }
           
           switch(op) {
            case 1:
                String nombre = JOptionPane.showInputDialog("Ingrese el nombre del contacto");
                if(nombre == null || nombre.isEmpty()) {
                    mostrarMensaje("Nombre no puede estar vacio");
                    break;
                }
                String telefono = JOptionPane.showInputDialog("Ingrese el telefono del contacto");
                if(telefono == null || telefono.isEmpty()) {
                    mostrarMensaje("telefono no puede estar vacio");
                    break;
                }
                String email = JOptionPane.showInputDialog("email el telefono del contacto");
                if(email == null || email.isEmpty()) {
                    mostrarMensaje("email no puede estar vacio");
                    break;
                }
                
                gestor.agregarcontacto(new Contacto(nombre,telefono,email));
            case 2:
                String nombreBuscar = JOptionPane.showInputDialog("Ingrese el nombre de la lista");
                if (nombreBuscar == null || nombreBuscar.isEmpty()) {
                    mostrarMensaje("Nombre no puede estar vacio");
                    break;
                }
                
            String nuevonombre = JOptionPane.showInputDialog("Ingrese el nuevo telefono");
                if(nuevonombre == null || nuevonombre.isEmpty()) {
                    mostrarMensaje("Nombre no puede estar vacio");
                    break;
                }                
            String nuevotelefono = JOptionPane.showInputDialog("Ingrese el nuevo telefono");
                if(nuevotelefono == null || nuevotelefono.isEmpty()) {
                    mostrarMensaje("telefono no puede estar vacio");
                    break;
                }
                
            String nuevoemail = JOptionPane.showInputDialog("Ingrese el nuevo telefono");
                if(nuevoemail == null || nuevoemail.isEmpty()) {
                    mostrarMensaje("Email no puede estar vacio");
                    break;
                }
            gestor.actualizarcontacto(nuevonombre, nuevotelefono, nuevoemail);
              
            case 3:
            String nombrebuscar = JOptionPane.showInputDialog("Ingrese el nuevo telefono");
                if(nombrebuscar == null || nombrebuscar.isEmpty()){
                    mostrarMensaje("Nombre no puede estar vacio");
                    break;
                }
                Contacto contactoEncontrado = gestor.buscarcontacto(nombrebuscar);
                if(contactoEncontrado != null) {
                    mostrarMensaje("Contacto encontrado: \n" + contactoEncontrado);
                }else {
                    mostrarMensaje("Contacto no encontrado");
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
