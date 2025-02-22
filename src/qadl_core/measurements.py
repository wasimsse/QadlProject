class Measurement:
    """Represents a quantum measurement operation."""

    def __init__(self, qubit, classical_bit):
        self.qubit = qubit
        self.classical_bit = classical_bit

    def __repr__(self):
        return f"<Measurement: {self.qubit} -> {self.classical_bit}>"
