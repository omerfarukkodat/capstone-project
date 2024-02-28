%Step 7
load matlab.mat
mean_ML = mean(COPx);
mean_AP = mean(COPy);
max_radius = max(abs(COPx-mean_ML)) + max(abs(COPy-mean_AP));

subplot(5, 5, 7)
plot(AP, ML, '.');
hold on
plot(mean_ML, mean_AP, 'r*');
Theta = linspace(0, 2*pi, 100);
x = mean_ML + max_radius * cos(Theta);
y = mean_AP + max_radius * sin(Theta);
plot(x, y, 'g', 'LineWidth', 2);
xlabel('ML');
ylabel('AP');
title('Center of Pressure (COP) and Sway Area');


