#ifndef LEG
#define LEG

#include "Arduino.h"
#include <Servo.h>

class Leg
{
  public:
    Leg(int sn, Servo *m1, Servo *m2, Servo *m3, int off1, int off2, int off3);
    int offset[3];
    Servo* servos[3];
    void move( int pos[3] );
    
    
};

#endif
