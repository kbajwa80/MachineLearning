#!/usr/bin/python
import subprocess
subprocess.call(['python', './get-pip.py'])
subprocess.call(['yum', 'install', 'gcc*'])
subprocess.call(['pip', 'install', 'pandas'])
subprocess.call(['pip', 'install', 'pystan'])
subprocess.call(['pip', 'install', 'plotly'])
subprocess.call(['pip', 'install', 'fbprophet'])

