theta=pi/2;
R2=0.15;
R1=0.1;
F=500;
fr=0.3;

S=theta/2*(R2^2-R1^2)
P=F/S;

Nt=10;
Nr=10;
dr=(R2-R1)/Nr;
dt=theta/Nt;

C1=0;

for i=1:Nr
   
    for j=1:Nt
     ds=(R1+dr*(i-1/2))*dr*dt;
     F=fr*ds*P;
     C1=C1+2*F*(R1+dr*(i-1/2));
    end
   
    
end
C1
C2=2*theta*fr*P*(R2^3-R1^3)/3