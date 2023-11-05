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

data = Network('O1.s2p')
totalPoints = int(data.s.size/4)

for i in range(totalPoints):
    _complex_s11 = data.s[i:(i+1),0,0][0]
    _complex_s21 = data.s[i:(i+1),0,1][0]

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
    
    L = 0.006072
    # print("L", L)
    t = (_complex_s11+ _complex_s21 - _gm3)/(1-((_complex_s11 + _complex_s21) * _gm3))
    # print("t", t)
    tx = numpy.log(1/t)
    # print("tx", tx)
    txx = -((1/(2 * math.pi * L)) * tx)**2
    # print("txx", txx)
    phase_fac = txx**(1/2)
    # print("phase_fac", phase_fac)

    _c = constants.c # 3*10^8 # speed of light
    # print("_c", _c)
    _fq = data.f[i:(i+1)]
    graph_frequency.append(_fq[0])
    # print("_fq", _fq)
    _lambda = _c / _fq
    # print("_lambda", _lambda)
    _fc = 6.557e9 #cutoff frequency #Ghz conversion???
    # print("_fc", _fc)
    _lc = _c/_fc
    # print("_lc", _lc)
    _a = 1/numpy.square(_lc)
    # print("_a", _a)

    za = (1+_gm3)/(1-_gm3)
    # print("za", za)
    yy = (1/numpy.square(_lambda)) - _a
    # print("yy", yy)
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


plt.plot(graph_frequency, graph_magnetic)
plt.plot(graph_frequency, graph_electrical)
plt.plot(graph_frequency, graph_loss)
plt.show()
