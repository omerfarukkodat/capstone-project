% step 11 
load matlab.mat
ML = sum(abs(ML))/length(ML);
MAX = max(ML)-min(ML);
subplot(5,5,11)
plot(ML, AP, '.');
xlabel('ML');
ylabel('AP');
title('COP max sinyal')

