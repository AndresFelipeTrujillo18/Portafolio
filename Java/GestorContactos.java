
package GestorTelefonico;

import java.util.ArrayList;



public class GestorContactos {
    
    private ArrayList<Contacto> ListaContacto ;
    
    public GestorContactos() {
    
        ListaContacto = new ArrayList<>();
}
    
    public void agregarcontacto(Contacto contacto) {
        
        ListaContacto.add(contacto);
        mostrarinfo("Contacto agregado exitosamente");
    }
    
    private void mostrarinfo (String mensaje) {
        javax.swing.JOptionPane.showMessageDialog(null, mensaje);
        
    }
    
    public Contacto buscarcontacto(String nombre) {
        for(Contacto contacto : ListaContacto) {
            if (contacto.getNombre().equals(nombre)) {
                return contacto;
            }
        } 
        
        return null; 
    }
    
    public boolean eliminarcontacto(String nombre) {
        Contacto contacto = buscarcontacto(nombre);
        if(contacto != null) {
            ListaContacto.remove(contacto);
            mostrarinfo("Contacto eliminado exitosamente");
            return true;
        } else {
            mostrarinfo("Contacto no encontrado");
            return false;
        }
    }
    
    public boolean actualizarcontacto(String nombre, String ntelefono, String nemail) {
        Contacto contacto = buscarcontacto(nombre);
        if(contacto != null) {
            contacto.setTelefono(ntelefono);
            contacto.setEmail(nemail);
            mostrarinfo("Contacto actualizado correctamente");
            return true;
        } else {
            mostrarinfo("Contacto no encontrado");
            return false;
        }
    }
    
    public void mostrarcontacto(String nombre) {
        Contacto contacto = buscarcontacto(nombre);
        if(contacto.isEmpty())  {
            mostrarinfo("La lista se encuentra vacia");
        }else {
            StringBuilder contactos = new StringBuilder();
            for(Contacto cont : ListaContacto) {
                contactos.append(cont).append("\n");

            }
            mostrarinfo(contactos.toString());    
        }
    }

}
