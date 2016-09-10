import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt

z = pd.read_json('http://moatsearch-data.s3.amazonaws.com/homework/ad_classification_hw_dataset.json')
desc = z.describe
print desc

