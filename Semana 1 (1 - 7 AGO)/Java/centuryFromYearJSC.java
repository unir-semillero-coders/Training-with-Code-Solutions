package CodeWars.Century_from_year;
import java.util.Scanner;

/* REQUERIMIENTOS
Introduction
The first century spans from the year 1 up to and including the 
year 100, the second century - from the year 101 up to and including 
the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
*/


public class centuryFromYear {
    
    public static void main(String[] args){
        Scanner myScan= new Scanner(System.in);
        int ano;
        int Siglo;
        
        System.out.println("Ingrese un año: ");
        ano= myScan.nextInt();
        Siglo= (ano+99)/100;
        
        System.out.println("El año: " + ano + " Pertenece al Siglo: " + Siglo);
    }
}
