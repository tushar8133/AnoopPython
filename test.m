
%% Data initialization%%
% O is the data file for teflon measurements with frequency, S11 real, S11imaginary, S21 real, S21 imaginary  data in 1st, 2nd, 3rd, 4th, 5th column respectively

O= xlsread('O');
 
freq = O(:,1); % frequency in Hz

s11real_tef(:,1) = O(:,2);
s11imag_tef(:,1) = O(:,3);
s21real_tef(:,1) = O(:,4);
s21imag_tef(:,1) = O(:,5);

s11_tef(:,1) = complex(s11real_tef(:,1), s11imag_tef(:,1));
s21_tef(:,1) = s21real_tef(:,1)+1j*s21imag_tef(:,1);

% defined measured data as 
S11 = s11_tef;
S21 = s21_tef;

% size of material (m)
L=0.005098; % for teflon

%% S11 and S21 are final data for s11 and s21 as measured at calibrated ports
% freq is column matrix with frequency data in Hz 

% initialize parameters

b=length(freq);
c=3.0e8; % speed of light
fc=6.557e9; % cut off frequency (X-band)
lamc= c/fc; % cut off wavelength
lam=c./freq; %wavelength
a= 1/(lamc^2);


% initialize variables

yy = zeros(b,1); gamma0 = zeros(b,1);

for i = 1:b
    yy(i,1) = (1/lam(i,1)^2)- a ;
    gamma0(i,1) = 2*pi*1j*sqrt(yy(i,1));
end


%======================
% Calculate X & Gama
%======================

X = zeros(b,1);
gama1 = zeros(b,1);
gama2 = zeros(b,1);
gama = zeros(b,1);

for i = 1:b
    X(i,1) =((S11(i,1)^2)- (S21(i,1)^2) + 1)/(2*S11(i,1));
    gama1(i,1) = X(i,1) + sqrt((X(i,1)^2)-1);
    gama2(i,1) = X(i,1) - sqrt((X(i,1)^2)-1);
end

%======================
% Check Reflection<=1
%======================
for i=1:b
    if abs(gama2(i,1))<=1
        gama(i,1)=gama2(i,1);
    else
        if abs(gama1(i,1))<=1
            gama(i,1)=gama1(i,1);
        end
    end
end

