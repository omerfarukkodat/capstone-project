% step 5 
load matlab.mat
RMS_ML = sqrt(mean((ML - mean_ML).^2));
RMS_AP = sqrt(mean((AP - mean_AP).^2));
RMS_RADIUS = sqrt(mean((sqrt((ML - mean_ML).^2 + (AP - mean_AP).^2)).^2));


subplot(5, 5, 5)
plot(ML, AP, '.');
hold on;
plot(mean_ML, mean_AP, 'r*');
theta = linspace(0, 2*pi, 100);
x = mean_ML + RMS_ML * cos(theta);
y = mean_AP + RMS_AP * sin(theta);
plot(x, y, 'g', 'LineWidth', 2);
axis equal;
xlabel('ML');
ylabel('AP');
title('COP RMS')