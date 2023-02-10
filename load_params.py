import yaml
from pprint import pprint

with open("Robot_Params.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

