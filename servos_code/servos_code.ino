// modified: 2/17 by Emily Liang

#include <Servo.h> 

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

int input;
int off1 = 50;
int off2 = 115;
int off3 = 120;



int pos = 70; 
 
void setup() 
{ 
  for (int i = 0; i < servos_size; i++) 
  {
    servos[i].write(pos);
  }
  delay(15); 
    
  /*for (int i = 2; i <= 14; i++) {
    if (i != 4) 
    {
      servos[i].attach(i);
    }
  }
  spineF.attach(24); 
  spineB.attach(23);*/
  servos[0].attach(2);
  servos[2].attach(7);
  servos[1].attach(8);
  Serial.begin(9600);
  servos[0].write(off1);   
  servos[1].write(off2 + 85.664);
  servos[2].write(off3-22.5);

} 
 
void loop() {
  while (Serial.available()==0){} 
  input = Serial.parseInt(); 
  Serial.println(input);
  servos[2].write(input);

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
