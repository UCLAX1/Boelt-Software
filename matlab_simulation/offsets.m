function [off_fl, off_fr, off_bl, off_br] = offsets(x1, y1, x2, y2)
    
    t1 = atan2(x1, y1);
    t2 = atan2(x2, y2);

    off_fr = fr(t1);
    off_fl = fl(t1);

    off_br = br(t2);
    off_bl = bl(t2);
    
    
end

function off = fr(t1)
    off.t1 = t1;
    off.t2 = (pi/2-t1);
    off.t3 = -pi/2;
end

function off = fl(t1)
    off.t1 = pi-t1;
    off.t2 = t1-pi/2;
    off.t3 = -pi/2;
end

function off = br(t2)
    off.t1 = -t2;
    off.t2 = t2+pi/2;
    off.t3 = -pi/2;
end

function off = bl(t2)
    off.t1 = t2-pi;
    off.t2 = -pi/2-t2;
    off.t3 = -pi/2;
end