#define s0 4
#define s1 5
#define s2 6
#define s3 7
#define salidaTCS 8

int limiteCapturas = 100;  // Establece el límite de capturas deseado
int contadorCapturas = 0;  // Contador para rastrear el número de capturas

void setup() {
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(salidaTCS, INPUT);

  digitalWrite(s0, HIGH);
  digitalWrite(s1, LOW);

  Serial.begin(9600);
}

void loop() {
  if (contadorCapturas < limiteCapturas) {
    // Rojo
    digitalWrite(s2, LOW);
    digitalWrite(s3, LOW);
    int rojo = pulseIn(salidaTCS, LOW);
    delay(200);

    // Verde
    digitalWrite(s2, HIGH);
    digitalWrite(s3, HIGH);
    int verde = pulseIn(salidaTCS, LOW);
    delay(200);

    // Azul
    digitalWrite(s2, LOW);
    digitalWrite(s3, HIGH);
    int azul = pulseIn(salidaTCS, LOW);
    delay(200);

    // Enviar los valores RGB al puerto serie en formato "R,G,B\n"
    Serial.print(rojo);
    Serial.print(",");
    Serial.print(verde);
    Serial.print(",");
    Serial.println(azul);

    // Incrementa el contador de capturas
    contadorCapturas++;
  } else {
    while (true);
  }
}
