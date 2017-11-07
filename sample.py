#!/usr/bin/env python3

import cobra
from cobra.flux_analysis import sample

model = cobra.io.load_json_model('data/iJO1366.json')

# 1200 is the number of samples to obtain. When using 'optgp' this must be a
# multiple of `processes`, otherwise a larger number of samples will be
# returned.
res = sample(model, 1200, method='optgp', processes=12)

from IPython import embed; embed()
