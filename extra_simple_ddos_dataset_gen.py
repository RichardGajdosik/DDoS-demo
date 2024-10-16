import pandas as pd
import random
from datetime import timedelta, datetime

def generate_simple_normalized_times_with_ddos():
    """
    Generates simulated internet connection times for a car's onboard computer.
    Generates multiple connections per period in chronological order.
    Generates data for the entire year.
    Adds an anomaly resembling a DDoS attack.
    Saves a CSV file:
    - 'SimpleNormalizedTimes.csv' containing only the normalized times between -1 and 1.
    """
    num_days = 365  # Simulating 365 days for the whole year
    start_date = pd.Timestamp('2023-01-01')  # Starting on January 1, 2023

    # Initialize list to store connection times
    connection_times = []

    # Number of packets in each period
    packets_per_period = {
        'Nightly': 1,
        'Morning': 1,
        'Work End': 1,
        'Shopping': 1
    }

    # Settings for DDoS attack anomaly
    ddos_week_number = random.randint(1, 52)  # Select a random week in the year
    ddos_date = start_date + timedelta(weeks=ddos_week_number - 1, days=6)  # Set the date to Sunday of that week
    ddos_time_start = 14.0  # 14:00 (2 PM)
    ddos_duration_minutes = 10
    ddos_packets = 150

    # Generate data for each day
    for day_offset in range(num_days):
        current_date = start_date + timedelta(days=day_offset)
        week_day = current_date.weekday() + 1  # Adjust to make Monday=1, Sunday=7

        if current_date == ddos_date:
            # Generating DDoS anomaly
            # Generating timestamps for the DDoS attack
            ddos_timestamps = sorted([ddos_time_start + random.uniform(0, ddos_duration_minutes / 60) for _ in range(ddos_packets)])
            for connection_hour in ddos_timestamps:
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                connection_time_value = time_offset
                connection_times.append(connection_time_value)
            continue  # Skip further generation for this day (Sunday with anomaly)

        if week_day <= 5:  # Monday to Friday
            # Nightly connections
            connection_hours_list = sorted([random.uniform(3.0, 4.0) for _ in range(packets_per_period['Nightly'])])
            for connection_hour in connection_hours_list:
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                connection_time_value = time_offset
                connection_times.append(connection_time_value)

            # Morning connections
            connection_hours_list = sorted([random.uniform(6.5, 7.0) for _ in range(packets_per_period['Morning'])])
            for connection_hour in connection_hours_list:
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                connection_time_value = time_offset
                connection_times.append(connection_time_value)

            # Work End connections
            connection_hours_list = sorted([random.uniform(16.0, 16.5) for _ in range(packets_per_period['Work End'])])
            for connection_hour in connection_hours_list:
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                connection_time_value = time_offset
                connection_times.append(connection_time_value)

        elif week_day == 6:  # Saturday
            # Shopping connections
            for _ in range(packets_per_period['Shopping']):
                # Shopping Start
                shopping_start_time = random.uniform(14.0, 16.0)
                connection_hour = shopping_start_time
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                connection_time_value = time_offset
                connection_times.append(connection_time_value)

                # Shopping End
                shopping_duration = random.uniform(1.75, 2.25)  # Duration between 1.75 to 2.25 hours
                shopping_end_time = shopping_start_time + shopping_duration
                connection_hour = shopping_end_time
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                connection_time_value = time_offset
                connection_times.append(connection_time_value)

        else:  # Sunday
            # No connections, unless it's a DDoS attack day
            continue

    # Note: Removed the sorting step to preserve the original order
    # connection_times.sort()

    # Save to CSV file
    df_normalized = pd.DataFrame({'Connection Time': connection_times})
    df_normalized.to_csv('ExtraSimpleDDoSNormalizedTimes.csv', index=False)

    print(f"SimpleNormalizedTimes.csv has been generated with DDoS attack on {ddos_date.strftime('%Y-%m-%d')} at 14:00.")

    return df_normalized

# Generate the data and save to CSV file
df_normalized = generate_simple_normalized_times_with_ddos()