load matlab.mat
 ML= COPx;
 AP= COPy;

Xn1 = ML - mean(ML);
Xn2 = ML - (sum(ML) / length(ML));


figure();
plot(Xn2);
xlabel('ML');
ylabel('AP');
title('COP Mean AP coordinate')