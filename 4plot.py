import matplotlib.pyplot as plt
from skrf import Network
nw = Network

fig = plt.figure(figsize=(9,8))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222); ax2.grid()
ax3 = fig.add_subplot(223, projection='polar')
ax4 = fig.add_subplot(224); ax4.grid()

# nw.plot_s_smith(m=0,n=0,
#                 r=1,
#                 chart_type='z',
#                 ax=ax1,
#                 show_legend=True,
#                 draw_labels=True,
#                 draw_vswr=True)

nw.plot_s_db(m=1,n=0,
             ax=ax2,
             title='S21 (in dB)')

nw.plot_s_polar(m=0,n=1,
                ax=ax3,
                title='S12 in polar')

nw.plot_s_complex(m=1,n=1,
                  ax=ax4,
                  title='S22 complex plane')


fig.tight_layout()
plt.show()
