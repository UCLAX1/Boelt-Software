import math 

def IK(links, px, py, pz, t1):
    L1 = links["L1"]
    L3 = links["L3"]
    L4 = links["L4"]
    d2 = links["d2"]
    d3 = links["d3"]

    t2 = theta2(px, py, L1, d3, t1) 
    [t4,s4,c4] = theta4(px, py, pz, L1, L3, L4, d2, t1, t2)
    t3 = theta3(L3, L4, d2, pz, s4, c4)
    return [t2, t3, t4]

def theta2(px, py, L1, d3, t1):
    a = -px*math.sin(t1) + py*math.cos(t1)
    b = L1 - px*math.cos(t1) - py*math.sin(t1)
    c = -d3

    g = a**2 + b**2 - c**2
    print(f"A: {a}, B: {b}, C: {c}")

    if (g > 0):
        t2 = math.atan2(-math.sqrt(g), c) + math.atan2(b, a)
        return t2
        # t2_2 = atan2(-sqrt(g), c) + atan2(b, a)
    elif (g == 0):
        t2 = math.atan2(math.sqrt(g), c) + math.atan2(b, a)
        return t2
    else:
        print("There is no solution for this configuration")
    


def theta4(px, py, pz, L1, L3, L4, d2, t1, t2):
    a = L1**2*math.cos(t2)**2 - 2*L1*px*math.cos(t2)*math.cos(t1 + t2) - 2*L1*py*math.sin(t1 + t2)*math.cos(t2)
    b = -L3**2 - L4**2 + d2**2 - 2*d2*pz + px**2*math.cos(t1+t2)**2
    c = px*py*math.sin(2*t1 + 2*t2) + py**2*math.sin(t1+t2)**2 + pz**2

    c4 = (a+b+c)/(2*L3*L4)

    s4 = math.sqrt(1-c4**2)
    t4 = math.atan2(s4, c4)
    # t4_2 = atan2(-s4, c4)
    return [t4,s4,c4]


def theta3(L3, L4, d2, pz, s4, c4):
    a = L4*s4
    b = L3 + L4*c4
    c = pz - d2

    g = a**2 + b**2 - c**2

    if (g > 0):
        t3 = math.atan2(math.sqrt(g), c) + math.atan2(b, a)
        # t3_2 = atan2(-sqrt(g), c) + atan2(b, a)
    elif (g == 0):
        t3 = math.atan2(math.sqrt(g), c) + math.atan2(b, a)
    else:
        print("There is no solution for this configuration")
    return t3
    
