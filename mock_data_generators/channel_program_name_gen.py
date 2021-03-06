'''
Copyright 2019 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This script generates the CRM account data's Channel Program Name.
'''


import numpy as np
from itertools import groupby
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("crm_account.csv")
mu = 3
sigma = 0.4
lv = np.random.normal(mu, sigma, 2500)
lv = [int(i) for i in lv]
print(min(lv))
print(max(lv))
data['Channel Program Name'] = lv
count, bins, ignored = plt.hist(lv, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.show()
data.to_csv("crm_account_temp.csv")
