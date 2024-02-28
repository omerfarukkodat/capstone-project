% Step 9
load matlab.mat
mean_COPx = mean(COPx);
mean_COPy = mean(COPy);
max_diff_ML = max(abs(diff(COPx)));
max_diff_AP = max(abs(diff(COPy)));
n = 1;
m = 2;
sum_sq_diff = (COPx(n+1:end) - COPx(n:end-1)).^2 + (COPy(n+1:end) - COPy(n:end-1)).^2;
planar_deviation = sqrt(sum(sum_sq_diff)) / length(sum_sq_diff);

subplot(5, 5, 9);
plot(abs(diff(COPy)));
xlabel('time (examples)');
ylabel('displacement (mm)');
title('Maximum Displacement');

