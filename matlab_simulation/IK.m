function [t2, t3, t4] = IK(links, px, py, pz, t1, off)
    L1 = links.L1;
    L3 = links.L3;
    L4 = links.L4;
    d2 = links.d2;
    d3 = links.d3;

    t2 = theta2(px, py, L1, d3, t1);
    [t4,s4,c4] = theta4(px, py, pz, L1, L3, L4, d2, t1, t2);
    t3 = theta3(L3, L4, d2, pz, s4, c4);
    t2 = wrapToPi(t2);
    t3 = wrapToPi(t3);
    t4 = wrapToPi(t4);

end

function t2 = theta2(px, py, L1, d3, t1)
    a = -px*sin(t1) + py*cos(t1);
    b = L1 - px*cos(t1) - py*sin(t1);
    c = -d3;

    g = a^2 + b^2 - c^2
    if (abs(g) < 1E-5 && g<0)
        g = 0
    end
    

    if (g > 0)
%         t2 = atan2(-sqrt(g), c) + atan2(b, a);
        t2 = atan2(sqrt(g), c) + atan2(b, a);

    elseif (g == 0)
        g
        t2 = atan2(sqrt(g), c) + atan2(b, a)
    else
        fprintf("There is no solution for this configuration")
    end
end

function [t4,s4,c4] = theta4(px, py, pz, L1, L3, L4, d2, t1, t2)
    a = L1^2*cos(t2)^2 - 2*L1*px*cos(t2)*cos(t1 + t2) - 2*L1*py*sin(t1 + t2)*cos(t2);
    b = -L3^2 - L4^2 + d2^2 - 2*d2*pz + px^2*cos(t1+t2)^2;
    c = px*py*sin(2*t1 + 2*t2) + py^2*sin(t1+t2)^2 + pz^2;

    c4 = (a+b+c)/(2*L3*L4);

    if (c4-1 < 1E-5 && c4 > 1)
        c4 = 1
    end

    s4 = sqrt(1-c4^2);
    t4 = atan2(s4, c4);
%     t4_2 = atan2(-s4, c4);
end

function t3 = theta3(L3, L4, d2, pz, s4, c4)
    a = L4*s4;
    b = L3 + L4*c4;
    c = pz - d2;

    g = a^2 + b^2 - c^2;
    if (abs(g) < 1E-5  && g<0)
        g = 0
    end

    if (g > 0)
        t3 = atan2(-sqrt(g), c) + atan2(b, a);
%         t3_2 = atan2(-sqrt(g), c) + atan2(b, a);
    elseif (g == 0)
        t3 = atan2(sqrt(g), c) + atan2(b, a);
    else
        print("There is no solution for this configuration")
    end
end

