package edu.darley.segundasemana;

public class SmartTv {
    static boolean ligada=false;
    static int canal=1;
    static int volume=25;

    public void aumentarVolume(){
        volume++;
    }

    public void diminuirVolume(){
        volume--;
    }

    public void ligar(){
        ligada=true;
    }
    public void desligar(){
        ligada=false;
    }

}

