# File: src/qadl_core/qadl_parser.py

import re
from qadl_core.quantum_circuit import QuantumCircuitDef
from qadl_core.qubits import Qubit
from qadl_core.measurements import Measurement
from qadl_core.gates import HadamardGate, CNOTGate, XGate, CZGate

def parse_qadl(script):
    """
    Parses a QADL script and returns a QuantumCircuitDef object.
    Handles syntax validation and structured parsing.
    """
    lines = script.strip().split("\n")
    
    # ✅ Ensure the script starts and ends correctly
    if not lines[0].strip().lower().startswith("@startqadl"):
        raise SyntaxError("Syntax error on line 1: Missing '@startqadl'")
    if not lines[-1].strip().lower().startswith("@endqadl"):
        raise SyntaxError("Syntax error on last line: Missing '@endqadl'")

    circuit_name = None
    qubits = []
    classical_bits = []
    gates = []
    measurements = []
    inside_circuit = False  # Track circuit block

    for i, line in enumerate(lines[1:-1], start=2):  # Skip @startqadl and @endqadl
        line = line.strip()
        if not line or line.startswith("//"):  # Ignore empty lines & comments
            continue
        
        # ✅ Circuit declaration
        if line.lower().startswith("circuit "):
            match = re.match(r"Circuit\s+(\w+)\s*\{?", line, re.IGNORECASE)
            if match:
                circuit_name = match.group(1)
                inside_circuit = True  
            else:
                raise SyntaxError(f"Syntax error on line {i}: Invalid circuit declaration")

        # ✅ Closing bracket validation
        elif line == "}":
            if inside_circuit:
                inside_circuit = False  
            else:
                raise SyntaxError(f"Syntax error on line {i}: Unexpected closing bracket '}}'")

        # ✅ Qubit declaration
        elif line.lower().startswith("qubit "):
            match = re.match(r"qubit\s+(\w+)", line, re.IGNORECASE)
            if match:
                qubit_name = match.group(1)
                if qubit_name in [q.name for q in qubits]:  
                    raise SyntaxError(f"Syntax error on line {i}: Duplicate qubit name '{qubit_name}'")
                qubits.append(Qubit(qubit_name))
            else:
                raise SyntaxError(f"Syntax error on line {i}: Invalid qubit declaration")
        
        # ✅ Classical Bit declaration
        elif line.lower().startswith("bit "):
            match = re.match(r"bit\s+(\w+)", line, re.IGNORECASE)
            if match:
                bit_name = match.group(1)
                if bit_name in classical_bits:
                    raise SyntaxError(f"Syntax error on line {i}: Duplicate classical bit '{bit_name}'")
                classical_bits.append(bit_name)
            else:
                raise SyntaxError(f"Syntax error on line {i}: Invalid classical bit declaration")

        # ✅ Gate operations
        elif line.lower().startswith("gate "):
            match = re.match(r"gate\s+(\w+)\s+([\w\s,]+)", line, re.IGNORECASE)
            if match:
                gate_name, qubit_list = match.groups()
                qubit_names = qubit_list.split()

                # 🎯 Handle different gate types
                if gate_name.lower() == "hadamard":
                    if len(qubit_names) != 1:
                        raise SyntaxError(f"Syntax error on line {i}: Hadamard gate requires exactly one qubit")
                    gates.append(HadamardGate(qubit_names[0]))

                elif gate_name.lower() == "cnot":
                    if len(qubit_names) != 2:
                        raise SyntaxError(f"Syntax error on line {i}: CNOT requires exactly two qubits (control & target)")
                    gates.append(CNOTGate(control=qubit_names[0], target=qubit_names[1]))

                elif gate_name.lower() == "x":
                    if len(qubit_names) != 1:
                        raise SyntaxError(f"Syntax error on line {i}: X gate requires exactly one qubit")
                    gates.append(XGate(qubit_names[0]))

                elif gate_name.lower() == "cz":
                    if len(qubit_names) != 2:
                        raise SyntaxError(f"Syntax error on line {i}: CZ requires exactly two qubits (control & target)")
                    gates.append(CZGate(control=qubit_names[0], target=qubit_names[1]))

                else:
                    raise SyntaxError(f"Syntax error on line {i}: Unknown gate '{gate_name}'")
            else:
                raise SyntaxError(f"Syntax error on line {i}: Invalid gate format")

        # ✅ Measurement validation
        elif line.lower().startswith("measure "):
            match = re.match(r"measure\s+(\w+)\s*->\s*(\w+)", line, re.IGNORECASE)
            if match:
                qubit, classical_bit = match.groups()
                if qubit not in [q.name for q in qubits]:  
                    raise SyntaxError(f"Syntax error on line {i}: Undefined qubit '{qubit}' in measurement")
                if classical_bit not in classical_bits:  
                    raise SyntaxError(f"Syntax error on line {i}: Undefined classical bit '{classical_bit}' in measurement")
                measurements.append(Measurement(qubit, classical_bit))
            else:
                raise SyntaxError(f"Syntax error on line {i}: Invalid measurement format")

        # 🚨 Handle unknown statements
        else:
            raise SyntaxError(f"Syntax error on line {i}: Unrecognized statement: {line}")

    # ✅ Ensure a valid circuit was defined
    if not circuit_name:
        raise SyntaxError("No valid circuit definition found.")

    return QuantumCircuitDef(circuit_name, qubits, classical_bits, gates, measurements)
