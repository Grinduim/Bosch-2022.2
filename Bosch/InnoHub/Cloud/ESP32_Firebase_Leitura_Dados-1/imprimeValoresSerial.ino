void imprimeValoresSerial(){
  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.println("%");

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println("ºC");
  
  Serial.print("Luminosidade: ");
  Serial.print(luminosidade);
  Serial.println("%");
  
  Serial.print("Potenciômetro: ");
  Serial.print(potenciometro);
  Serial.println("V");
  Serial.println();
}
