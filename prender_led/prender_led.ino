int led=13;
int estado;
void setup()
{
  Serial.begin(9600);
  pinMode (led, OUTPUT);
}

void loop()
{
  if(Serial.available())
  {
    estado=Serial.read();
  }

  if(estado=='1')
  {
      digitalWrite(led,1);
  }

  else if(estado=='2')
  {
    digitalWrite(led,0);
  }
  
}
