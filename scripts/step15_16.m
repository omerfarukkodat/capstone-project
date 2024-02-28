
%step 15 16
load matlab.mat
ML_STD_SPD = sqrt(mean((COPx - mean_ML).^2));
RMS_ML = sqrt(mean(COPx.^2));
subplot(5, 5, 15);
plot(1:length(COPx), COPx);
xlabel('AP Displacement (mm');
ylabel('ML Displacement (mm)');
title(sprintf('ML Time Series (TD SPD=%.2f)', RMS_ML));

AP_STD_SPD = sqrt(mean((COPy - mean_AP).^2));
RMS_AP = sqrt(mean(COPy.^2));

subplot(5, 5, 16);
plot(1:length(COPy), COPy);
xlabel('ML Displacement (mm');
ylabel('AP Displacement (mm)');
title(sprintf('AP Time Series (TD SPD=%.2f)', RMS_AP));

subplot(5, 5, 17);
plot(COPy);
xlabel('Time (samples)');
ylabel('Displacement (mm)');
title('COPy Time Series');
xlim([1, length(COPy)]);


% speed in ML direction
MEAN_SPD_ML = mean(abs(diff(COPx)));

%  speed in AP direction
MEAN_SPD_AP = mean(abs(diff(COPy)));

% mean speed
MEAN_SPD = mean(sqrt(diff(COPx).^2 + diff(COPy).^2));

% sway length in ML direction
SWAY_LENGTH_ML = sum(abs(diff(COPx)));
% sway length in AP direction
SWAY_LENGTH_AP = sum(abs(diff(COPy)));
% sway length
SWAY_LENGTH = sum(sqrt(diff(COPx).^2 + diff(COPy).^2));

% Plot COP trajectory
subplot(5, 5, 18);
plot(COPx, COPy);
xlabel('Position Médiolatérale (ML)');
ylabel('Position Antéropostérieure (AP)');
title('COP Trajectory');

% bar plot for mean speed
subplot(5, 5, 19);
bar([MEAN_SPD_ML, MEAN_SPD_AP, MEAN_SPD]);
xticks(1:3);
xticklabels({'ML', 'AP', 'Overall'});
xlabel('Direction');
ylabel('Mean Speed');
title('Mean Speed in ML and AP Directions');

% Create a bar plot for sway length
subplot(5, 5, 20);
bar([SWAY_LENGTH_ML, SWAY_LENGTH_AP, SWAY_LENGTH]);
xticks(1:3);
xticklabels({'ML', 'AP', 'Overall'});
xlabel('Direction');
ylabel('Sway Length');
title('Sway Length in ML and AP Directions');


% Define the frequency bands
f_inf = 0;
f_2 = 2;
f_5 = 5;

Fs = 100; 
ML_fft = fft(COPx);
ML_power = abs(ML_fft).^2;
ML_power_half = ML_power(1:floor(length(ML_power)/2)+1);
ML_freq_half = linspace(0, Fs/2, length(ML_power_half));

Delta_t_c = 20;
ML_ST_power = ML_power_half(ML_freq_half <= f_2); % Short-term power spectrum
ML_LT_power = ML_power_half(ML_freq_half > f_2); % Long-term power spectrum
ML_LT_power = ML_LT_power(ML_freq_half(ML_freq_half > f_2) <= f_5); % Remove frequencies above 5 Hz
Hs = sum(ML_ST_power); 
Hl = sum(ML_LT_power); 

Gamma_X_ST = sum(ML_power_half(f_inf < ML_freq_half & ML_freq_half <= f_2)) / Hs;
Gamma_X_LT = sum(ML_power_half(f_2 < ML_freq_half & ML_freq_half <= f_5)) / Hl;

% Plot the power spectrum in the ML direction
subplot(5,5,21);
plot(ML_freq_half, ML_power_half);
xlabel('Frequency (Hz)');
ylabel('Power (cm^2/Hz)');
title('Power Spectrum in the ML Direction');

hold on;
line([f_2 f_2], [0 max(ML_power_half)], 'Color', 'r', 'LineWidth', 1.5);
line([f_5 f_5], [0 max(ML_power_half)], 'Color', 'r', 'LineWidth', 1.5);
line([f_inf f_2], [Gamma_X_ST*Hs Gamma_X_ST*Hs], 'Color', 'g', 'LineWidth', 1.5);
line([f_2 f_5], [Gamma_X_LT*Hl Gamma_X_LT*Hl], 'Color', 'g', 'LineWidth', 1.5);
text(f_2+0.1, max(ML_power_half)*0.8, sprintf('\\Gamma_X^{ST} = %.2f',Gamma_X_ST),'Color', 'g');
text(f_2+0.1, max(ML_power_half)*0.6, sprintf('\\Gamma_X^{LT} = %.2f',Gamma_X_LT),'Color', 'g');
legend('Power Spectrum', '2 Hz', '5 Hz', 'Frequency Quotient');




