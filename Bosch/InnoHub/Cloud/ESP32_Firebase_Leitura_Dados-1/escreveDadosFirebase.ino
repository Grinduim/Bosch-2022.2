void escreveDadosFirebase(){
   if(Firebase.RTDB.setInt(&fbdo, "esp32/contagem", contador))             Serial.println("contador Ok");
   else Serial.println("Erro: " + fbdo.errorReason());
   
   if(Firebase.RTDB.setFloat(&fbdo, "esp32/umidade", umidade))             Serial.println("umidade Ok");
   else Serial.println("Erro: " + fbdo.errorReason());
     
   if(Firebase.RTDB.setFloat(&fbdo, "esp32/temperatura", temperatura))     Serial.println("temperatura Ok");
   else Serial.println("Erro: " + fbdo.errorReason());
   
   if(Firebase.RTDB.setFloat(&fbdo, "esp32/luminosidade", luminosidade))   Serial.println("luminosidade Ok");
   else Serial.println("Erro: " + fbdo.errorReason());
   
   if(Firebase.RTDB.setFloat(&fbdo, "esp32/potenciometro", potenciometro)) Serial.println("potenciometro Ok");
   else Serial.println("Erro: " + fbdo.errorReason());

   contador++;
   Serial.println();
}
