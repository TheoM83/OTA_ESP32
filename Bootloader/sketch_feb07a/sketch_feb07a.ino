#include <WiFi.h>
#include <Update.h>
#include <string.h>
#include <iostream>

//DEVICE INFORMATIONS
String ID = WiFi.macAddress();
String Name = "device-TEST";
String Version = "1";

//REMOTE SERVER
const char * host = "192.168.1.27";
const uint16_t port = 8090;

//WIFI INFORMATIONS
const char* ssid = "SFR_1508";
const char* password =  "shraidhagrodwermiof4";


//FUNCTIONS

void WifiConnect(){
  Serial.begin(115200);
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
      //Sending device information
      Serial.println("Connected to "+String(host));
      Serial.println("Sending information");
      client.println(ID+"~"+Name+"~"+Version);
      delay(200);

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
      Serial.println("Not enough memory");
      client.flush();
    }
  }
}

void setup()
{
  //Connect to the Wifi
  WifiConnect();
  //Performing OTA
  OTA();
}
 
void loop()
{

}
