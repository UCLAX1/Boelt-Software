#ifndef LEG
#define LEG

#include "Arduino.h"
#include <Servo.h>

class Leg 
{
  public:
    int servoIndex[3];
    int legOffset[3];
    Servo motor1;
    Servo motor2;
    Servo motor3;
    void move( int pos[3] );
    
    
};

#endif
