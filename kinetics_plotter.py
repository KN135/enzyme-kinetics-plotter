import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Michaelis-Menten equation
def michaelis_menten(S, Vmax, Km):
    return (Vmax * S) / (Km + S)


# Enzyme kinetics analysis
def analyze_kinetics(sample_S, sample_V):

    S = np.array(sample_S, dtype=float)
    V = np.array(sample_V, dtype=float)

    # Validate experimental data
    if len(S) != len(V) or len(S) < 3:
        raise ValueError("Provide at least 3 matching data points.")

    if not np.all(np.isfinite(S)) or not np.all(np.isfinite(V)):
        raise ValueError("Data must contain finite numbers.")

    if np.any(S <= 0) or np.any(V <= 0):
        raise ValueError("Concentrations and velocities must be positive.")

    # Non-linear curve fitting
    initial_guess = [max(V) * 1.2, np.median(S)]

    params, covariance = curve_fit(
        michaelis_menten,
        S,
        V,
        p0=initial_guess,
        bounds=(0, np.inf),
        maxfev=10000
    )

    Vmax, Km = params

    print("\n--- ENZYME KINETICS RESULTS ---")
    print(f"Vmax = {Vmax:.3f} umol/min")
    print(f"Km   = {Km:.3f}")

    # Generate smooth curve
    S_fit = np.linspace(0, max(S) * 1.2, 200)
    V_fit = michaelis_menten(S_fit, Vmax, Km)

    # Create visualizations
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Michaelis-Menten plot
    axes[0].scatter(S, V, color="blue", label="Experimental data")
    axes[0].plot(
        S_fit, V_fit,
        color="red",
        label="Non-linear fit"
    )

    axes[0].axhline(
        Vmax, color="green",
        linestyle="--", label="Vmax"
    )

    axes[0].set_title("Michaelis-Menten Plot")
    axes[0].set_xlabel("Substrate Concentration (S)")
    axes[0].set_ylabel("Initial Velocity (V)")
    axes[0].legend()
    axes[0].grid(True)

    # Lineweaver-Burk plot
    reciprocal_S = 1 / S
    reciprocal_V = 1 / V

    x_line = np.linspace(
        -1 / Km * 1.2,
        max(reciprocal_S) * 1.1,
        200
    )

    y_line = (Km / Vmax) * x_line + (1 / Vmax)

    axes[1].scatter(
        reciprocal_S,
        reciprocal_V,
        color="purple",
        label="Experimental data"
    )

    axes[1].plot(
        x_line, y_line,
        color="orange",
        label="Theoretical line"
    )

    axes[1].scatter(
        [-1 / Km],
        [0],
        color="red",
        label="-1/Km"
    )

    axes[1].scatter(
        [0],
        [1 / Vmax],
        color="green",
        label="1/Vmax"
    )

    axes[1].set_title("Lineweaver-Burk Plot")
    axes[1].set_xlabel("1 / Substrate Concentration")
    axes[1].set_ylabel("1 / Initial Velocity")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()

    # Save graph
    plt.savefig(
        "enzyme_kinetics_plots.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("\nPlot saved as enzyme_kinetics_plots.png")

    plt.show()


# Sample experimental data
if __name__ == "__main__":

    sample_S = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    sample_V = [12.1, 21.3, 34.4, 52.0, 61.8, 68.1]

    print("Running enzyme analysis with sample lab data...")

    analyze_kinetics(sample_S, sample_V)
