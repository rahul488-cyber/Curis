function joint_angles = IK(pos_target)

% Initialization
jinit = [90; 60; -120]; 
jstart = jinit;
FK = FKdraw(jinit(1,1), jinit(2,1), jinit(3,1));
pos_start = [FK(1,16); FK(2,16); FK(3,16)];
delta = divelo(pos_start, pos_target);

% Assign initial variables
j1 = jstart(1,1);
j2 = jstart(2,1);
j3 = jstart(3,1);

% Check if target position is different from start position
if pos_target == pos_start
    error('Set target position first: No Movement'); 
end

movement = 1;

while movement == 1
    FK = FKdraw(j1, j2, j3);
    Jac = Jacobian(FK);
    Jacinv = pinv(Jac);
    dXYZ = delta(1:3,1) / 10;  
    dTheta = Jacinv * dXYZ;
    dTheta1 = radtodeg(dTheta(1,1));
    dTheta2 = radtodeg(dTheta(2,1));
    dTheta3 = radtodeg(dTheta(3,1));
    j1 = j1 + dTheta1;
    j2 = j2 + dTheta2;
    j3 = j3 + dTheta3;
    FK = FKdraw(j1, j2, j3);
    pos_new = [FK(1,16); FK(2,16); FK(3,16)];
    delta = divelo(pos_new, pos_target);
    EucError = delta(5,1)^2;
    
    if EucError < 10^-2
        movement = 0; 
        pos_start = pos_new;
        jstart = [j1; j2; j3];
    end 

    if all(delta(:) <= 0.1)
        movement = 0; 
        pos_start = pos_new;
        jstart = [j1; j2; j3];
    end 
end

% Print and return the final joint angles
disp(['Final joint angles: j1 = ', num2str(j1), ', j2 = ', num2str(j2), ', j3 = ', num2str(j3)]);
joint_angles = [j1, j2, j3];

end
