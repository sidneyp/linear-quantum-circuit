import numpy as np
import quantum_computer as qc

result_list = []

#NOT WORKING
#MAYBE PROBLEM IS IN CZ
for _ in range(1000):
  circuit = qc.QuantumCircuit(2)
  circuit.H(0)
  circuit.H(1)
  circuit.X(0)
  circuit.X(1)
  circuit.CZ(0,1)
  circuit.X(0)
  circuit.X(1)
  circuit.H(0)
  circuit.H(1)
  circuit.Z(0)
  circuit.Z(1)
  circuit.CZ(0,1)
  circuit.H(0)
  circuit.H(1)

  result_list.append(circuit.measurement())

result_array = np.array(result_list)
print(np.unique(result_array, return_counts=True, axis=0))