
import skrf as rf
rf.stylely()
from pylab import *

# load data for the waveguide to CPW probe
probe = rf.Network('C:/test.s2p')

# we will focus on s11
s11 = probe.s11

#  time-gate the first largest reflection
s11_gated = s11.time_gate(center=0, span=.2, t_unit='ns')
s11_gated.name='gated probe'

# plot frequency and time-domain s-parameters
figure(figsize=(8,4))
subplot(121)
s11.plot_s_db()
s11_gated.plot_s_db()
title('Frequency Domain')

subplot(122)
s11.plot_s_db_time()
s11_gated.plot_s_db_time()
title('Time Domain')
tight_layout()