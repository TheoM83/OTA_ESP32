#include <WiFi.h>
 
const char* ssid = "";
const char* password =  "";

const uint16_t port = 8090;
const char * host = "192.168.1.25";

//DEVICE INFORMATIONS
const char* ID = "UID123";
const char* Name = "device-TEST";
const char* Version = "1";

void setup()
{
  //Connect to the Wifi
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.println("///Connecting to the Wifi///");
  }
  Serial.print("  --> Connected as : ");
  Serial.println(WiFi.localIP());

  //Connect to the Server
  WiFiClient client;
    
    if (!client.connect(host, port)) 
    {
      Serial.println("Connection to host failed");
      delay(1000);
    }
    else
    {
      Serial.println("Connected to server successful!");
      Serial.println("Sending information");
      client.print(ID);
      delay(50);
      client.print(Name);
      delay(50);
      client.print(Version);
      delay(50);
      client.stop();
     }
}
 
void loop()
{

}
