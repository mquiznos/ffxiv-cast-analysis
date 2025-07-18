from modules.readFFlogsReport import fflogsReader
import numpy as np


## get the 2 fflogs url's and the specified job from the command line


## read the timeline data from the 2 provided fflogs links

# reader = fflogsReader(job = 'Scholar')
# own_timeline = reader.getSpellTimeline(url='https://www.fflogs.com/reports/P61L2rqMpYRQJjfW?fight=196')
# target_timeline = reader.getSpellTimeline(url='https://www.fflogs.com/reports/6bZHqT3VnF9vp2m8?fight=7')

## write fflogs data to text files, so the analysis can be developed without
## repeatedly scraping the data 

# np.savetxt('own_tl_from_file.txt', np.array(own_timeline), fmt='%s')
# np.savetxt('target_tl_from_file.txt', np.array(target_timeline), fmt='%s')

## analysis module call goes here