#define s0 4
#define s1 5
#define s2 6
#define s3 7
#define salidaTCS 8

int limiteCapturas = 100;  // Establece el límite de capturas deseado
int contadorCapturas = 0;  // Contador para rastrear el número de capturas

// Valores de referencia para calibración
int blancoR = 43;  // Cambia estos valores tras calibrar con un objeto blanco
int blancoG = 47;
int blancoB = 43;

void setup() {
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(salidaTCS, INPUT);

  // Cambia a 100% de escala
  digitalWrite(s0, HIGH);
  digitalWrite(s1, HIGH);

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

    // Normalizar los valores con referencia al blanco
    int normR = map(rojo, 0, blancoR, 0, 255);
    int normG = map(verde, 0, blancoG, 0, 255);
    int normB = map(azul, 0, blancoB, 0, 255);

    // Limitar los valores entre 0 y 255
    normR = constrain(normR, 0, 255);
    normG = constrain(normG, 0, 255);
    normB = constrain(normB, 0, 255);

    // Enviar los valores RGB normalizados al puerto serie
    Serial.print(normR);
    Serial.print(",");
    Serial.print(normG);
    Serial.print(",");
    Serial.println(normB);

    // Incrementa el contador de capturas
    contadorCapturas++;
  } else {
    while (true); // Detener el programa al alcanzar el límite
  }
}
