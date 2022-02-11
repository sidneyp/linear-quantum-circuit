import numpy as np
import random

class QuantumCircuit(object):
  def __init__(self, qubits):

    # Qubit states
    self.state_zero = np.array([1,0])
    self.state_one = np.array([0,1])

    # Circuit initialization
    self.q = qubits*[self.state_zero]

    # 1-bit Quantum gates
    self.H_gate = (1/np.sqrt(2)) * np.array([[1,1],[1,-1]])
    self.S_gate = np.array([[1,0],[0,complex(0,1)]])
    self.Z_gate = np.array([[1,0],[0,-1]])

    # 2-bit Quantum gates
    self.NOT_gate = np.array([[0,1],[1,0]])

  def qubit_prob(self, qubit_idx):
    return abs(self.q[qubit_idx])**2

  def qubit_collapse(self, qubit_idx):
    prob = self.qubit_prob(qubit_idx)
    self.q[qubit_idx] = random.choices(
        [self.state_zero, self.state_one], weights=prob, k=1)[0]
    return self.q[qubit_idx]

  def qubit_collapse_check(self, qubit_idx):
    prob = self.qubit_prob(qubit_idx)
    return random.choices(
        [self.state_zero, self.state_one], weights=prob, k=1)[0]

  def measurement(self):
    circuit_result = []
    for i in range(len(self.q)):
      circuit_result.append(self.qubit_collapse(i)[1])
    return circuit_result

  def measurement_check(self):
    circuit_result = []
    for i in range(len(self.q)):
      circuit_result.append(self.qubit_collapse_check(i)[1])
    return circuit_result

  # 1-bit Quantum gates functions
  def H(self, qubit_idx):
    self.q[qubit_idx] = np.matmul(self.H_gate, self.q[qubit_idx])

  def S(self, qubit_idx):
    self.q[qubit_idx] = np.matmul(self.S_gate, self.q[qubit_idx])

  def NOT(self, qubit_idx):
    self.q[qubit_idx] = np.matmul(self.NOT_gate, self.q[qubit_idx])

  def Z(self, qubit_idx):
    self.q[qubit_idx] = np.matmul(self.Z_gate, self.q[qubit_idx])

  def U(self, qubit_idx, theta, phi, lam):
    U_gate = np.array([[np.cos(0.5*theta), -np.exp(complex(0,1)*lam)*np.sin(0.5*theta)],
                        [np.exp(complex(0,1)*phi)*np.sin(0.5*theta), np.exp(complex(0,1)*(lam+phi))*np.cos(0.5*theta)]])
    self.q[qubit_idx] = np.matmul(U_gate, self.q[qubit_idx])

  def X(self, qubit_idx):
    self.NOT(qubit_idx)

  def RX(self, qubit_idx, theta):
    self.U(qubit_idx, theta, -0.5*np.pi, 0.5*np.pi)

  def RY(self, qubit_idx, theta):
    self.U(qubit_idx, theta, 0, 0)

  # 2-bit Quantum gates functions
  def CNOT(self, qubit_idx_c, qubit_idx_not):
    self.qubit_collapse(qubit_idx_c)
    if np.array_equal(self.q[qubit_idx_c], self.state_one):
      self.NOT(qubit_idx_not)

  def CZ(self, qubit_idx_c, qubit_idx_z):
    if np.array_equal(self.qubit_collapse_check(qubit_idx_c), self.state_one):
      self.Z(qubit_idx_z)

  def SWAP(self, qubit_idx_1, qubit_idx_2):
    temp = self.q[qubit_idx_1]
    self.q[qubit_idx_1] = self.q[qubit_idx_2]
    self.q[qubit_idx_2] = temp

  def CU(self, qubit_idx_c, qubit_idx_u, theta, phi, lam, gamma):
    self.qubit_collapse(qubit_idx_c)
    if np.array_equal(self.q[qubit_idx_c], self.state_one):
      CU_gate = np.array([[np.exp(complex(0,1)*gamma)*np.cos(0.5*theta), -np.exp(complex(0,1)*(gamma+lam))*np.sin(0.5*theta)],
                          [np.exp(complex(0,1)*(gamma+phi))*np.sin(0.5*theta), np.exp(complex(0,1)*(lam+phi+gamma))*np.cos(0.5*theta)]])
      self.q[qubit_idx_u] = np.matmul(CU_gate, self.q[qubit_idx_u])

  # 3-bit Quantum gates functions
  def CCNOT(self, qubit_idx_c_1, qubit_idx_c_2, qubit_idx_not):
    self.qubit_collapse(qubit_idx_c_1)
    self.qubit_collapse(qubit_idx_c_2)
    if np.array_equal(self.q[qubit_idx_c_1], self.state_one) and np.array_equal(self.q[qubit_idx_c_2], self.state_one):
      self.NOT(qubit_idx_not)
