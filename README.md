# linear-quantum-circuit
Trying to simulate a quantum circuit linearly.

The idea behind making a linear simulation of a quantum circuit is by
collapsing the quantum states in binary when two or more qubits interact.

In this approach, the n qubits are represented by n superposition state vectors
in two-dimensional Hilbert space. While the standard representation for n qubits
is one superposition state vector in 2<sup>n</sup> dimensional Hilbert space. [Source](https://en.wikipedia.org/wiki/Qubit)

Our quantum circuit simulation works for several small circuits. However, there
are larger circuits that this method fails, such as Grover's algorithm circuit.


| Circuit                     | Script                           | Working? |
|-----------------------------|----------------------------------|----------|
| NOT gate                    | quantum_circuit_not.py           | Yes      |
| SWAP gate                   | quantum_circuit_swap.py          | Yes      |
| SWAP with CNOT gates        | quantum_circuit_cnot_swap.py     | Yes      |
| Double H                    | quantum_circuit_double_h.py      | Yes      |
| Bell test                   | quantum_circuit_bell.py          | Yes      |
| GHZ state                   | quantum_circuit_ghz.py           | Yes      |
| W state                     | quantum_circuit_w_state.py       | Yes      |
| Grover's algorithm          | quantum_circuit_grover_alg.py    | No       |
| Grover's algorithm N=2 A=00 | quantum_circuit_grover_n2_a00.py | No       |
