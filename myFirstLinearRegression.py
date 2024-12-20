from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np  # Arrays & Linear Stuff
import pandas as pd  # Data analytics tool
import matplotlib.pyplot as plt  # Graphs and Charts
from IPython.display import clear_output  # Clear the output
from six.moves import urllib
import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

# Load the Titanic dataset
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')  # Training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')  # Testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

# Display the first rows of the training data
print(dftrain.head())

# Plot a histogram of the age column
dftrain.age.hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
