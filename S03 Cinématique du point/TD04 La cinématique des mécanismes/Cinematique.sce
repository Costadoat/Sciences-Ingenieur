clear
close
duree=3
l1=0.025
l2=0.05
dt=0.01
t=(0:dt:duree)
m=3*%pi
wm=m*ones(1,size(t,2))
thetam=(m*t)
theta6=acos(-l1*cos(thetam)/l2)
ym=l1*sin(thetam)+l2*sin(theta6)
w6=(-l1*sin(thetam)./(l2*sin(theta6)))*m
Vm=l1*wm.*cos(thetam)+l2*w6.*cos(theta6)
plot(t,Vm,'b')


thetam21=0
theta621=acos(-l1/l2)
wm21=3*%pi
wmt21=0
i=0
for t2=0:dt:duree
    Vm21=10*l1*cos(m*t2)
    wm21=Vm21./(l1.*cos(thetam21)+l2.*(-l1*sin(thetam21)./(l2.*sin(theta621))).*cos(theta621))
    w621=(-l1*sin(thetam21)./(l2*sin(theta621)))*wm21
    theta621=theta621+w621*dt
    thetam21=thetam21+wm21*dt
    thetam2($+1)=thetam21
    theta62($+1)=theta621
    Vm2($+1)=Vm21
    wm2($+1)=wm21
    t1($+1)=t2
end
plot(t1,wm2,'r')
    wmoyen=wmt21/i
