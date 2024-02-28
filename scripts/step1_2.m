% Center of Pressure (COP)
% step 1 2 
load matlab.mat
 ML= COPx;
 AP= COPy;

Xn1 = ML - mean(ML);
Xn2 = ML - (sum(ML) / length(ML));

figure();
plot(Xn1);
xlabel('ML');
ylabel('AP');
title('COP Mean ML coordinate')
