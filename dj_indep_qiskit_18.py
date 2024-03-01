from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend('qasm_simulator')

shots = 10000

qc = QuantumCircuit()

q = QuantumRegister(18, 'q')
c = ClassicalRegister(18, 'c')

qc.add_register(q)
qc.add_register(c)

qc.u(np.pi / 2, 0, 0, q[0])

qc.u(np.pi / 2, 0, 0, q[1])

qc.h(q[2])
qc.u(np.pi / 2, 0, 0, q[3])

qc.h(q[4])
qc.u(np.pi / 2, 0, 0, q[5])

qc.u(np.pi / 2, 0, 0, q[6])

qc.h(q[7])
qc.u(np.pi / 2, 0, 0, q[8])

qc.u(np.pi / 2, 0, 0, q[9])

qc.h(q[10])
qc.u(np.pi / 2, 0, 0, q[11])

qc.u(np.pi / 2, 0, 0, q[12])

qc.h(q[13])
qc.h(q[14])
qc.u(np.pi / 2, 0, 0, q[15])

qc.h(q[16])
qc.u(np.pi / 2, -np.pi, -np.pi, q[17])

qc.cx(q[0], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[0])

qc.cx(q[1], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[1])

qc.cx(q[2], q[17])
qc.h(q[2])
qc.cx(q[3], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[3])

qc.cx(q[4], q[17])
qc.h(q[4])
qc.cx(q[5], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[5])

qc.cx(q[6], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[6])

qc.cx(q[7], q[17])
qc.h(q[7])
qc.cx(q[8], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[8])

qc.cx(q[9], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[9])

qc.cx(q[10], q[17])
qc.h(q[10])
qc.cx(q[11], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[11])

qc.cx(q[12], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[12])

qc.cx(q[13], q[17])
qc.h(q[13])
qc.cx(q[14], q[17])
qc.h(q[14])
qc.cx(q[15], q[17])
qc.u(np.pi / 2, -np.pi, -np.pi, q[15])

qc.cx(q[16], q[17])
qc.h(q[16])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])
qc.measure(q[3], c[3])
qc.measure(q[4], c[4])
qc.measure(q[5], c[5])
qc.measure(q[6], c[6])
qc.measure(q[7], c[7])
qc.measure(q[8], c[8])
qc.measure(q[9], c[9])
qc.measure(q[10], c[10])
qc.measure(q[11], c[11])
qc.measure(q[12], c[12])
qc.measure(q[13], c[13])
qc.measure(q[14], c[14])
qc.measure(q[15], c[15])
qc.measure(q[16], c[16])
qc.measure(q[17], c[17])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
