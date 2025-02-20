int relayPin = 7;  // Pin donde está conectado el relé que controla el compresor
int intensidad = 0;

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);  // Inicializa la comunicación serial a 9600 baudios
}

void loop() {
  if (Serial.available() > 0) {
    intensidad = Serial.parseInt();  // Lee el valor entero enviado desde la aplicación
    if (intensidad >= 0 && intensidad <= 255) {
      analogWrite(relayPin, intensidad);  // Ajusta la intensidad (PWM) del compresor
    }
  }
}