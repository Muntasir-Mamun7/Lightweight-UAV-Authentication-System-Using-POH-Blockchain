#!/usr/bin/env python3
"""
Create a graphical abstract for the UAV PoH Blockchain paper.
This script generates a visual representation of the lightweight UAV authentication system.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.lines as mlines
import numpy as np

# Set up the figure with high DPI for publication quality
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

# Define colors matching a professional academic style
color_uav = '#3498db'  # Blue
color_auth = '#e74c3c'  # Red
color_poh = '#f39c12'  # Orange
color_ledger = '#27ae60'  # Green
color_arrow = '#34495e'  # Dark gray
color_bg = '#ecf0f1'  # Light gray background

# Title
ax.text(7, 7.5, 'Lightweight UAV Authentication System', 
        ha='center', va='top', fontsize=20, fontweight='bold', color='#2c3e50')
ax.text(7, 7.1, 'Using Proof-of-History Blockchain', 
        ha='center', va='top', fontsize=16, color='#34495e')

# ========== SECTION 1: UAV (Left) ==========
# UAV Icon representation
uav_x, uav_y = 1.5, 4.5
uav_box = FancyBboxPatch((uav_x - 0.6, uav_y - 0.6), 1.2, 1.2,
                         boxstyle="round,pad=0.1", 
                         edgecolor=color_uav, facecolor=color_uav, 
                         linewidth=3, alpha=0.3)
ax.add_patch(uav_box)

# UAV symbol (simplified drone icon)
ax.plot([uav_x-0.3, uav_x+0.3], [uav_y, uav_y], color=color_uav, linewidth=4)
ax.plot([uav_x, uav_x], [uav_y-0.2, uav_y+0.2], color=color_uav, linewidth=4)
# Propellers
for dx, dy in [(-0.3, 0.2), (0.3, 0.2), (-0.3, -0.2), (0.3, -0.2)]:
    circle = Circle((uav_x + dx, uav_y + dy), 0.08, color=color_uav, alpha=0.7)
    ax.add_patch(circle)

ax.text(uav_x, uav_y - 1.0, 'UAV', ha='center', va='top', 
        fontsize=14, fontweight='bold', color=color_uav)

# Telemetry data list
telemetry = ['GPS', 'Altitude', 'Velocity', 'Timestamp']
for i, item in enumerate(telemetry):
    ax.text(uav_x, uav_y - 1.3 - i*0.25, f'• {item}', ha='center', va='top', 
            fontsize=9, color='#34495e')

# ========== SECTION 2: Authentication (Center-Left) ==========
auth_x, auth_y = 4.5, 4.5

# Authentication box
auth_box = FancyBboxPatch((auth_x - 0.8, auth_y - 0.8), 1.6, 1.6,
                          boxstyle="round,pad=0.1", 
                          edgecolor=color_auth, facecolor=color_auth, 
                          linewidth=3, alpha=0.2)
ax.add_patch(auth_box)

# Key symbol
ax.text(auth_x, auth_y + 0.2, '🔐', ha='center', va='center', fontsize=40)

ax.text(auth_x, auth_y - 1.0, 'Authentication', ha='center', va='top', 
        fontsize=14, fontweight='bold', color=color_auth)
ax.text(auth_x, auth_y - 1.3, 'ECC Signature', ha='center', va='top', 
        fontsize=10, color='#34495e')
ax.text(auth_x, auth_y - 1.55, 'Verification', ha='center', va='top', 
        fontsize=10, color='#34495e')

# Arrow from UAV to Auth
arrow1 = FancyArrowPatch((uav_x + 0.7, uav_y), (auth_x - 0.9, auth_y),
                         arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color=color_arrow, alpha=0.7)
ax.add_patch(arrow1)
ax.text((uav_x + auth_x) / 2, uav_y + 0.4, 'Encrypted', ha='center', 
        fontsize=9, style='italic', color=color_arrow)
ax.text((uav_x + auth_x) / 2, uav_y + 0.15, 'Telemetry', ha='center', 
        fontsize=9, style='italic', color=color_arrow)

# ========== SECTION 3: PoH Engine (Center-Right) ==========
poh_x, poh_y = 7.5, 4.5

# PoH Engine box
poh_box = FancyBboxPatch((poh_x - 0.9, poh_y - 0.9), 1.8, 1.8,
                         boxstyle="round,pad=0.1", 
                         edgecolor=color_poh, facecolor=color_poh, 
                         linewidth=3, alpha=0.2)
ax.add_patch(poh_box)

# Hash chain visualization
hash_y_start = poh_y + 0.3
for i in range(3):
    y_pos = hash_y_start - i * 0.3
    rect = Rectangle((poh_x - 0.4, y_pos - 0.08), 0.8, 0.16, 
                     edgecolor=color_poh, facecolor=color_poh, 
                     linewidth=2, alpha=0.6)
    ax.add_patch(rect)
    if i < 2:
        ax.arrow(poh_x, y_pos - 0.08, 0, -0.06, 
                head_width=0.1, head_length=0.03, fc=color_poh, ec=color_poh)

ax.text(poh_x, poh_y - 1.1, 'PoH Engine', ha='center', va='top', 
        fontsize=14, fontweight='bold', color=color_poh)
ax.text(poh_x, poh_y - 1.4, 'Sequential Hashing', ha='center', va='top', 
        fontsize=10, color='#34495e')
ax.text(poh_x, poh_y - 1.65, 'SHA-256', ha='center', va='top', 
        fontsize=10, color='#34495e')

# Arrow from Auth to PoH
arrow2 = FancyArrowPatch((auth_x + 0.9, auth_y), (poh_x - 1.0, poh_y),
                         arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color=color_arrow, alpha=0.7)
ax.add_patch(arrow2)
ax.text((auth_x + poh_x) / 2, auth_y + 0.4, 'Verified', ha='center', 
        fontsize=9, style='italic', color=color_arrow)
ax.text((auth_x + poh_x) / 2, auth_y + 0.15, 'Data', ha='center', 
        fontsize=9, style='italic', color=color_arrow)

# ========== SECTION 4: Immutable Ledger (Right) ==========
ledger_x, ledger_y = 11, 4.5

# Ledger representation
ledger_box = FancyBboxPatch((ledger_x - 0.9, ledger_y - 0.9), 1.8, 1.8,
                            boxstyle="round,pad=0.1", 
                            edgecolor=color_ledger, facecolor=color_ledger, 
                            linewidth=3, alpha=0.2)
ax.add_patch(ledger_box)

# Blockchain blocks
block_size = 0.25
for i in range(3):
    for j in range(2):
        x_pos = ledger_x - 0.35 + j * 0.35
        y_pos = ledger_y + 0.4 - i * 0.35
        block = Rectangle((x_pos - block_size/2, y_pos - block_size/2), 
                         block_size, block_size,
                         edgecolor=color_ledger, facecolor='white', 
                         linewidth=2)
        ax.add_patch(block)
        # Chain links
        if i < 2:
            ax.plot([x_pos, x_pos], [y_pos - block_size/2, y_pos - block_size/2 - 0.1],
                   color=color_ledger, linewidth=1.5)

ax.text(ledger_x, ledger_y - 1.1, 'Immutable Ledger', ha='center', va='top', 
        fontsize=14, fontweight='bold', color=color_ledger)
ax.text(ledger_x, ledger_y - 1.4, 'Tamper-Evident', ha='center', va='top', 
        fontsize=10, color='#34495e')
ax.text(ledger_x, ledger_y - 1.65, 'Timeline', ha='center', va='top', 
        fontsize=10, color='#34495e')

# Arrow from PoH to Ledger
arrow3 = FancyArrowPatch((poh_x + 1.0, poh_y), (ledger_x - 1.0, ledger_y),
                         arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color=color_arrow, alpha=0.7)
ax.add_patch(arrow3)
ax.text((poh_x + ledger_x) / 2, poh_y + 0.4, 'Cryptographic', ha='center', 
        fontsize=9, style='italic', color=color_arrow)
ax.text((poh_x + ledger_x) / 2, poh_y + 0.15, 'Proof', ha='center', 
        fontsize=9, style='italic', color=color_arrow)

# ========== SECTION 5: Key Benefits (Bottom) ==========
benefits_y = 1.5

# Benefit boxes
benefits = [
    ('⚡', 'Lightweight', '120K hash/s', 1.8),
    ('⚡', 'Low Latency', '12-18 ms', 4.5),
    ('🛡️', 'Secure', 'Tamper-proof', 7.2),
    ('✓', 'Practical', 'COTS Hardware', 9.9),
    ('📊', 'Verifiable', 'Mathematical Proof', 12.6)
]

for emoji, title, desc, x_pos in benefits:
    # Background box
    benefit_box = FancyBboxPatch((x_pos - 0.6, benefits_y - 0.4), 1.2, 0.8,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#bdc3c7', facecolor='#ecf0f1', 
                                linewidth=2, alpha=0.5)
    ax.add_patch(benefit_box)
    
    ax.text(x_pos, benefits_y + 0.2, emoji, ha='center', va='center', fontsize=18)
    ax.text(x_pos, benefits_y - 0.05, title, ha='center', va='center', 
            fontsize=9, fontweight='bold', color='#2c3e50')
    ax.text(x_pos, benefits_y - 0.28, desc, ha='center', va='center', 
            fontsize=7, color='#7f8c8d')

# ========== Mathematical Formula (Top Center) ==========
formula_box = FancyBboxPatch((4.5, 6.0), 5, 0.6,
                            boxstyle="round,pad=0.1", 
                            edgecolor='#95a5a6', facecolor='white', 
                            linewidth=2, alpha=0.8)
ax.add_patch(formula_box)

ax.text(7, 6.3, r'$H_i = \mathsf{SHA256}(H_{i-1} \parallel T_i \parallel D_i)$', 
        ha='center', va='center', fontsize=13, color='#2c3e50',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='none', alpha=0.9))

# Add subtle background
background = Rectangle((0, 0), 14, 8, facecolor=color_bg, alpha=0.3, zorder=-1)
ax.add_patch(background)

plt.tight_layout()
plt.savefig('/home/runner/work/Lightweight-UAV-Authentication-System-Using-POH-Blockchain/Lightweight-UAV-Authentication-System-Using-POH-Blockchain/Fig/graphical_abstract.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("Graphical abstract created successfully: Fig/graphical_abstract.png")
plt.close()
