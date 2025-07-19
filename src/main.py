from modules.readFFlogsReport import fflogsReader
from modules.analyzeTimelines import makePlots
import numpy as np
import sys

# command line arguments (job & 2 fflogs links)
job = sys.argv[1]
own_fflogs_url = sys.argv[2]
target_fflogs_url = sys.argv[3]

# scrape the data from fflogs
reader = fflogsReader(job = job)

raw_own_tl = reader.getSpellTimeline(url=own_fflogs_url)
raw_target_tl = reader.getSpellTimeline(url=target_fflogs_url)

# analyze the spell timelines and produce a comparison plot
analysis = makePlots(timeline1 = raw_own_tl, timeline2= raw_target_tl, job = job)

analysis.movementSpellPlots()