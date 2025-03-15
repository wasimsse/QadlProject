# 🧑‍💻 QADL - Quantum Architecture Description Language

QADL (**Quantum Architecture Description Language**) is a **domain-specific language (DSL)** designed for defining **quantum circuits and architectures**. This project provides a **QADL editor, execution engine, and visualization tools**.

QADL allows users to:
- **Describe** quantum circuits in an intuitive format  
- **Simulate & visualize** quantum operations  
- **Edit, save, and manage** QADL scripts  
- **Execute** and generate graphical representations of circuits  

---

## 🚀 Features
✅ **Quantum Circuit Description** using simple and intuitive syntax  
✅ **Graphical Visualization** of quantum circuits  
✅ **Support for Multiple Gates** (Hadamard, CNOT, X, CZ, etc.)  
✅ **Code Editor with Syntax Highlighting**  
✅ **File Management** (Open, Save, Save As, Edit)  
✅ **Gradio-based GUI** for easy interaction  
✅ **Support for Quantum Algorithms** (Bell State, QFT, Quantum Teleportation)  

---

## 💞 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/wasimsse/QadlProject.git
cd QadlProject
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv_qadl
source venv_qadl/bin/activate  # Mac/Linux
venv_qadl\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Running QADL Editor
```bash
python src/main.py
```

Open your browser and visit:  
**http://127.0.0.1:7860**

---

## 📚 QADL Syntax & Examples

### 1️⃣ Bell State Circuit
```qadl
@startqadl
Circuit BellState {
    qubit q0
    qubit q1

    gate Hadamard q0
    gate CNOT q0 q1

    measure q0 -> c0
    measure q1 -> c1
}
@endqadl
```

### 2️⃣ Quantum Teleportation
```qadl
@startqadl
Circuit QuantumTeleportation {
    qubit q0
    qubit q1
    qubit q2
bit c0 
bit c1 

    gate Hadamard q1
    gate CNOT q1 q2
    gate CNOT q0 q1
    gate Hadamard q0

    measure q0 -> c0
    measure q1 -> c1
}
@endqadl
```

### 3️⃣ Grovers Algorithm
```qadl
@startqadl
Circuit GroversAlgorithm {
    qubit q0
    qubit q1
    qubit q2
    bit c0
    bit c1
    bit  c2
    gate Hadamard q0
    gate X q0
    gate CNOT q0 q1
    gate CNOT q1 q2
    gate X q0
    gate X q2
    gate Hadamard q0
    gate X q0
    gate CNOT q0 q1
    gate CNOT q1 q2
    gate X q0
    gate Hadamard q0

    measure q0 -> c0
    measure q1 -> c1
    measure q2 -> c2
}
@endqadl
```

### 4️⃣ Quantum Fourier Transform (QFT)
```qadl
@startqadl
Circuit QFT3 {
    qubit q0
    qubit q1
    qubit q2

    gate Hadamard q0
    gate CR q1 q0 1/2
    gate CR q2 q0 1/4
    gate Hadamard q1
    gate CR q2 q1 1/2
    gate Hadamard q2
    gate SWAP q0 q2
}
@endqadl
```

---

## 📁 Project Structure
```
QADL_PROJECT/
│── src/
│   ├── qadl_core/        # Core QADL functionality (parsing, execution)
│   │   ├── qadl_parser.py
│   │   ├── qadl_executor.py
│   │   ├── gates.py
│   │   ├── qubits.py
│   │   ├── measurements.py
│   ├── gradio_ui/        # Gradio-based UI components
│   │   ├── main_ui.py
│   ├── utils/            # Helper functions and utilities
│   │   ├── file_handler.py
│   ├── views/            # Stores generated circuit images
│   ├── examples/         # Example QADL scripts
│   ├── main.py           # Entry point for the project
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
```

---

## 🛠️ How to Use QADL
- **Write a QADL Script**: Use the built-in editor to write a quantum circuit.  
- **Run the Script**: Click the "Run QADL" button to execute and visualize.  
- **Save & Load Files**:  
  - Click **Save** to store a QADL file.  
  - Click **Open** to load a QADL script.  
- **View the Output**: The circuit diagram appears on the right.  
- **Modify & Debug**: Edit and rerun scripts as needed.  

---

## 🧩 Supported Quantum Gates

| Gate  | Description                  |
|-------|------------------------------|
| **H** | Hadamard (Creates superposition) |
| **CNOT** | Controlled NOT gate          |
| **X** | Pauli-X gate (bit-flip)      |
| **CZ** | Controlled-Z gate            |
| **SWAP** | Swaps two qubits            |
| **CR** | Controlled Rotation         |

---

## 🤝 Contributing
Want to contribute? Follow these steps:

1️⃣ **Fork the repository**  
2️⃣ **Create a new branch**  
3️⃣ **Make changes & commit**  
4️⃣ **Push to GitHub and open a PR**  

```bash
git checkout -b feature-new
git commit -m "Added new feature"
git push origin feature-new
```

---

## 📄 License
This project is open-source under the **MIT License**.

---

## 🔗 Resources
- 📖 [Qiskit Documentation](https://qiskit.org)  
- 📚 [Quantum Computing Basics - IBM Quantum](https://quantum-computing.ibm.com)  
- 🎓 [Learn Quantum Programming - Quantum Katas](https://github.com/microsoft/QuantumKatas)  
- 💡 [Project Repository: QADL GitHub](https://github.com/wasimsse/QadlProject)  

