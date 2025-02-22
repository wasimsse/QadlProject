# File: src/qadl_core/quantum_circuit.py

class QuantumCircuitDef:
    """
    Represents a quantum circuit definition from QADL.
    """

    def __init__(self, name, qubits=None, classical_bits=None, gates=None, measurements=None):
        self.name = name
        self.qubits = qubits if qubits else []
        self.classical_bits = classical_bits if classical_bits else []
        self.gates = gates if gates else []
        self.measurements = measurements if measurements else []

    def add_qubit(self, qubit):
        """Adds a qubit to the circuit."""
        self.qubits.append(qubit)

    def add_classical_bit(self, bit):
        """Adds a classical bit to the circuit."""
        self.classical_bits.append(bit)

    def add_gate(self, gate):
        """Adds a gate operation to the circuit."""
        self.gates.append(gate)

    def add_measurement(self, measurement):
        """Adds a measurement to the circuit."""
        self.measurements.append(measurement)

    def __repr__(self):
        return f"QuantumCircuitDef(name={self.name}, qubits={self.qubits}, classical_bits={self.classical_bits}, gates={self.gates}, measurements={self.measurements})"
