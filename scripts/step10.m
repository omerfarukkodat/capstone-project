% step 10
load matlab.mat
var_vel_AP = var(diff(COPx));
var_vel_ML = var(diff(COPy));
mean_AP = mean(abs(COPy));
sway_vel_coeff = sqrt((var_vel_ML + var_vel_AP) / (mean_AP^2));

subplot(5,5,10);
plot(1:length(COPx), COPx, 'b');
hold on;
plot(1:length(COPy), COPy, 'r');
xlabel('Time (samples)');
ylabel('Displacement (mm)');
title(sprintf('COP Displacement and Sway Velocity (Coefficient=%.2f)', sway_vel_coeff));
legend('ML Displacement', 'AP Displacement');
