# enzyme-kinetics-plotter
# 🧬 Enzyme Kinetics Calculator & Plotter

A Python-based scientific computing project designed to analyze enzyme-catalyzed reactions using experimental substrate concentration and initial velocity data.

The program estimates important kinetic parameters, including **Maximum Velocity (Vmax)** and **Michaelis Constant (Km)** using nonlinear regression.

## 🚀 Features

- **Michaelis-Menten Analysis:** Models enzyme reaction kinetics.
- **Nonlinear Regression:** Uses SciPy's `curve_fit` to estimate Vmax and Km.
- **Michaelis-Menten Plot:** Visualizes experimental data and fitted curves.
- **Lineweaver-Burk Plot:** Generates a double-reciprocal representation.
- **Parameter Estimation:** Calculates kinetic parameters automatically.
- **Graph Export:** Saves high-resolution plots as PNG files.

## 🛠️ Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/enzyme-kinetics-plotter.git
```

Move into the project folder:

```bash
cd enzyme-kinetics-plotter
```

Install the required packages:

```bash
pip install numpy scipy matplotlib
```

## ▶️ How to Run

Execute the Python script:

```bash
python kinetics_plotter.py
```

The program will:
1. Load the sample experimental data.
2. Estimate Vmax and Km.
3. Generate Michaelis-Menten and Lineweaver-Burk plots.
4. Save the figure as `enzyme_kinetics_plots.png`.

## 🧪 Sample Experimental Data

| Substrate Concentration (S) | Initial Velocity (V) |
|---:|---:|
| 0.5 | 12.1 |
| 1.0 | 21.3 |
| 2.0 | 34.4 |
| 5.0 | 52.0 |
| 10.0 | 61.8 |
| 20.0 | 68.1 |

## 📊 Scientific Background

The Michaelis-Menten equation:

\[
V = \frac{V_{max}[S]}{K_m+[S]}
\]

Where:

- V = Initial reaction velocity
- Vmax = Maximum reaction velocity
- Km = Michaelis constant
- [S] = Substrate concentration

## 📁 Project Structure

```text
enzyme-kinetics-plotter/
│
├── kinetics_plotter.py
├── README.md
└── enzyme_kinetics_plots.png
```

## 🎯 Project Objective

This project demonstrates the application of Python programming, scientific computing, nonlinear regression, and data visualization in biochemical research.

## 👨‍💻 Author

YOUR NAME

GitHub: https://github.com/KN135

---

*Developed as a scientific computing project for enzyme kinetics analysis.*
