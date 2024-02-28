% step 4
load matlab.mat
mean_ML = mean(ML);
mean_AP = mean(AP);
max_ML = max(abs(ML - mean_ML));
max_AP = max(abs(AP - mean_AP));
max_radius = max(sqrt((ML - mean_ML).^2 + (AP - mean_AP).^2));

subplot(5, 5, 4)
plot(ML, AP, '.');
hold on;
plot(mean_ML, mean_AP, 'r*');
theta = linspace(0, 2*pi, 100);
x = mean_ML + max_ML * cos(theta);
y = mean_AP + max_AP * sin(theta);
plot(x, y, 'g', 'LineWidth', 2);
axis equal;
xlabel('ML');
ylabel('AP');
title('COP Max')