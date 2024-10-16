import matplotlib.pyplot as plt

def plot_float_values(file_path):
    """
    Reads float values from a file, where each value is on a separate line,
    and plots them with x-axis as the sequence number and y-axis as the value.
    """
    # Read the float values from the file
    with open(file_path, 'r') as file:
        values = [float(line.strip()) for line in file if line.strip()]

    # Generate sequence numbers for the x-axis
    x_values = list(range(1, len(values) + 1))

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(x_values, values, linestyle='-', marker='o', markersize=2)

    # Set labels and title
    plt.xlabel('Sequence Number')
    plt.ylabel('Value')
    plt.title('Plot of Float Values')

    # Show grid for better readability
    plt.grid(True)

    # Adjust layout to prevent clipping
    plt.tight_layout()

    # Save the plot as a PDF file
    plt.savefig('SimpleDDoSNormalizedTimes.pdf', dpi=300)

    # Optional: Display the plot window
    # plt.show()

    print("Plot has been saved as 'SimpleDDoSNormalizedTimes.pdf'.")

# Example usage:
# Replace 'values.txt' with the path to your file containing the float values
plot_float_values('SimpleDDoSNormalizedTimes.csv')