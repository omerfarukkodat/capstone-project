% step 8
load matlab.mat
std_x = std(COPy);
std_y = std(COPy);
corr_coef = corrcoef(COPx, COPy);
r = corr_coef(1, 2);
sway_dir_coeff = (std_y * r - std_x) / (std_y * r + std_x);
subplot(5, 5, 8)
plot(COPx,COPy)
xlabel('ML');
ylabel('AP');
title('Sway Direction Coeff');

