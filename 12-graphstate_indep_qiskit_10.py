from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend('qasm_simulator')

shots = 10000

qc = QuantumCircuit()

q = QuantumRegister(10, 'q')
meas = ClassicalRegister(10, 'meas')

qc.add_register(q)
qc.add_register(meas)

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])
qc.h(q[4])
qc.h(q[5])
qc.h(q[6])
qc.h(q[7])
qc.h(q[8])
qc.h(q[9])
qc.cz(q[0], q[1])
qc.cz(q[2], q[3])
qc.cz(q[1], q[4])
qc.cz(q[3], q[4])
qc.cz(q[0], q[6])
qc.cz(q[5], q[6])
qc.cz(q[5], q[7])
qc.cz(q[7], q[8])
qc.cz(q[2], q[9])
qc.cz(q[8], q[9])
qc.measure(q[0], meas[0])
qc.measure(q[1], meas[1])
qc.measure(q[2], meas[2])
qc.measure(q[3], meas[3])
qc.measure(q[4], meas[4])
qc.measure(q[5], meas[5])
qc.measure(q[6], meas[6])
qc.measure(q[7], meas[7])
qc.measure(q[8], meas[8])
qc.measure(q[9], meas[9])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
