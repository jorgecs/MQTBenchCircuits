from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend('qasm_simulator')

shots = 10000

qc = QuantumCircuit()

q = QuantumRegister(8, 'q')
meas = ClassicalRegister(8, 'meas')

qc.add_register(q)
qc.add_register(meas)

qc.ry(-np.pi / 4, q[0])
qc.ry(-0.9553166181245093, q[1])
qc.ry(-np.pi / 3, q[2])
qc.ry(-1.1071487177940904, q[3])
qc.ry(-1.1502619915109316, q[4])
qc.ry(-1.183199640139716, q[5])
qc.ry(-1.2094292028881888, q[6])
qc.x(q[7])
qc.cz(q[7], q[6])
qc.ry(1.2094292028881888, q[6])
qc.cz(q[6], q[5])
qc.ry(1.183199640139716, q[5])
qc.cx(q[6], q[7])
qc.cz(q[5], q[4])
qc.ry(1.1502619915109316, q[4])
qc.cx(q[5], q[6])
qc.cz(q[4], q[3])
qc.ry(1.1071487177940904, q[3])
qc.cx(q[4], q[5])
qc.cz(q[3], q[2])
qc.ry(np.pi / 3, q[2])
qc.cx(q[3], q[4])
qc.cz(q[2], q[1])
qc.ry(0.9553166181245093, q[1])
qc.cx(q[2], q[3])
qc.cz(q[1], q[0])
qc.ry(np.pi / 4, q[0])
qc.cx(q[1], q[2])
qc.cx(q[0], q[1])
qc.measure(q[0], meas[0])
qc.measure(q[1], meas[1])
qc.measure(q[2], meas[2])
qc.measure(q[3], meas[3])
qc.measure(q[4], meas[4])
qc.measure(q[5], meas[5])
qc.measure(q[6], meas[6])
qc.measure(q[7], meas[7])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
