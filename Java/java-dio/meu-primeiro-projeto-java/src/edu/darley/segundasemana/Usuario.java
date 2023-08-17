package edu.darley.segundasemana;

public class Usuario {
    public static void main(String[] args) throws Exception {
      
        SmartTv smartTv = new SmartTv();

        System.out.println("Volume atual? " + SmartTv.volume);
        smartTv.diminuirVolume();
        smartTv.diminuirVolume();
        smartTv.diminuirVolume();
        smartTv.aumentarVolume();
        System.out.println("Volume atual? " + SmartTv.volume);


        System.out.println("TV ligada? " + SmartTv.ligada);
        System.out.println("Canal atual? " + SmartTv.canal);
        System.out.println("Volume atual? " + SmartTv.volume);


        smartTv.ligar();
        System.out.println("Novo status -> Tv ligada? " +SmartTv.ligada);

        smartTv.desligar();
        System.out.println("Novo status -> Tv ligada? " +SmartTv.ligada);
    }
    
}
