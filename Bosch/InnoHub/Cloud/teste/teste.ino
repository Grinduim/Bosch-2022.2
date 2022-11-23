#define LED  13
#define POT 34
#define DHPIN 14
#define DHTTYPE DHT11

#include <WiFi.h>
#include "DHT.h"

const char* ssid = "Vivo-Internet-BF17";
const char* password = "78814222";

DHT dht(DHPIN,DHTTYPE);

float temp;
float humi;



void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid,password);

  while( WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.println("Conecting to wifi");
  }
  
  Serial.println("Conected");

  dht.begin();

}

void loop() {
  humi = dht.readHumidity();
  temp = dht.readTemperature();
  Serial.println("\t: ");
  Serial.print("Temperatura: ");
  Serial.print(temp);
  Serial.println("\t: ");
  Serial.print("Humidade:");
  Serial.print(humi);
  

}
