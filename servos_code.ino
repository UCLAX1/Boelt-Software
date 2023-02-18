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
  servos[0].attach(22);
} 
 
void loop() 
{ 
  for(int i = 1; i <= 40; i++) 
  {                                
   pos += 1;
   for(int i = 0; i < servos_size; i++)
   {
     servos[i].write(pos);
   }
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  for(int i = 1; i <= 40; i++)     // goes from 180 degrees to 0 degrees 
  {                                
    pos -= 1;
    for(int i = 0; i < servos_size; i++)
   {
     servos[i].write(pos);
   }
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
} 
