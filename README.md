# Prime Number Waveform • Visualizing Prime Gaps up to 1 Billion

This project provides Python scripts and datasets to generate **prime gap waveforms** — a novel visual representation of the gaps between consecutive prime numbers. Using the **logarithmic midpoint** between each prime pair and alternating the prime gaps in sign, the result is a striking, continuous waveform with both signal-like structure and emergent patterns.

## 📌 What This Project Does

- Generates coordinate pairs: `x = log10(midpoint of prime pair)`, `y = ±(prime gap)`
- Produces smooth, high-resolution **waveform plots (PNG + SVG)**
- Supports waveform generation up to **1 billion natural numbers**
- Optionally exports coordinate data to **CSV files** for further analysis

## 💡 Why It’s Useful

- Creates the first known **visual archive of prime gap behavior at this scale**
- Offers a reproducible framework for:
  - Mathematical pattern exploration
  - Educational demonstrations
  - Data-driven signal analysis (without traditional signal tools)
- Can support further research in number theory or AI pattern detection

## 📚 Dataset & Paper

- 📦 Full datasets up to 1 Billion numbers: Zenodo DOI [https://zenodo.org/records/15636895]
- 📝 Preprint (coming soon): [arXiv link]

## 🙋‍♂️ Who Maintains This

Created and maintained by Shashaank C D, independent researcher.
This is part of an open-access contribution to mathematical exploration.
Feel free to open issues or submit pull requests!

## 📬 Contact
✉️ Email: cdshashaank@outlook.com
🌐 ORCID: 0009-0006-0174-189X
🔗 LinkedIn: Shashaank CD

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and share with attribution.

## 🚀 Getting Started

### Requirements

Make sure you have Python 3.8+ and the following libraries:

```bash
pip install sympy matplotlib pandas numpy scipy


