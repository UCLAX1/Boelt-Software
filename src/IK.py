import math
import numpy as np


def IK(target, theta1, config, legIndex):
    # if legIndex <= 1:
    #     py = py-config.center_to_spine
    # else:
    #     py = py+config.center_to_spine

    off = config.offset(legIndex)
    link = config.link(legIndex)
    t1 = theta1+off[0]
    print(f"t1: {t1}")
    [t2, t3, t4] = IK_x(link, target, theta1+off[0])
    q = np.array([theta1, t2-off[1], t3-off[2], t4])
    return q


def IK_x(links, target, t1):
    px = target[0]
    py = target[1]
    pz = target[2]
    print(f"target: {target}")

    t2_1 = theta2(px, py, links.L1, links.d3, t1, 0)
    t2_2 = theta2(px, py, links.L1, links.d3, t1, 1)
    t2s = [t2_1, t2_2]
    print(f"t2s, {t2s}")
    foo = abs(np.array(list(map(wrapToPi, t2s))) - 0.9153)
    I = np.argmin(foo)
    t2 = t2s[I]

    [t4_1, s4_1, c4_1] = theta4(
        px, py, pz, links.L1, links.L3, links.L4, links.d2, t1, t2_1)
    [t4_2, s4_2, c4_2] = theta4(
        px, py, pz, links.L1, links.L3, links.L4, links.d2, t1, t2_2)
    t4s = [t4_1, t4_2]
    t4 = t4s[I]

    t3_1 = theta3(links.L3, links.L4, links.d2, pz, s4_1, c4_1, 1)
    t3_2 = theta3(links.L3, links.L4, links.d2, pz, s4_2, c4_2, 0)
    t3s = [t3_1, t3_2]

    t3 = t3s[I]
    q = np.array([t2, t3, t4])
    return q


def theta2(px, py, L1, d3, t1, solNum):
    a = -px*math.sin(t1) + py*math.cos(t1)
    b = L1 - px*math.cos(t1) - py*math.sin(t1)
    c = -d3

    g = a**2 + b**2 - c**2
    if (abs(g) < 1E5 and g < 0):
        g = 0

    if (g > 0):
        t2s = [math.atan2(math.sqrt(g), c) + math.atan2(b, a),
               math.atan2(-math.sqrt(g), c) + math.atan2(b, a)]
        t2 = t2s[solNum]
        return t2
        # t2_2 = atan2(-sqrt(g), c) + atan2(b, a)
    elif (g == 0):
        t2 = math.atan2(math.sqrt(g), c) + math.atan2(b, a)
        return t2
    else:
        print("There is no solution for this configuration")


def theta4(px, py, pz, L1, L3, L4, d2, t1, t2):
    a = L1**2*math.cos(t2)**2 - 2*L1*px*math.cos(t2) * \
        math.cos(t1 + t2) - 2*L1*py*math.sin(t1 + t2)*math.cos(t2)
    b = -L3**2 - L4**2 + d2**2 - 2*d2*pz + px**2*math.cos(t1+t2)**2
    c = px*py*math.sin(2*t1 + 2*t2) + py**2*math.sin(t1+t2)**2 + pz**2

    c4 = (a+b+c)/(2*L3*L4)

    s4 = math.sqrt(1-c4**2)
    t4 = math.atan2(s4, c4)
    # t4_2 = atan2(-s4, c4)
    return [t4, s4, c4]


def theta3(L3, L4, d2, pz, s4, c4, solNum):
    a = L4*s4
    b = L3 + L4*c4
    c = pz - d2

    g = a**2 + b**2 - c**2

    if (abs(g) < 1E5 and g < 0):
        g = 0

    if (g > 0):
        t3s = [math.atan2(math.sqrt(g), c) + math.atan2(b, a),
               math.atan2(-math.sqrt(g), c) + math.atan2(b, a)]
        t3 = t3s[solNum]
        # t3_2 = atan2(-sqrt(g), c) + atan2(b, a)
    elif (g == 0):
        t3 = math.atan2(math.sqrt(g), c) + math.atan2(b, a)
    else:
        print("There is no solution for this configuration")
    return t3


def wrapToPi(x):
    if not (-math.pi < x < math.pi):
        x = wrapTo2Pi(x+math.pi)-math.pi
    return x


def wrapTo2Pi(x):
    isPositive = (x > 0)
    x = x % (2*math.pi)
    if x == 0 & isPositive:
        x = 2*math.pi
    return x