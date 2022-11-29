void realizaMedidas(){

  umidade = dht.readHumidity();

  temperatura = dht.readTemperature();


  if(isnan(umidade) || isnan(temperatura)){
    Serial.println("Falha na leitura do sensor DHT!");
    return;
  }

  luminosidade = 100.0 * (analogRead(analogPinLdr)) / 4095;

  potenciometro = 3.3 * (analogRead(analogPinPotenciometro)) / 4095;
  
}