from skrf import Network, Frequency
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
data = Network('Port 4.s2p')


s11 = data.s11
s11_w = data.windowed()

s11_gated = data.s11.time_gate(center=5, span=10, t_unit='ns')

#s11.plot_s_db_time()
s11_gated.plot_s_db_time(0,0, window='rectangular', label="RTG")
s11_gated.plot_s_db_time(0,0, window='hamming', label="HTG")
s11_gated.plot_s_db_time(0,0, label="TG")
#s11_w.plot_s_db_time(0,0,label="TGW")


plt.show()