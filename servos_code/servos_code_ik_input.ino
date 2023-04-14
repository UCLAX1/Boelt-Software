#include <Servo.h>
#include "leg.h"

Servo legFL;
Servo legFR;
Servo legBL;
Servo legBR;
Servo hiplegFL;
Servo hiplegFR;
Servo hiplegBL;
Servo hiplegBR;
Servo hipFL;
Servo hipFR;
Servo hipBL;
Servo hipBR;
Servo spineF;
Servo spineB;

Servo servos[] = {legFL, legFR, legBL, legBR, hiplegFL, hiplegFR, hiplegBL, hiplegBR, hipFL, hipFR, hipBL, hipBR, spineF, spineB};
// int servos_size = sizeof(servos)/sizeof(servos[0]);
int servos_size = 14;
int servo_pins[] = {0, 6, 0, 0, 0, 8, 0, 0, 0, 7, 0, 0, 0, 0};
int default_pos[] = {0, 85, 0, 0, 0, 100, 0, 0, 0, 115, 0, 0, 0, 0};
/*
pin 2
pin 3
pin 4
pin 5
pin 6 leg FR
pin 7 hip FR
pin 8 hiplegFR
 */

int input;
int off1 = 85;  // leg FR
int off2 = 100; // leghip FR
int off3 = 115; // hip FR
float data[4] = {0.0, 0.0, 0.0, 0.0};

Leg LegFR(&servos[9], &servos[5], &servos[1], 115, 100, 85);

void setup()
{
    for (int i = 0; i < servos_size; i++)
    {
        servos[i].write(default_pos[i]);
        servos[i].attach(servo_pins[i]);
        delay(15);
    }

    /*servos[0].attach(2);
    servos[2].attach(7);
    servos[1].attach(7);*/
    Serial.begin(9600);
    /*servos[0].write(off1);
    servos[1].write(off2 + 85.664);
    servos[2].write(off3-22.5);*/
}

void readFloatArray(float *data)
{
    uint8_t buffer[sizeof(float) * 4];

    // Wait until a complete binary data packet is available
    while (Serial.available() < sizeof(buffer))
    {
        delay(1);
    }

    // Read the binary data into a buffer
    Serial.readBytes(buffer, sizeof(buffer));

    // Unpack the binary data into an array of four floats
    for (int i = 0; i < 4; i++)
    {
        memcpy(&data[i], &buffer[i * sizeof(float)], sizeof(float));
    }
}

void loop()
{
    if (Serial.available() > 0)
    {
        readFloatArray(data);
        Serial.flush();
        Serial.println(data[0]);
        Serial.println(data[1]);
        Serial.println(data[2]);
        Serial.println(data[3]);
    }

    Serial.print("Data 3: ");
    Serial.println(data[3]);
    float angles[] = {data[1], data[2], data[3]};
    LegFR.move(angles);
    // servos[9].write(input);

    delay(150);
}