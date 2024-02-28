 % STEP 6
 load matlab.mat
subplot(5, 5, 6)
plot(ML, AP, '.');
hold on;
plot(mean_ML, mean_AP, 'r*');
theta = linspace(0, 2*pi, 100);
x = mean_ML + max_radius * cos(theta);
y = mean_AP + max_radius * sin(theta);
plot(x, y, 'g', 'LineWidth', 2);
axis equal;
xlabel('ML');
ylabel('AP');
title('COP Range (Amplitude)')
