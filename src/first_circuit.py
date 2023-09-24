from qiskit import *

qc = QuantumCircuit(3)

qc.h(0)
qc.h(1)
qc.x(0)
qc.x(1)

qc.draw()
