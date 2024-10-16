import pandas as pd
import random
from datetime import timedelta, datetime

def generate_fixed_connection_times():
    """
    Generates simulated internet connection times for a car's onboard computer with specific weekday and location adjustments.
    Generates multiple connections per period in chronological order.
    Generates data for the entire year.
    Saves two CSV files:
    - 'AllData.csv' containing all generated data.
    - 'NormalizedTimes.csv' containing only the normalized times.
    """
    num_days = 365  # Simulate 365 days for the entire year
    start_date = pd.Timestamp('2023-01-01')  # Start on January 1, 2023

    # Initialize lists to store data
    connection_times = []
    connection_hours = []
    connection_types = []
    simulation_days = []
    dates = []
    timestamps = []
    weekdays = []
    weekday_names = []
    locations = []

    # Define location codes
    location_codes = {
        'Home': 10,
        'Work': 20,
        'Other': 30
    }

    # Number of packets per period
    packets_per_period = {
        'Nightly': 10,
        'Morning': 10,
        'Work End': 10,
        'Shopping': 10
    }

    # Generate data for each day
    for day_offset in range(num_days):
        current_date = start_date + timedelta(days=day_offset)
        week_day = current_date.weekday() + 1  # Adjust to make Monday=1, Sunday=7

        # Simulation Day starts from 1
        sim_day = day_offset + 1

        if week_day <= 5:  # Monday to Friday
            # Connections at Home
            location = 'Home'
            location_code = location_codes[location]
            integer_part = location_code + week_day  # Consistent integer part for Home

            # Nightly at Home
            # Generate sorted list of connection hours
            connection_hours_list = sorted([random.uniform(3.0, 4.0) for _ in range(packets_per_period['Nightly'])])
            for connection_hour in connection_hours_list:
                connection_type = 'Nightly'
                time_offset = ((connection_hour - 12) / 12) * 0.9999  # Negative value
                if time_offset < 0:
                    connection_time_value = (-integer_part) + time_offset
                else:
                    connection_time_value = integer_part + time_offset

                dates.append(current_date)
                timestamps.append(datetime.combine(current_date, datetime.min.time()) + timedelta(hours=connection_hour))
                connection_times.append(connection_time_value)
                connection_hours.append(connection_hour)
                connection_types.append(connection_type)
                simulation_days.append(sim_day)
                weekdays.append(week_day)
                weekday_names.append(current_date.strftime('%A'))
                locations.append(location)

            # Morning at Home
            connection_hours_list = sorted([random.uniform(6.5, 7.0) for _ in range(packets_per_period['Morning'])])
            for connection_hour in connection_hours_list:
                connection_type = 'Morning'
                time_offset = ((connection_hour - 12) / 12) * 0.9999  # Negative value
                if time_offset < 0:
                    connection_time_value = (-integer_part) + time_offset
                else:
                    connection_time_value = integer_part + time_offset

                dates.append(current_date)
                timestamps.append(datetime.combine(current_date, datetime.min.time()) + timedelta(hours=connection_hour))
                connection_times.append(connection_time_value)
                connection_hours.append(connection_hour)
                connection_types.append(connection_type)
                simulation_days.append(sim_day)
                weekdays.append(week_day)
                weekday_names.append(current_date.strftime('%A'))
                locations.append(location)

            # Work End
            location = 'Work'
            location_code = location_codes[location]
            integer_part = location_code + week_day

            connection_hours_list = sorted([random.uniform(16.0, 16.5) for _ in range(packets_per_period['Work End'])])
            for connection_hour in connection_hours_list:
                connection_type = 'Work End'
                time_offset = ((connection_hour - 12) / 12) * 0.9999  # Positive value
                if time_offset < 0:
                    connection_time_value = (-integer_part) + time_offset
                else:
                    connection_time_value = integer_part + time_offset

                dates.append(current_date)
                timestamps.append(datetime.combine(current_date, datetime.min.time()) + timedelta(hours=connection_hour))
                connection_times.append(connection_time_value)
                connection_hours.append(connection_hour)
                connection_types.append(connection_type)
                simulation_days.append(sim_day)
                weekdays.append(week_day)
                weekday_names.append(current_date.strftime('%A'))
                locations.append(location)

        elif week_day == 6:  # Saturday
            # Shopping connections
            for _ in range(packets_per_period['Shopping']):
                # Shopping Start from Home
                location = 'Home'
                location_code = location_codes[location]
                integer_part = location_code + week_day

                shopping_start_time = random.uniform(14.0, 16.0)
                connection_hour = shopping_start_time
                connection_type = 'Shopping Start'
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                if time_offset < 0:
                    connection_time_value = (-integer_part) + time_offset
                else:
                    connection_time_value = integer_part + time_offset

                dates.append(current_date)
                timestamps.append(datetime.combine(current_date, datetime.min.time()) + timedelta(hours=connection_hour))
                connection_times.append(connection_time_value)
                connection_hours.append(connection_hour)
                connection_types.append(connection_type)
                simulation_days.append(sim_day)
                weekdays.append(week_day)
                weekday_names.append(current_date.strftime('%A'))
                locations.append(location)

                # Corresponding Shopping End at Other
                location = 'Other'
                location_code = location_codes[location]
                integer_part = location_code + week_day

                shopping_duration = random.uniform(1.75, 2.25)  # Duration between 1.75 to 2.25 hours
                shopping_end_time = shopping_start_time + shopping_duration
                connection_hour = shopping_end_time
                connection_type = 'Shopping End'
                time_offset = ((connection_hour - 12) / 12) * 0.9999
                if time_offset < 0:
                    connection_time_value = (-integer_part) + time_offset
                else:
                    connection_time_value = integer_part + time_offset

                dates.append(current_date)
                timestamps.append(datetime.combine(current_date, datetime.min.time()) + timedelta(hours=connection_hour))
                connection_times.append(connection_time_value)
                connection_hours.append(connection_hour)
                connection_types.append(connection_type)
                simulation_days.append(sim_day)
                weekdays.append(week_day)
                weekday_names.append(current_date.strftime('%A'))
                locations.append(location)

        else:  # Sunday
            # No connections
            continue

    # Create a DataFrame with separate rows for each connection time
    df = pd.DataFrame({
        'Date': dates,
        'Timestamp': timestamps,
        'Simulation Day': simulation_days,
        'Weekday': weekdays,
        'Weekday Name': weekday_names,
        'Location': locations,
        'Connection Type': connection_types,
        'Connection Hour': connection_hours,
        'Connection Time': connection_times
    })

    # Sort the DataFrame by Timestamp to ensure chronological order
    df.sort_values(by='Timestamp', inplace=True)

    # Save to CSV files
    df.to_csv('AllData.csv', index=False)

    # Create the second CSV with only normalized times
    df_normalized = df[['Connection Time']]
    df_normalized.to_csv('NormalizedTimes.csv', index=False)

    return df, df_normalized

# Generate the data and save to files
df_all, df_normalized = generate_fixed_connection_times()
print("AllData.csv and NormalizedTimes.csv have been generated.")