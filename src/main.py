from modules.readFFlogsReport import fflogsReader
from modules.analyzeTimelines import makePlots
import numpy as np


## get the 2 fflogs url's and the specified job from the command line


## read the timeline data from the 2 provided fflogs links
reader = fflogsReader(job = 'Scholar')
raw_own_tl = reader.getSpellTimeline(url='https://www.fflogs.com/reports/P61L2rqMpYRQJjfW?fight=196')
raw_target_tl = reader.getSpellTimeline(url='https://www.fflogs.com/reports/6bZHqT3VnF9vp2m8?fight=7')

## write fflogs data to text files, so the analysis can be developed without
## repeatedly scraping the data 

# np.savetxt('own_tl_from_file.txt', np.array(own_timeline), fmt='%s')
# np.savetxt('target_tl_from_file.txt', np.array(target_timeline), fmt='%s')


## analyze the spell timelines and produce a comparison plot
analysis = makePlots(timeline1 = raw_own_tl, timeline2= raw_target_tl, job = 'Scholar')

own_timeline = analysis.timeToFloat(raw_own_tl)
target_timeline = analysis.timeToFloat(raw_target_tl)

analysis.movementSpellPlots(own_timeline=own_timeline, target_timeline=target_timeline)