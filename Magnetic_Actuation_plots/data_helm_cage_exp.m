%MATLAB script for plotting the results of the  magnetic actuation
%Remember to convert the '.csv' file into a '.mat' workspace named 's_dot.mat'

load('s_dot.mat')
ang_speed_IMU = sdot_meas(:,3:5);
ang_speed_kalman = sdot_meas(:,20:22);

euler_angles = sdot_meas(:,10:12);
quat = sdot_meas(:,13:16);

mag_field = sdot_meas(:,6:9);

cm = sdot_meas(:,17:19);

dipole = sdot_meas(:,23:25);
pwm = sdot_meas(:,26:28);
direc = sdot_meas(:,29:31);

aux_time = sdot_meas(:,2);
Time = aux_time;
runtime = 0;


for nom = 1:length(aux_time)
    Time(nom) = runtime;
    runtime = runtime + aux_time(nom);
end


figure('Color',[1 1 1])
plot(Time,ang_speed_kalman(:,1),'b','LineWidth',2);
hold on
plot(Time,ang_speed_IMU(:,1),'g','LineWidth',2);
xlabel('Time, s')
ylabel('Angular Velocity in X, deg/s')
legend('Kalman','IMU')
grid on


figure('Color',[1 1 1])
plot(Time,ang_speed_kalman(:,2),'b','LineWidth',2);
hold on
plot(Time,ang_speed_IMU(:,2),'g','LineWidth',2);
xlabel('Time, s')
ylabel('Angular Velocity in Y, deg/s')
legend('Kalman','IMU')
grid on

figure('Color',[1 1 1])
plot(Time,ang_speed_kalman(:,3),'b','LineWidth',2);
hold on
plot(Time,ang_speed_IMU(:,3),'g','LineWidth',2);
xlabel('Time, s')
ylabel('Angular Velocity in Z, deg/s')
legend('Kalman','IMU')
grid on

figure('Color',[1 1 1])
plot(Time,mag_field(:,1),'b','LineWidth',2);
hold on
plot(Time,mag_field(:,2),'g','LineWidth',2);
plot(Time,mag_field(:,3),'r','LineWidth',2);
plot(Time,mag_field(:,3),'r','LineWidth',2);
xlabel('Time, s')
ylabel('Magnetometer measurements, µT')
legend('X','Y','Z', '|B|')
grid on

figure('Color',[1 1 1])
plot(Time,euler_angles(:,1),'b','LineWidth',2);
hold on
plot(Time,euler_angles(:,2),'g','LineWidth',2);
plot(Time,euler_angles(:,3),'r','LineWidth',2);
xlabel('Time, s')
ylabel('Euler Angles, deg')
legend('Roll','Pitch','Yaw')
grid on



figure('Color',[1 1 1])
plot(Time,quat(:,1),'b','LineWidth',2);
hold on
plot(Time,quat(:,2),'g','LineWidth',2);
plot(Time,quat(:,3),'r','LineWidth',2);
plot(Time,quat(:,4),'y','LineWidth',2);
xlabel('Time, s')
ylabel('Quaternions')
legend('q0','q1','q2','q3')
grid on

figure('Color',[1 1 1])
plot(Time,cm(:,1),'b','LineWidth',2);
hold on
plot(Time,cm(:,2),'g','LineWidth',2);
plot(Time,cm(:,3),'r','LineWidth',2);
xlabel('Time, s')
ylabel('Center of mass Shift, m')
legend('X','Y','Z')
grid on


for i = 1:length(pwm)
    if direc(i,1) == 1
        pwm(i,1) = pwm(i,1) * -1;
    end
    if direc(i,2) == 1
        pwm(i,2) = pwm(i,2) * -1;
    end
    if direc(i,3) == 1
        pwm(i,3) = pwm(i,3) * -1;
    end        
end

figure('Color',[1 1 1])
plot(Time,pwm(:,1),'b','LineWidth',2);
hold on
plot(Time,pwm(:,2),'g','LineWidth',2);
plot(Time,pwm(:,3),'r','LineWidth',2);
xlabel('Time, s')
ylabel('PWM')
legend('X','Y','Z')
grid on

figure('Color',[1 1 1])
plot(Time,dipole(:,1),'b','LineWidth',2);
hold on
plot(Time,dipole(:,2),'g','LineWidth',2);
plot(Time,dipole(:,3),'r','LineWidth',2);
xlabel('Time, s')
ylabel('Magnetic Dipole, X')
legend('X','Y','Z')
grid on

