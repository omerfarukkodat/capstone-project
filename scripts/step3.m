
% step 3
load matlab.mat
ML= COPx;
AP= COPy;
Yn = COPx - mean(AP);
Xn = COPy - mean(ML);
COV = sum(Xn.*Yn) / length(Yn); 
Rn = sqrt(Xn.^2 + Yn.^2);

subplot(5,5,3);
plot(COPx,COPy);
xlabel('ML');
ylabel('AP');
title('COP Mean distance')