import uuid
import time
import matplotlib
import matplotlib.pyplot as plt
import random
from pylsl import StreamInfo, StreamOutlet

warmup_trials = 2
trials_per_class = 5
perform_time = 3.5
wait_time = 1
pause_every = 30
pause_duration = 10 
fontsize = 50 
labels = ['IG', 'G', 'IR', 'R']
markers = ['imag_grasp', ' grasp', 'imag_release', 'release']

matplotlib.rcParams.update({'font.size': fontsize})


info = StreamInfo(name='MotorImag-Markers', type='Markers', channel_count=1,
                  nominal_srate=0, channel_format='string',
                  source_id='t8u43t98u')
outlet = StreamOutlet(info)

print("Press [Enter] to begin.")
x = input()

hFigure, ax = plt.subplots()
ax.set_yticklabels([''])
ax.set_xticklabels([''])
t = plt.text(0.5, 0.5, '', horizontalalignment='center')
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=0, ymax=1)
plt.ion()
plt.draw()
plt.show()
choice = 0
try:
    for trial in range(1, warmup_trials+trials_per_class*len(labels)+1):
        choice = 0
        while choice < len(labels):
            print(choice)
            if not plt.fignum_exists(hFigure.number):
                break
            t.set_text(labels[choice])
            if trial == warmup_trials:
                outlet.push_sample(['calib-begin'])
            if trial > warmup_trials:
                outlet.push_sample([markers[choice]])
            hFigure.canvas.draw()
            hFigure.canvas.flush_events()
            time.sleep(perform_time)
            t.set_text('')
            hFigure.canvas.draw()
            hFigure.canvas.flush_events()
            time.sleep(wait_time)
            if trial % pause_every == 0:
                t.set_text('Pause')
                hFigure.canvas.draw()
                hFigure.canvas.flush_events()
                time.sleep(pause_duration)
                t.set_text('')
            hFigure.canvas.draw()
            hFigure.canvas.flush_events()
            choice += 1
        print(f'Completed {trial} trial')
        
except Exception as e:
    print(e)
outlet.push_sample(['calib-end'])
