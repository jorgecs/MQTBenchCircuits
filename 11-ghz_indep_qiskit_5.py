from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend('qasm_simulator')

shots = 10000

qc = QuantumCircuit()

q = QuantumRegister(5, 'q')
meas = ClassicalRegister(5, 'meas')

qc.add_register(q)
qc.add_register(meas)

qc.h(q[4])
qc.cx(q[4], q[3])
qc.cx(q[3], q[2])
qc.cx(q[2], q[1])
qc.cx(q[1], q[0])
qc.measure(q[0], meas[0])
qc.measure(q[1], meas[1])
qc.measure(q[2], meas[2])
qc.measure(q[3], meas[3])
qc.measure(q[4], meas[4])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
