# File: src/qadl_core/qadl_executor.py

import os
import traceback
from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
from qadl_core.qubits import Qubit
from qadl_core.gates import HadamardGate, CNOTGate, XGate, CZGate
from qadl_core.measurements import Measurement
from qadl_core.qadl_parser import parse_qadl

def execute_qadl_script(script):
    """
    Executes a QADL script and generates a quantum circuit image.
    Handles errors gracefully.
    """
    try:
        # ✅ Parse the QADL script
        circuit_def = parse_qadl(script)
        num_qubits = len(circuit_def.qubits)
        num_classical_bits = len(circuit_def.classical_bits)

        # ✅ Initialize QuantumCircuit
        qc = QuantumCircuit(num_qubits, num_classical_bits)

        # ✅ Fix: Ensure proper indexing
        qubit_index = {qubit.name: idx for idx, qubit in enumerate(circuit_def.qubits)}
        classical_bit_index = {bit: idx for idx, bit in enumerate(circuit_def.classical_bits)}

        # ✅ Apply gates
        for gate in circuit_def.gates:
            try:
                if isinstance(gate, HadamardGate):
                    qc.h(qubit_index[gate.qubit])  
                elif isinstance(gate, XGate):
                    qc.x(qubit_index[gate.qubit])  
                elif isinstance(gate, CNOTGate):
                    qc.cx(qubit_index[gate.control], qubit_index[gate.target])
                elif isinstance(gate, CZGate):
                    qc.cz(qubit_index[gate.control], qubit_index[gate.target])
                else:
                    raise ValueError(f"Unsupported gate: {gate}")
            except KeyError as ke:
                raise ValueError(f"Invalid gate qubit reference: {ke}")

        # ✅ Apply measurements
        for measurement in circuit_def.measurements:
            if measurement.qubit in qubit_index and measurement.classical_bit in classical_bit_index:
                qc.measure(qubit_index[measurement.qubit], classical_bit_index[measurement.classical_bit])
            else:
                raise ValueError(f"Invalid measurement mapping: {measurement.qubit} -> {measurement.classical_bit}")

        # ✅ Ensure output directory exists
        os.makedirs("views", exist_ok=True)  

        # ✅ Save circuit image
        image_path = f"views/{circuit_def.name}_circuit.png"
        circuit_drawer(qc, output="mpl", filename=image_path)

        return f"✅ Successfully executed {circuit_def.name}", image_path

    except SyntaxError as se:
        return f"❌ Execution Error: {se}", None
    except KeyError as ke:
        return f"❌ Mapping Error: Invalid qubit or bit reference - {ke}", None
    except ValueError as ve:
        return f"❌ Gate Error: {ve}", None
    except Exception as e:
        error_msg = traceback.format_exc()
        return f"❌ Critical Error: {e}\n{error_msg}", None
