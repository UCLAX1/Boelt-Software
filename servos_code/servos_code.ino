// modified: 2/17 by Emily Liang

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
//int servos_size = sizeof(servos)/sizeof(servos[0]);
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
int off1 = 85; //leg FR
int off2 = 100; //leghip FR
int off3 = 115; //hip FR

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
 
void loop() {
  while (Serial.available()==0){} 
  input = Serial.parseInt(); 
  Serial.println(input);
  int pos[] = {input, input, input};
  LegFR.move(pos);
  //servos[9].write(input);
  delay(15);
/*
  for (int i = 0; i < servos_size; i++) 
  {
    servos[i].write(default_pos[i]);
    delay(15); 
  }*/
  
  /*int test = servos[1].read();
  Serial.println(test);
  delay(15);*/

//    servos[0].write(0);
//  for(int i = 1; i <= 40; i++) 
//  {                                
//   pos += 1;
//   for(int i = 0; i < servos_size; i++)
//   {
//     servos[i].write(pos);
//   }
//    delay(15);                       // waits 15ms for the servo to reach the position 
//  } 
//  for(int i = 1; i <= 40; i++)     // goes from 180 degrees to 0 degrees 
//  {                                
//    pos -= 1;
//    for(int i = 0; i < servos_size; i++)
//   {
//     servos[i].write(pos);
//   }
//    delay(15);                       // waits 15ms for the servo to reach the position 
//  } 
}