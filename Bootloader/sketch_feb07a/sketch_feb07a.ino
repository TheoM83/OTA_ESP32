#include <WiFi.h>
#include <Update.h>
#include <string.h>
#include <iostream>
#include <Crypto.h>
#include <AES.h>
#include <string.h>

//REMOTE PYTHON SERVER
const char * host = "192.168.1.14";
const uint16_t port = 8090;

//DEVICE INFORMATIONS
String ID = WiFi.macAddress();
String Name = "device-TEST";
String Version = "1";

//WIFI INFORMATIONS
const char* ssid = "Livebox-3f60";
const char* password =  "AA7CAD6FED74FAC79D3ED4E3C2";

//AES KEY
byte key[32] = {0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78};
String padding_character = "/";

//VARIABLES
AES128 aes128;
byte buffer[256];
byte cipher_buffer[256];
byte buffer_tmp[17];

//FUNCTIONS

void WifiConnect(){
  Serial.begin(115200);
  Serial.println("My mac address : "+String(ID)+'\n');
  WiFi.begin(ssid, password);
  Serial.println("Connecting to "+String(ssid)+'\n');
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.print(".");
  }
  Serial.print('\n');
  Serial.print("Connected as : ");
  Serial.println(WiFi.localIP());
}

void OTA()
{
  WiFiClient client;
  if (!client.connect(host, port)) 
  {
    Serial.println("Connection to host failed");
    delay(1000);
  }
  else
  {
      aes128.setKey(key, aes128.keySize());
      //Sending device information
      Serial.println("Connected to "+String(host));
      Serial.println("Sending information");

      //Prepare Message
      String message = ""+ID+"~"+Name+"~"+Version;
      while (message.length()%16 != 0)
      {message = message + padding_character;}
      message.getBytes(buffer, message.length()+1);

      for (int i = 0; i < message.length(); i=i+16){
        for (int j = 0 ; j < 16 ; j++){
          buffer_tmp[j] = buffer[i+j];
        }
        aes128.encryptBlock(buffer_tmp, buffer_tmp);
        for (int j = 0 ; j < 16 ; j++){
          cipher_buffer[i+j] = buffer_tmp[j];
        }
      }
      client.println((char*) cipher_buffer);
            
      delay(400);

      //Receiving update information
      Serial.println("Checking Firmware");
      String stringFileSize = client.readStringUntil('\n');
      Serial.println(stringFileSize);

      //Starting the update
      
      int fileSize = atoi(stringFileSize.c_str());
      bool start = Update.begin(fileSize);
      if (start) {
      Serial.println("Downloading and applying OTA update...");
      size_t written = Update.writeStream(client);

      if (written == fileSize) 
      {
        Serial.println("Written : " + String(written) + " successfully");
      } else {
        Serial.println("Written only : " + String(written) + "/" + String(fileSize) + ". Retry?" );
      }
      if (Update.end()) 
      {
        Serial.println("Update finished!");
        if (Update.isFinished()) 
        {
          Serial.println("Rebooting.");
          ESP.restart();
        } 
        else 
        {
          Serial.println("Error...");
        }
      } 
      else 
      {
        Serial.println("Error...");
      }
    } 
    else
    {
      Serial.println("No firmware");
    }
     
    client.flush();  
  }
}

void setup()
{
  WifiConnect();
  OTA();
  //...
}
 
void loop()
{
  //...
}
