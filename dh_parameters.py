from coppeliasim_zmqremoteapi_client import RemoteAPIClient

import numpy as np

#setting up sim vvv
client = RemoteAPIClient()
sim = client.require('sim')

