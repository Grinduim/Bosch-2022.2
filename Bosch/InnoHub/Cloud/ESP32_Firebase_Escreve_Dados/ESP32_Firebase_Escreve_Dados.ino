//Incluindo as bibliotecas do projeto
#include <WiFi.h>
#include <Wire.h>
#include "DHT.h"
#include <Firebase_ESP_Client.h>

//Substituir as informações abaixo com as credencias de acesso do seu roteador
#define WIFI_SSID "Vivo-Internet-BF17"
#define WIFI_PASSWORD "78814222"

// Rede do Celular
// #define WIFI_SSID "SSID"
// #define WIFI_PASSWORD "SENHA"

//Apresenta as informações do processo de geração de token
#include "addons/TokenHelper.h"

//Apresenta informações de impressão de carga útil do Banco de Dados em Tempo Real (RTDB) e outras funções auxiliares
#include "addons/RTDBHelper.h"

//Inserir chave de API do projeto Firebase
#define API_KEY "AIzaSyD_2ELKROPWMNJZk9PbdW0iXuZOcuEwIQ8"

//Inserir URL RTDB
#define DATABASE_URL "https://esp32-firebase-c4892-default-rtdb.firebaseio.com"

//Cria o objeto fbdo do tipo FirebaseData
FirebaseData fbdo;

//Cria o objeto auth do tipo FirebaseAuth
FirebaseAuth auth;

//Cria o objeto config do tipo FirebaseConfig
FirebaseConfig config;


//Variável que registra a última vez que uma mensagem foi publicada
unsigned long ultimoEnvioDeDados = 0;
 
//Variável de contagem que iremos escrever no banco de dados em tempo real para fins de depuração (debug)
int contador = 0;

//Variável para verificar se o ESP32 está conectado ao banco de dados do Firebase
bool signupOK = false;

//Variável para armazenar o intervalo de tempo entre os envios dos dados ao Firebase
const long intervalo = 5000;       


#define ledPin1 13 // Pino 13 conectado no LED externo
#define ledPin2 2  // LED do módulo DOIT ESP32 DEVKIT V1

//Pino GPIO34 (ADC1_CH6) -> usado para ler o valor de tensão analógica sobre o potenciômetro
#define analogPinPotenciometro 34
//Pino GPIO33 (ADC1_CH5) -> usado para ler o valor de tensão analógica sobre o LDR 
#define analogPinLdr           33 

#define DHTPIN 14
#define DHTTYPE DHT11  //DHT 11
// #define DHTTYPE DHT22   //DHT 22 (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);

float umidade;
float temperatura;
float luminosidade;
float potenciometro;


void setup() {

  Serial.begin(115200);
  
  conectaWiFi();

  //Atribui a chave de API Web ao objeto config para acesso ao projeto/aplicação do Firebase 
  config.api_key = API_KEY;

  //Atribui a URL do banco de dados ao objeto config para acesso ao RTDB do projeto/aplicação do Firebase
  config.database_url = DATABASE_URL;
  
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);

  dht.begin();
  
  // Realiza o login na plataforma Firebase
  if(Firebase.signUp(&config, &auth, "", "")){
    Serial.println("Login realizado com sucesso no Firebase");
    signupOK = true;
  }
  //Apresenta a mensagem de erro caso não seja possível realizar o login
  else{
    Serial.printf("%s\n", config.signer.signupError.message.c_str()); 
  }

  //Atribui uma função de retorno de chamada para a tarefa de geração de token de longa duração
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h

  //Inicia a comunicação com a aplicação do Firebase passando as informações de acesso do endereço do objeto config e auth
  Firebase.begin(&config, &auth);
  //Habilita a fução de reconexão
  Firebase.reconnectWiFi(true);
}

void loop(){
    //Realiza as leituras dos sensores DHT, LDR e Potenciômetro
    realizaMedidas();
    
      // A cada intervalo de X segundos (interval0 = 5 segundos)
      //essa rotina enviará mensagens para o banco de dados do Firebase
      if(Firebase.ready() && signupOK && (millis() - ultimoEnvioDeDados >= intervalo)){
    
      // Registra o último valor de tempo que os dados foram enviados para o RTDB do Firebase
      ultimoEnvioDeDados = millis();
    
      //Apresenta os dados na porta serial
      imprimeValoresSerial();

      //Chama a rotina(função) para escrever os dados no Firebase
      escreveDadosFirebase();
      }
}
