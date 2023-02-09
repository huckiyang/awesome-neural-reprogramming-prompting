import numpy as np
import pickle

from qiskit import IBMQ, transpile, QuantumCircuit
from qiskit.providers.ibmq.managed import IBMQJobManager
from qiskit.circuit import Parameter
from qiskit.circuit.random import random_circuit


# Load the token 
token = ""
IBMQ.enable_account(token)

provider= IBMQ.get_provider(hub = 'ibm-q-hub-ntu', group = 'ntu-internal', project = 'quantum-ml')

backend = provider.get_backend('ibmq_bogota')

device_properties = backend.properties()

with open("ibmq_bogota_noise" + ".txt", "wb") as fp:
	pickle.dump(device_properties, fp)



backend = provider.get_backend('ibmq_rome')

device_properties = backend.properties()

with open("ibmq_rome_noise" + ".txt", "wb") as fp:
	pickle.dump(device_properties, fp)