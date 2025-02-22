class Qubit:
    """Represents a single qubit in a quantum circuit."""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Qubit: {self.name}>"
