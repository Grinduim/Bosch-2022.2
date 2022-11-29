//Incluindo as bibliotecas do projeto
#include <WiFi.h>
#include <Firebase_ESP_Client.h>


//Substituir as informações abaixo com as credencias de acesso do seu roteador
// #define WIFI_SSID "OI-FIBRA"
// #define WIFI_PASSWORD "Vi&Ana122"

// Rede do Celular
// #define WIFI_SSID "SSID"
// #define WIFI_PASSWORD "SENHA"

//Apresenta as informações do processo de geração de token
#include "addons/TokenHelper.h"

//Apresenta informações de impressão de carga útil do Banco de Dados em Tempo Real (RTDB) e outras funções auxiliares
#include "addons/RTDBHelper.h"

//Inserir chave de API do projeto Firebase
#define API_KEY "AIzaSyALmts9w2wF1IjV4TydYQaE_lPfL63EVBQ"

//Inserir URL RTDB
#define DATABASE_URL "https://esp32-firebase-7179f-default-rtdb.firebaseio.com/"

//Cria o objeto fbdo do tipo FirebaseData
FirebaseData fbdo;

//Cria o objeto auth do tipo FirebaseAuth
FirebaseAuth auth;

//Cria o objeto config do tipo FirebaseConfig
FirebaseConfig config;

//Variável que registra a última vez que uma mensagem foi lida
unsigned long ultimaLeitura = 0;

//Variável para armazenar o intervalo de tempo entre leituras dos dados do Firebase
const long intervalo = 5000;  

//Variável para verificar se o ESP32 está conectado ao banco de dados do Firebase
bool signupOK = false;
    

#define ledPin1 13 // Pino 13 conectado no LED
#define ledPin2 2  // LED do módulo DOIT ESP32 DEVKIT V1


bool statusLed1 = 0;
bool statusLed2 = 0;

void setup() {

  Serial.begin(115200);
  
  conectaWiFi();

 //Atribui a chave de API Web ao objeto config para acesso ao projeto/aplicação do Firebase 
  config.api_key = API_KEY;

  //Atribui a URL do banco de dados ao objeto config para acesso ao RTDB do projeto/aplicação do Firebase
  config.database_url = DATABASE_URL;
  
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);

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
 
      // A cada intervalo de X segundos (intervalo = 5 segundos)
      //essa rotina lerá mensagens do banco de dados do Firebase
      if(Firebase.ready() && signupOK && (millis() - ultimaLeitura >= intervalo)){
    
      // Registra o último valor de tempo que os dados foram enviados para o RTDB do Firebase
      ultimaLeitura = millis();
    
      //Chama a rotina(função) para ler os dados no Firebase
      leDadosFirebase();
      
      imprimeStatusLeds();  
      }
}
