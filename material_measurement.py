from skrf import Network, Frequency, constants
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
import math
import numpy

graph_magnetic = []
graph_electrical = []
graph_loss = []
graph_frequency = []

data = Network('C:/test.s2p')
totalPoints = int(data.s.size/4)

for i in range(totalPoints):

    _fc = 6.557e9  # user input cutoff frequency #Ghz conversion???
    # print("_fc", _fc)
    L = 0.0015 #user input thickness of material
    # print("L", L)
    Ltotal = 0.00911 #user input waveguide total length
    # print("Ltotal", Ltotal)
    L1 = 0.00 #user input empty space
    # print("L1", L1)
    L2 = Ltotal-L-L1
    # print("L2", L2)
    _c = constants.c # 3*10^8 # speed of light
    # print("_c", _c)
    _fq = data.f[i:(i+1)]
    graph_frequency.append(_fq[0])
    # print("_fq", _fq)
    _lambda = _c / _fq
    # print("_lambda", _lambda)
    _lc = _c/_fc
    # print("_lc", _lc)
    _a = 1/numpy.square(_lc)
    # print("_a", _a)
    yy = (1/numpy.square(_lambda)) - _a
    #print("yy", yy)
    _gm0 = 2 * math.pi * 1j * numpy.sqrt(yy)
    #print("_gm0", _gm0)

    #Calculate plane transformation
    R1 = numpy.exp(-_gm0*L1)
    #print("R1", R1)
    R2 = numpy.exp(-_gm0*L2)
    #print("R2", R2)

    _complex_s11_NRW = data.s[i:(i+1),0,0][0]
    _complex_s21_NRW = data.s[i:(i+1),0,1][0]

    _complex_s11 = _complex_s11_NRW/(R1**2)
    _complex_s21 = _complex_s21_NRW/(R1*R2)

    _x = ((   (_complex_s11)**2 ) - ((_complex_s21)**2) + 1) / (2 * _complex_s11)
    # print('_x', _x)
    _gm1 = _x + (( (_x**2) - 1 )**(1/2))
    # print('_gm1', _gm1)
    _gm2 = _x - (( (_x**2) - 1 )**(1/2))
    # print('_gm2', _gm2)
    _ag1 = abs(_gm1)
    # print('_ag1', _ag1)
    _ag2 = abs(_gm2)
    # print('_ag2', _ag2)
    
    _gm3 = 0
    if _ag2 <= 1:
        _gm3 = _gm2
    elif _ag1 <= 1:
        _gm3 = _gm1
    # print(_gm3)

    t = (_complex_s11+ _complex_s21 - _gm3)/(1-((_complex_s11 + _complex_s21) * _gm3))
    # print("t", t)
    tx = numpy.log(1/t)
    # print("tx", tx)
    txx = -((1/(2 * math.pi * L)) * tx)**2
    # print("txx", txx)
    phase_fac = txx**(1/2)
    # print("phase_fac", phase_fac)


    za = (1+_gm3)/(1-_gm3)
    # print("za", za)
    mur = (za * (phase_fac) * (1/numpy.sqrt(yy))) #magnetic
    # print("mur", mur)
    er = ((numpy.square(_lambda))/mur) * (txx + _a) # electric
    # print("er", er)
    tandel1 = (mur.real * er.real) - (mur.imag * er.imag)
    # print("tandel1", tandel1)
    tandel2 = (mur.real * er.imag) + (mur.imag * er.real)
    # print("tandel2", tandel2)
    loss = tandel2/tandel1
    # print("loss", loss)

    graph_magnetic.append(mur[0].real)
    graph_electrical.append(er[0].real)
    graph_loss.append(loss[0])

'''
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')'''


fig, axs = plt.subplots(2, 2)
#plt.title("magnetic", loc = 'left')
plt.xlabel("Frequency")
#plt.ylabel("Mu")
#plt.plot( graph_frequency, graph_magnetic)
plt.plot(graph_frequency, graph_electrical, label="Er")
#plt.plot(graph_frequency, graph_loss, label="Loss")
plt.show()
