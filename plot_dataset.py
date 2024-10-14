import pandas as pd
import matplotlib.pyplot as plt

def plot_all_connections():
    """
    Reads 'AllData.csv', generates a single graph of all the normalized connection times,
    connected with lines, and saves it as 'AllConnections.pdf'.
    """
    # Read the data
    df = pd.read_csv('AllData.csv')

    # Convert 'Timestamp' column to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Sort the DataFrame by Timestamp
    df.sort_values(by='Timestamp', inplace=True)

    # Create a figure
    plt.figure(figsize=(12, 6))

    # Plot the normalized connection times with lines
    plt.plot(df['Timestamp'], df['Connection Time'], marker='o', linestyle='-', label='Connection Time')

    # Add labels and title
    plt.xlabel('Timestamp')
    plt.ylabel('Normalized Connection Time')
    plt.title('All Connection Times')

    # Add grid lines for better readability
    plt.grid(True)

    # Adjust x-axis labels
    plt.xticks(rotation=45)

    # Add a legend
    plt.legend()

    # Tight layout to ensure everything fits
    plt.tight_layout()

    # Save the figure to a PDF
    plt.savefig('AllConnections.pdf')

    # Show the plot (optional)
    # plt.show()

    print("AllConnections.pdf has been generated.")

# Generate the graph and save to PDF
plot_all_connections()