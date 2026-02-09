# Graphical Abstract

This directory contains the graphical abstract for the paper "A Lightweight and Practical UAV Authentication System Implementation based on Proof-of-History Blockchain".

## File: graphical_abstract.png

The graphical abstract visually represents the complete workflow of the UAV authentication system:

### Components Illustrated:

1. **UAV (Left)**: Shows the drone collecting telemetry data
   - GPS coordinates
   - Altitude measurements
   - Velocity data
   - Timestamps

2. **Authentication (Center-Left)**: Cryptographic verification layer
   - ECC (Elliptic Curve Cryptography) signature
   - Verification of encrypted telemetry

3. **PoH Engine (Center-Right)**: Core innovation
   - Sequential hashing mechanism
   - SHA-256 cryptographic function
   - Formula: H_i = SHA256(H_{i-1} || T_i || D_i)

4. **Immutable Ledger (Right)**: Final storage
   - Tamper-evident timeline
   - Blockchain-based verification
   - Mathematical proof of integrity

### Key Benefits Highlighted:

- **Lightweight**: 120K hashes per second
- **Low Latency**: 12-18 millisecond authentication
- **Secure**: Tamper-proof logging
- **Practical**: Works on COTS (Commercial Off-The-Shelf) hardware
- **Verifiable**: Mathematical proof of data integrity

## Generation

The graphical abstract was generated using Python and matplotlib. To regenerate:

```bash
python3 create_graphical_abstract.py
```

This will create/update `Fig/graphical_abstract.png` with high resolution (300 DPI) suitable for publication.

## Usage in LaTeX

The graphical abstract is included in the paper's LaTeX source (`elsarticle-template-num.tex`) within the `\begin{graphicalabstract}...\end{graphicalabstract}` environment:

```latex
\begin{graphicalabstract}
\includegraphics[width=\linewidth]{Fig/graphical_abstract.png}
\end{graphicalabstract}
```

## Specifications

- **Format**: PNG
- **Resolution**: 300 DPI (publication quality)
- **Dimensions**: 4170 x 2370 pixels
- **Size**: ~289 KB
- **Color Mode**: RGBA
