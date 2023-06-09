#include <Servo.h>
#include "leg.h"

// servos array
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

Servo servos[] = {
  legFL, hiplegFL, hipFL, 
  legFR, hiplegFR, hipFR, 
  legBL, hiplegBL, hipBL, 
  legBR, hiplegBR, hipBR
};
int servos_size = 12;

// servo pins
/*
index name pin #
0 legFL pin 5
1 hiplegFL pin 4
2 hipFL pin 3
3 leg FR pin 6
4 hiplegFR pin 8
5 hip FR pin 7
6 legBL pin 12
7 hiplegBL pin 24
8 hipBL pin 25
9 legBR pin 36
10 hiplegBR pin 29
11 hipBR pin 28
*/

int servo_pins[] = {
// leg thigh hip
    5,  4,   3,  //FL
    6,  8,   7,  //FR
    12, 24,  25, //BL
    36, 29,  28  //BR
    };

// servo default positions (offsets)
int default_pos[] = {
// leg thigh hip
    88, 118, 85, //FL
    90, 106, 65, //FR
    102, 83, 99, //BL
    99, 90, 88  //BR
    };

int current_pos[] = {
// leg thigh hip
    90, 90, 85, //FL
    90, 90, 82, //FR
    90, 90, 99, //BL
    90, 90, 88  //BR
    };

int motor = 6;

void setup()
{
  for (int i = 0; i < servos_size; i++)
  {
    servos[i].write(default_pos[i]);
    servos[i].attach(servo_pins[i]);
    servos[i].write(default_pos[i]);

    delay(15);
  }
  Serial.begin(9600);
}

void loop()
{
  char input = 'p';
  if (Serial.available() > 0)
  {
    input = Serial.read();
  }

  switch (input) {
    case 'w':
      current_pos[motor] += 1;
      break;
    case 's':
      current_pos[motor] -= 1;
      break;
    case 'n':
      Serial.print("motor ");
      Serial.print(motor);
      Serial.print(" = ");
      Serial.println(current_pos[motor]);
      Serial.println("next motor selected");
      motor += 1;
      break;
  }

    for (int i = 0; i < servos_size; i++) {
    servos[i].write(current_pos[i]);
    delay(15); 
    }
}

