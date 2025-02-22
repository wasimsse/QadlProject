# File: src/qadl_core/gates.py

class HadamardGate:
    """Represents a Hadamard gate."""
    def __init__(self, qubit):
        """Initialize with a single qubit."""
        self.qubit = qubit

    def __repr__(self):
        return f"HadamardGate({self.qubit})"


class CNOTGate:
    """Represents a CNOT (Controlled-NOT) gate."""
    def __init__(self, control, target):
        """Initialize with a control and target qubit."""
        self.control = control
        self.target = target

    def __repr__(self):
        return f"CNOTGate(control={self.control}, target={self.target})"


class XGate:
    """Represents an X (Pauli-X) gate."""
    def __init__(self, qubit):
        """Initialize with a single qubit."""
        self.qubit = qubit

    def __repr__(self):
        return f"XGate({self.qubit})"


class CZGate:
    """Represents a CZ (Controlled-Z) gate."""
    def __init__(self, control, target):
        """Initialize with a control and target qubit."""
        self.control = control
        self.target = target

    def __repr__(self):
        return f"CZGate(control={self.control}, target={self.target})"


# New: Dictionary for easy lookup (useful in parser)
GATE_CLASSES = {
    "Hadamard": HadamardGate,
    "CNOT": CNOTGate,
    "X": XGate,
    "CZ": CZGate
}
