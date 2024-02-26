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

qc.ry(1.7376841305223034, q[0])
qc.ry(1.4598019857964233, q[1])
qc.ry(3 * np.pi / 8, q[2])
qc.x(q[3])
qc.x(q[4])
qc.cx(q[1], q[0])
qc.ry(1.3166149125118367, q[0])
qc.cx(q[1], q[0])
qc.u(0 / 2, 0, 0, q[2])

qc.cx(q[0], q[2])

qc.u(-1 * 0 / 2, 0, 0, q[2])

qc.cx(q[0], q[2])

qc.u(0 / 2, 0, 0, q[2])

qc.cx(q[1], q[2])

qc.u(-1 * 0 / 2, 0, 0, q[2])

qc.cx(q[1], q[2])

qc.x(q[1])
qc.ccx(q[1], q[4], q[3])
qc.x(q[1])
qc.cx(q[3], q[2])
qc.u(0.2942523647695425, 0, 0, q[2])
qc.cx(q[3], q[2])
qc.u(0.2942523647695425, -np.pi, -np.pi, q[2])
qc.cx(q[3], q[2])
qc.u(-0.1144919077447111, 0, 0, q[2])
qc.cx(q[3], q[2])
qc.u(0.1144919077447111, 0, 0, q[2])
qc.ccx(q[3], q[0], q[2])
qc.cx(q[3], q[2])
qc.u(0.1144919077447111, 0, 0, q[2])
qc.cx(q[3], q[2])
qc.u(-0.1144919077447111, 0, 0, q[2])
qc.ccx(q[3], q[0], q[2])
qc.cx(q[3], q[2])
qc.u(-0.2289838154894222, 0, 0, q[2])
qc.cx(q[3], q[2])
qc.u(0.2289838154894222, 0, 0, q[2])
qc.ccx(q[3], q[1], q[2])
qc.cx(q[3], q[2])
qc.u(0.2289838154894222, 0, 0, q[2])
qc.cx(q[3], q[2])
qc.u(-0.2289838154894222, 0, 0, q[2])
qc.ccx(q[3], q[1], q[2])
qc.x(q[1])
qc.ccx(q[1], q[4], q[3])
qc.x(q[1])
qc.x(q[3])
qc.x(q[4])
qc.measure(q[0], meas[0])
qc.measure(q[1], meas[1])
qc.measure(q[2], meas[2])
qc.measure(q[3], meas[3])
qc.measure(q[4], meas[4])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
