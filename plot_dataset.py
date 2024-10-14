import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_all_connections():
    """
    Reads 'AllData.csv', generates a single graph of all the normalized connection times,
    connected with lines, and saves it as 'AllConnections.pdf'.
    Adjusts the x-axis to handle many days and reduces marker size for clarity.
    """
    # Read the data
    df = pd.read_csv('AllData.csv')

    # Convert 'Timestamp' column to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Sort the DataFrame by Timestamp
    df.sort_values(by='Timestamp', inplace=True)

    # Create a figure
    plt.figure(figsize=(18, 9))

    # Plot the normalized connection times with reduced marker size
    plt.plot(df['Timestamp'], df['Connection Time'], linestyle='-', linewidth=0.5, color='blue')

    # Optionally, plot as a scatter plot with reduced marker size and transparency
    plt.scatter(df['Timestamp'], df['Connection Time'], s=1, color='blue', alpha=0.5)

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Normalized Connection Time')
    plt.title('All Connection Times Over One Year')

    # Set x-axis major locator to monthly interval
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add grid lines for better readability
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Remove legend (since we're only plotting one type of data)
    # plt.legend()

    # Tight layout to ensure everything fits
    plt.tight_layout()

    # Save the figure to a PDF
    plt.savefig('AllConnections.pdf', dpi=300)

    # Show the plot (optional)
    # plt.show()

    print("AllConnections.pdf has been generated.")

# Generate the graph and save to PDF
plot_all_connections()