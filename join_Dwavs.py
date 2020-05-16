#!/usr/bin/env python3
from pydub import AudioSegment
import glob

basename = 'mn20_025a'
directory = ''

filenames = glob.glob(directory, concatenate(basename,'???.wav'), recursive = False)
filenames.sort()

n = 1
for fn in filenames:
	if n = 1:
		combined = AudioSegment.from_wav(fn)
	else:
		combined = combined + AudioSegment.from_wav(fn)
	n+=1

combined.export("%s_combined" % basename, format = 'wav')