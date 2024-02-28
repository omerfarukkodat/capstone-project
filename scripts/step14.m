% step 14
load matlab.mat
%  total sway length
SWAY_LENGTH = sum(sqrt(diff(COPx).^2 + diff(COPy).^2));

%  COP data with sway path
subplot(5,5,12);
plot(COPx, COPy);
xlabel('ML');
ylabel('AP');
title('Center of Pressure');
hold on;
plot(COPx(1:end-1), COPy(1:end-1), 'Color', 'r');
legend('COP', 'Sway Path');

%  COPxnsway path in the ML direction
subplot(5,5,13);
plot(COPx(1:end-1), abs(diff(COPx)));
xlabel('ML');
ylabel('Sway Path');
title('Sway Path in the ML Direction');

% COPy sway path in the AP direction
subplot(5,5,14);
plot(COPy(1:end-1), abs(diff(COPy)));
xlabel('AP');
ylabel('Sway Path');
title('Sway Path in the AP Direction');
