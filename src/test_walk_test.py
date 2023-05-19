import walk_test
import move_foot as mf
from Config import Configuration

iterations = 5
config = Configuration()
answer = mf.moveFoot(config, 0, 0.5, 0.5, 0)
answer1 = mf.moveFoot(config, 1, 0.5, 0.5, 0)
answer2 = mf.moveFoot(config, 2, 0.5, 0.5, 0)
answer3 = mf.moveFoot(config, 3, 0.5, 0.5, 0)

#currentPos holds IK values where the legs should be with indexes 0-3 representing legs 0-3
currentPos = [answer, answer1, answer2, answer3 ]
queueOfPos = []
queueOfPos.append(currentPos)
increment = 1
print("Initial Values of currentPos:")
for i, value in enumerate(currentPos):
    print(f"Index {i}: {value}")
walk_test.startup(increment, currentPos, queueOfPos)
# Print the values of currentPos after startup
print("Values of currentPos after startup:")
for i, value in enumerate(currentPos):
    print(f"Index {i}: {value}")
while(iterations > 0):
    walk_test.walking(increment, currentPos, queueOfPos)
    # Print the values of currentPos after each walking call
    print("Values of currentPos after walking:")
    for i, value in enumerate(currentPos):
        print(f"Index {i}: {value}")
    iterations = iterations - 1
