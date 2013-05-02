#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

f = open('/home/leomcabrall/github/cminfo/analisys.txt', 'r')
s = f.read()
f.close()

lines = [x for x in s.split('\n') if x != '']

downstream_signoise = [x.split(',')[2].replace(' dB', '') for x in lines]
data = [x.split(',')[0].replace(' dB', '') for x in lines]
t = zip(data, downstream_signoise)

plt.plot(downstream_signoise)
plt.ylabel('Downstream signal noise')
plt.xlabel('Horario')
plt.show()
