# 📦 Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sympy import primerange
from scipy.interpolate import make_interp_spline
import pandas as pd

# 📌 Parameters
MAX_PRIME = 1_000_000_000
DPI = 300
WIDTH_INCHES = 100
HEIGHT_INCHES = 10

# 🔢 Step 1: Generate primes and compute midpoints, gaps
primes = list(primerange(2, MAX_PRIME))
midpoints, gaps = [], []

for i in range(len(primes) - 1):
    p1, p2 = primes[i], primes[i + 1]
    mid = (p1 + p2) / 2
    gap = p2 - p1
    alt_gap = gap * ((-1) ** i)
    midpoints.append(mid)
    gaps.append(alt_gap)

# 🔣 Step 2: X-axis log10(midpoint)
x_vals = np.log10(midpoints)
y_vals = np.array(gaps)

# 💾 Step 3: Export CSV
df = pd.DataFrame({
    'Prime_1': primes[:-1],
    'Prime_2': primes[1:],
    'Midpoint': midpoints,
    'log10_Midpoint': x_vals,
    'Gap': np.diff(primes),
    'Alternating_Gap': y_vals
})

csv_filename = f"prime_waveform_coords_{MAX_PRIME}.csv"
df.to_csv(csv_filename, index=False)
print(f"✅ CSV exported: {csv_filename}")

# 🌊 Step 4: Smooth waveform using cubic spline
num_points = 20000
x_smooth = np.linspace(x_vals.min(), x_vals.max(), num_points)
spline = make_interp_spline(x_vals, y_vals, k=3)
y_smooth = spline(x_smooth)

# 🖌️ Step 5: Build variable-width segments
points = np.array([x_smooth, y_smooth]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
n = len(segments)
line_widths = np.linspace(3.0, 0.3, n)
colors = [(0.25, 0.45, 0.75, 1)] * n  # Steel blue

lc = LineCollection(segments, linewidths=line_widths, colors=colors)

# 🖼️ Step 6: Plot and export
fig, ax = plt.subplots(figsize=(WIDTH_INCHES, HEIGHT_INCHES), dpi=DPI)
ax.add_collection(lc)
ax.axhline(0, color='black', linewidth=0.3, linestyle='--')
ax.set_xlim(x_smooth.min(), x_smooth.max())
ax.set_ylim(y_smooth.min() - 2, y_smooth.max() + 2)
ax.set_title(f"Prime Waveform (Smooth + Fading Width, up to {MAX_PRIME})", fontsize=18)
ax.set_xlabel("log10(Midpoint Between Consecutive Primes)", fontsize=14)
ax.set_ylabel("Alternating Prime Gaps", fontsize=14)
ax.grid(True, alpha=0.2)

# 🔽 Step 7: Save as PNG + SVG
png_filename = f"prime_waveform_smooth_fade_{MAX_PRIME}.png"
svg_filename = f"prime_waveform_smooth_fade_{MAX_PRIME}.svg"

fig.savefig(png_filename, dpi=DPI, bbox_inches='tight')
fig.savefig(svg_filename, format='svg', bbox_inches='tight')

print(f"✅ PNG exported: {png_filename}")
print(f"✅ SVG exported: {svg_filename}")

input("Press Enter to exit...")
