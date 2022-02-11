import numpy as np
import quantum_computer as qc

result_list = []

for _ in range(1000):
  circuit = qc.QuantumCircuit(3)
  circuit.H(0)
  circuit.CNOT(0,1)
  circuit.CNOT(0,2)
  result_list.append(circuit.measurement())

result_array = np.array(result_list)
print(np.unique(result_array, return_counts=True, axis=0))