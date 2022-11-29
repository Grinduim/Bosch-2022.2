void leDadosFirebase(){ 
   if(Firebase.RTDB.getString(&fbdo, "leds/led1")){
       
       if(fbdo.stringData() == "L") statusLed1 = 1; 
       if(fbdo.stringData() == "D") statusLed1 = 0;
       digitalWrite(ledPin1, statusLed1);     
   }
   else Serial.println("Erro: " + fbdo.errorReason());

   if(Firebase.RTDB.getString(&fbdo, "leds/led2")){
       
       if(fbdo.stringData() == "L") statusLed2 = 1; 
       if(fbdo.stringData() == "D") statusLed2 = 0;
       digitalWrite(ledPin2, statusLed2);          
   }
   else Serial.println("Erro: " + fbdo.errorReason());
}
