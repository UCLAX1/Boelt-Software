#include <Servo.h>
#include "leg.h"

//servos array
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

Servo servos[] = {legFL, hiplegFL, hipFL, legFR, hiplegFR, hipFR, legBL, hiplegBL, hipBL, legBR, hiplegBR, hipBR, spineF, spineB};
int servos_size = 14;

//servo pins
/*
index name pin #
0 legFL pin 5
1 hiplegFL pin 4
2 hipFL pin 3
3 leg FR pin 6
4 hiplegFR pin 8
5 hip FR pin 7
6 legBL pin 12
7 hiplegBL pin 25
8 hipBL pin 24
9 legBR pin 36
10 hiplegBR pin 29
11 hipBR pin 28
12 spineF pin 9
13 spineB pin 37
*/
// trying swap of pins and default for 7 and 8
int servo_pins[] = {5, 4, 3, 6, 8, 7, 12, 24, 25, 36, 29, 28};
//servo default positions (offsets)

//FL, FR, BL, BR
// leg, hipleg, hip
//int default_pos[] = {
//125, 148, 135, 
//55, 45, 5, 
//120, 170, 126, 
//130, 103, 70  , 
//80, 100
//};

//int default_pos[] = {
//84, 82, 85, 
//90, 90, 90, 
//90, 90, 90, 
//90, 90, 90
//};

int default_pos[] = {
// leg thigh hip
    84, 82,  85, //FL
    89, 112, 82, //FR
    101, 74, 99, //BL
    95, 101, 88  //BR
    };
//initialize legs
Leg LegFL(1, &servos[0], &servos[1], &servos[2], default_pos[0], default_pos[1], default_pos[2]);
Leg LegFR(0, &servos[3], &servos[4], &servos[5], default_pos[3], default_pos[4], default_pos[5]);
Leg LegBL(2, &servos[6], &servos[7], &servos[8], default_pos[6], default_pos[7], default_pos[8]);
Leg LegBR(3, &servos[9], &servos[10], &servos[11], default_pos[9], default_pos[10], default_pos[11]);

float zeroes[] = {0.0,0.0,0.0};

//initialize spine?
//int spineF_pos = default_pos[12];
//int spineB_pos = default_pos[13];


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
int off1 = 85; //leg FR
int off2 = 100; //leghip FR
int off3 = 115; //hip FR
float data[4] = {0}; // Change 4 to 16 for all values


 
void setup() 
{ 
  for (int i = 0; i < servos_size; i++) 
  {
    servos[i].write(default_pos[i]);
    servos[i].attach(servo_pins[i]);
    servos[i].write(default_pos[i]);

    delay(15); 
  }
  

  /*servos[0].attach(2);
  servos[2].attach(7);
  servos[1].attach(7);*/
  Serial.begin(115200);
  /*servos[0].write(off1);   
  servos[1].write(off2 + 85.664);
  servos[2].write(off3-22.5);*/

  

} 


void readFloatArray(float* data) {
  uint8_t buffer[sizeof(float) * 4]; // Change to 16 for all values

  // Wait until a complete binary data packet is available
  while (Serial.available() < sizeof(buffer)) {
    delay(1);
  }

  // Read the binary data into a buffer
  Serial.readBytes(buffer, sizeof(buffer));

  // Unpack the binary data into an array of four floats
  for (int i = 0; i < 4; i++) { // Change 4 to 16 for all values
    memcpy(&data[i], &buffer[i * sizeof(float)], sizeof(float));
  }
  
}

void loop() {
  if (Serial.available() > 0) {
  readFloatArray(data);
  Serial.flush();
//  Serial.println(data[0]);
//  Serial.println(data[1]);
//  Serial.println(data[2]);
//  Serial.println(data[3]);
//  Serial.println(data[4]);
//  Serial.println(data[3]);
//  Serial.println(data[15]);
  

//Serial.print("Data 1: ");
//  Serial.println(data[1]);
//  Serial.print("Data 2: ");
//  Serial.println(data[2]);
//  Serial.print("Data 3: ");
//  Serial.println(data[3]);

  // leg, hipleg, hip
  float angles1[] = {-data[3], data[2], data[1]};
//  float angles2[] = {data[6], data[5], data[4]}; // Reflect: 
//  float angles3[] = {data[10], data[9], data[8]};
//  float angles4[] = {data[14], data[13], data[12]};
  float custom[] = {-90,-90,0};
  Serial.println("ANGLES:");
  Serial.println(angles1[0]);
  Serial.println(angles1[1]);
  Serial.println(angles1[2]);


  //float angles2[] = {data[1], data[2], -data[3]};
  LegFR.move(angles1); //angles1
//  LegFL.move(angles2); //angles2
  //LegBL.move(angles3); //angles 3
  //LegBR.move(angles4);  //angles 4
  //servos[9].write(input);
  delay(75);
  }
}