void imprimeStatusLeds(){

   if(statusLed1) Serial.print("LED1: LIGADO");
   else Serial.print("LED1: DESLIGADO");

   if(statusLed2) Serial.println("    LED2: LIGADO");
   else Serial.println("    LED2: DESLIGADO");
}
