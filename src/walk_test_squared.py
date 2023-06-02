import walk_test
import move_foot as mf
from Config import Configuration
from ctypes import c_float
from math import degrees
from serial import Serial
from time import sleep
import struct


iterations = 1
config = Configuration()
answer = mf.moveFoot(config, 0, 0.5, 0.5, 0)
answer1 = mf.moveFoot(config, 1, 0.5, 0.5, 0)
answer2 = mf.moveFoot(config, 2, 0.5, 0.5, 0)
answer3 = mf.moveFoot(config, 3, 0.5, 0.5, 0)

# currentPos holds IK values where the legs should be with indexes 0-3 representing legs 0-3
currentPos = [answer, answer1, answer2, answer3]
queueOfPos = []
queueOfPos.append(currentPos.copy())
increment = 1
# print("Initial Values of currentPos:")
# for i, value in enumerate(currentPos):
#     print(f"Index {i}: {value}")
walk_test.startup(increment, currentPos, queueOfPos)
# Print the values of currentPos after startup
# print("Values of currentPos after startup:")
# for i, value in enumerate(currentPos):
#     print(f"Index {i}: {value}")
# sleep(100)
# while (iterations > 0):
#     walk_test.walking(increment, currentPos, queueOfPos)
#     # Print the values of currentPos after each walking call
#     # print("Values of currentPos after walking:")
#     # for i, value in enumerate(currentPos):
#     #     print(f"Index {i}: {value}")
#     iterations = iterations - 1
# # print("QUEUE OF POS"+str(queueOfPos))
while (len(queueOfPos) > 0):
    # print("Length of QOP: " + str(len(queueOfPos)))
    # print("last QOP: " + str(queueOfPos[-1]))

    currentPos = queueOfPos.pop(0)
    # print("Length of QOP: " + str(len(queueOfPos)))
    # print("last QOP: " + str(queueOfPos[-1]))

    # print("CURRENTPOS" + str(currentPos))
    c_ans = list(map(c_float, list(map(degrees, currentPos[0]))))
    c_ans += list(map(c_float, list(map(degrees, currentPos[1]))))
    c_ans += list(map(c_float, list(map(degrees, currentPos[2]))))
    c_ans += list(map(c_float, list(map(degrees, currentPos[3]))))

    # print('Degrees: ' + str(c_ans))
    # print(type(c_ans[1]))
    # Send out ik anlges to arduino #

    ser = Serial('/dev/cu.usbmodem131488301', 115200, timeout=1)
    # Pack the data into a binary format
    packed_data = struct.pack('16f', *[c.value for c in c_ans])
    # Send the packed data over serial
    ser.write(packed_data)
    print('sent data')
    #sleep(.01)

    junk = input('Continue')
