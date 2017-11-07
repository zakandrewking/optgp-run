#!/usr/bin/env python3

import cobra
from cobra.flux_analysis import sample

model = cobra.io.load_json_model('data/iJO1366.json')

res = sample(model, 1200, method='optgp', processes=12)

from IPython import embed; embed()
