
package Cola;

import java.util.LinkedList;
import java.util.Queue;
import javax.swing.JOptionPane;


public class SistemaAtencionCliente {
    static Queue<Cliente> cola = new LinkedList<>();
    
    public static void agregarCliente(Queue<Cliente> cola) {
        String nombre = JOptionPane.showInputDialog("Ingrese el nombre del cliente");
        String motivo = JOptionPane.showInputDialog("Ingrese el motivo");
        
        Cliente nuevoCliente = new Cliente(nombre, motivo);
        cola.offer(nuevoCliente);
        JOptionPane.showMessageDialog(null, "Agregado correctamente");
    }
    
    public static Cliente atenderCliente(Queue<Cliente> cola) {
        if(!cola.isEmpty()) {
            Cliente clienteAtendido = cola.poll();
            JOptionPane.showMessageDialog(null, "Atendido a: \n " + clienteAtendido); 
            return clienteAtendido;
        } else{ 
            JOptionPane.showMessageDialog(null, "No hay informacion");
        }
        return null;
    }
    
    public static void mostrarClienteEnEspera(Queue<Cliente>cola) {
        if(!cola.isEmpty()) {
            StringBuilder sb = new StringBuilder();
            sb.append("Clientes en espera: \n" );
            
            int numero = 1;
            
            for(Cliente cliente : cola) {
                sb.append(numero).append(". ").append(cliente).append("\n");
                numero++;
            }
            JOptionPane.showMessageDialog(null, sb.toString());
        }else {
            JOptionPane.showMessageDialog(null, "La cola se encuentra vacia");
        }
    }
    
    public static void main(String[] args) {
        Cliente cliente = null;
        
        int op;
        do {
            op = Integer.parseInt(JOptionPane.showInputDialog("==== Menu de clientes ==== \n"
            + "1. Agregar cliente\n"
            + "2. Atender cliente\n"
            + "3. Mostrar cola de clientes\n"
            + "4. Salir del programa"));
            
            switch(op) {
                case 1: 
                    agregarCliente(cola);
                    break;
                case 2:
                    atenderCliente(cola);
                    break;
                case 3:
                    mostrarClienteEnEspera(cola);
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null, "Saliendo del programa");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opcion no valida");
                    break;
            }            
        }while(op!= 4);
    }
}
