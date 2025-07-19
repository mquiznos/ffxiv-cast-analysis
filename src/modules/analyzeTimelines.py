import numpy as np
import matplotlib.pyplot as plt

class makePlots:
    def __init__(self, timeline1, timeline2, job):
        self.job = job
        self.timeline1 = timeline1
        self.timeline2 = timeline2

        if job == 'Scholar':
            self.spell_plot_style = 'ro' 

    def timeToFloat(self, time_string_list):
        time_min = np.array([float(time_string_list[i][:2]) for i in range(len(time_string_list))])
        time_sec = np.array([float(time_string_list[i][3:5]) for i in range(len(time_string_list))])
        time_ms  = np.array([float(time_string_list[i][6:]) for i in range(len(time_string_list))])

        converted_time = time_ms + 1000*time_sec + 60*1000*time_min

        return converted_time

    def movementSpellPlots(self, own_timeline, target_timeline):
        vertical_offset = 1
        x_upper_bound = max(own_timeline[-1], target_timeline[-1])

        # create lists for the horizontal tick marks and labels (spaced by 1 minute)
        x_ticks = []
        t=0
        while t*60000 < x_upper_bound:
            x_ticks.append(t*60000)
            t += 1

        x_tick_labels = []
        t=0
        while t*60000 < x_upper_bound:
            x_tick_labels.append(str(t)+':00')
            t += 1

        y_ticks = [-vertical_offset,vertical_offset]
        y_tick_labels = ['Target','Self']

        plt.figure(figsize=(9, 4), dpi=80)

        plt.plot(own_timeline, np.zeros_like(own_timeline)+vertical_offset, self.spell_plot_style)
        plt.plot(target_timeline, np.zeros_like(target_timeline)-vertical_offset, self.spell_plot_style)

        plt.xlim(0,x_upper_bound)
        plt.ylim(-2*vertical_offset, 2*vertical_offset)

        plt.xticks(x_ticks, x_tick_labels)
        plt.yticks(y_ticks, y_tick_labels)
        plt.axhline(0, color='black', linewidth=.5)
        plt.axvline(0, color='black', linewidth=.5)
        plt.grid(visible=True, which='major')
        plt.savefig('result.png')