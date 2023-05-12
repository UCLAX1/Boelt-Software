import walk_test
import move_foot as mf
from Config import Configuration

config = Configuration()
#currentPos holds IK values where the legs should be with indexes 0-3 representing legs 0-3
currentPos = [mf.moveFoot(config, 0, 0.5, 0.5, 0), mf.moveFoot(config, 1, 0.5, 0.5, 0), mf.moveFoot(config, 2, 0.5, 0.5, 0), mf.moveFoot(config, 3, 0.5, 0.5, 0)]
increment = 0.0001
print("Initial Values of currentPos:")
for i, value in enumerate(currentPos):
    print(f"Index {i}: {value}")
walk_test.startup(increment, currentPos)
# Print the values of currentPos after startup
print("Values of currentPos after startup:")
for i, value in enumerate(currentPos):
    print(f"Index {i}: {value}")
while():
    walk_test.walking(increment, currentPos)
    # Print the values of currentPos after each walking call
    print("Values of currentPos after walking:")
    for i, value in enumerate(currentPos):
        print(f"Index {i}: {value}")
