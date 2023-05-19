import walk_test
import move_foot as mf
from Config import Configuration

iterations = 1
config = Configuration()
answer = mf.moveFoot(config, 0, 0.5, 0.5, 0)
print(f"KINEMATICSSSS: {answer}")
#answer1 = mf.moveFoot(config, 1, 0.5, 0.5, 0)
#print("answer worked")
#answer2 = mf.moveFoot(config, 2, 0.5, 0.5, 0)
#print("answer worked")
answer3 = mf.moveFoot(config, 3, 0.5, 0.5, 0)
print("answer worked")
#currentPos holds IK values where the legs should be with indexes 0-3 representing legs 0-3
currentPos = [answer, answer3, answer, answer3 ]
increment = 1
print("Initial Values of currentPos:")
for i, value in enumerate(currentPos):
    print(f"Index {i}: {value}")
#walk_test.startup(increment, currentPos)
# Print the values of currentPos after startup
#print("Values of currentPos after startup:")
#for i, value in enumerate(currentPos):
    print(f"Index {i}: {value}")
while(iterations > 0):
    walk_test.walking(increment, currentPos)
    # Print the values of currentPos after each walking call
    print("Values of currentPos after walking:")
    for i, value in enumerate(currentPos):
        print(f"Index {i}: {value}")
    iterations = iterations - 1
