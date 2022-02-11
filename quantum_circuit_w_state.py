import numpy as np
import quantum_computer as qc

result_list = []

for _ in range(1000):
  circuit = qc.QuantumCircuit(3)
  circuit.RY(0, 1.9106332362490184)
  circuit.CU(0,1, 0.5*np.pi, 0.5*np.pi, 0.5*np.pi, 0.5*np.pi)
  circuit.CNOT(1,2)
  circuit.CNOT(0,1)
  circuit.NOT(0)
  result_list.append(circuit.measurement())

result_array = np.array(result_list)
print(np.unique(result_array, return_counts=True, axis=0))