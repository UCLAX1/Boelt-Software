#include <SoftwareSerial.h>
#include "leg.h"

Leg::Leg(Servo *m1, Servo *m2, Servo *m3, int off1, int off2, int off3)
{
  servos[0] = m1;
  servos[1] = m2;
  servos[2] = m3;
  offset[0] = off1;
  offset[1] = off2;
  offset[2] = off3;
}

void Leg::move(float pos[3])
{
  for (int i = 0; i < 3; i++)
  {
    int angle = offset[i] + pos[i];
    if (angle < -180)
    {
      angle += 360;
    }
    if (angle > 180)
    {
      angle -= 360;
    }
    servos[i]->write(angle);
    Serial.println(angle);
  }
}