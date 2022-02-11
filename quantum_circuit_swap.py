import numpy as np
import quantum_computer as qc

result_list = []

for _ in range(1000):
  circuit = qc.QuantumCircuit(2)
  circuit.H(0)
  circuit.SWAP(0,1)
  result_list.append(circuit.measurement())

result_array = np.array(result_list)
print(np.unique(result_array, return_counts=True, axis=0))