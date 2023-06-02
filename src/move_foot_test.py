import walk_test
import move_foot as mf
from Config import Configuration
from ctypes import c_float
from math import degrees
from serial import Serial
from time import sleep
import struct


iterations = 5
config = Configuration()
answer = mf.moveFoot(config, 0, 0.5, 0.5, 0)
answer1 = mf.moveFoot(config, 1, 0.5, 0.5, 0)
answer2 = mf.moveFoot(config, 2, 0.5, 0.5, 0)
answer3 = mf.moveFoot(config, 3, 0.5, 0.5, 0)

# currentPos holds IK values where the legs should be with indexes 0-3 representing legs 0-3
# currentPos = [answer, answer1, answer2, answer3]
y_pos = 0
dy = 0.01

while True:
    if y_pos >= 1:
        dy = -0.01
    if y_pos <= 0:
        dy = 0.01

    y_pos += dy
    print("y_pos: " + str(y_pos))

    answer = mf.moveFoot(config, 3, 0.5, y_pos , 0)
    answer1 = mf.moveFoot(config, 1, 0.5, y_pos, 0)
    answer2 = mf.moveFoot(config, 2, 0.5, y_pos, 0)
    answer3 = mf.moveFoot(config, 3, 0.5, y_pos, 0)
    c_ans = list(map(c_float, list(map(degrees, answer))))
    c_ans += list(map(c_float, list(map(degrees, answer1))))
    c_ans += list(map(c_float, list(map(degrees, answer2))))
    c_ans += list(map(c_float, list(map(degrees, answer3))))

    print(c_ans)

    ser = Serial('/dev/cu.usbmodem131488301', 115200, timeout=1)
    # Pack the data into a binary format
    packed_data = struct.pack('16f', *[c.value for c in c_ans])
    # Send the packed data over serial
    ser.write(packed_data)
    print('sent data')

    junk = input('Continue')
