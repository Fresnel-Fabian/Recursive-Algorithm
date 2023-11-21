import random
import matplotlib.pyplot as plt


def estimate_pi(num_samples):
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25:  # Check if the point is inside the circle
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate, x_inside, y_inside, x_outside, y_outside


if __name__ == "__main__":
    num_samples = 1000  # Adjust the number of samples for accuracy
    estimated_pi, x_in, y_in, x_out, y_out = estimate_pi(num_samples)

    # Plot the results
    plt.figure(figsize=(6, 6))
    plt.scatter(x_in, y_in, color='blue', s=2, label='Inside Circle')
    plt.scatter(x_out, y_out, color='red', s=2, label='Outside Circle')
    circle = plt.Circle((0.5, 0.5), 0.5, color='green', fill=False, lw=1, label='Full Circle')
    plt.gca().add_patch(circle)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Estimation of π: {estimated_pi:.5f}")
    plt.legend()
    plt.show()
