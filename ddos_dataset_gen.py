import pandas as pd
import random
from datetime import timedelta, datetime

def generate_fixed_connection_times():
    """
    Generates simulated internet connections for a car's onboard computer with specific adjustments for weekdays and location.
    Generates multiple connections in each period for better simulation of real use cases.
    Generates data for the entire year.
    Adds an anomaly resembling a DDoS attack.
    Saves two CSV files:
    - 'AllData.csv' containing all the generated data.
    - 'NormalizedTimes.csv' containing only the normalized times.
    """
    num_days = 365  # Simulating 365 days for the whole year
    start_date = pd.Timestamp('2023-01-01')  # Starting on January 1, 2023

    # Initializing lists to store data
    connection_times = []
    connection_hours = []
    connection_types = []
    simulation_days = []
    dates = []
    timestamps = []
    weekdays = []
    weekday_names = []
    locations = []

    # Defining location codes
    location_codes = {
        'Home': 10,
        'Work': 20,
        'Other': 30
    }

    # Number of packets in each period
    packets_per_period = {
        'Nightly': 10,
        'Morning': 10,
        'Work End': 10,
        'Shopping': 10
    }

    # Settings for DDoS attack anomaly
    ddos_week_number = random.randint(1, 52)  # Select a random week in the year
    ddos_date = start_date + timedelta(weeks=ddos_week_number - 1, days=6)  # Set the date to Sunday of that week
    ddos_time_start = 14.0  # 14:00 (2 PM)
    ddos_duration_minutes = 10
    ddos_packets = 150

    # Generating data for each day
    for day_offset in range(num_days):
        current_date = start_date + timedelta(days=day_offset)
        week_day = current_date.weekday() + 1  # Adjust to make Monday=1, Sunday=7

        # Simulation day number starts from 1
        sim_day = day_offset + 1

        if current_date == ddos_date:
            # Generating DDoS anomaly
            location = 'Other'
            location_code = location_codes[location]
            integer_part = location_code + week_day

            # Generating timestamps for the DDoS attack
            ddos_timestamps = sorted([ddos_time_start + random.uniform(0, ddos_duration_minutes / 60) for _ in range(ddos_packets)])
            for connection_hour in ddos_timestamps:
                connection_type = 'DDoS Attack'
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
            continue  # Skip further generation for this day (Sunday with anomaly)

        if week_day <= 5:  # Monday to Friday
            # Home connections
            location = 'Home'
            location_code = location_codes[location]
            integer_part = location_code + week_day  # Consistent integer part for home

            # Nightly connections at home
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

            # Morning connections at home
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

            # End of work
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
                # Start of shopping from home
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

                # End of shopping at "Other"
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
            # No connections, unless it's a DDoS attack day
            continue

    # Creating a DataFrame with individual connections
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

    # Sorting the DataFrame by Timestamp for chronological order
    df.sort_values(by='Timestamp', inplace=True)

    # Saving to CSV files
    df.to_csv('AllData.csv', index=False)

    # Creating a second CSV file with only normalized times
    df_normalized = df[['Connection Time']]
    df_normalized.to_csv('DDoSNormalizedTimes.csv', index=False)

    print(f"DDoS attack generated on {ddos_date.strftime('%Y-%m-%d')} at 14:00.")

    return df, df_normalized

# Generate the data and save to CSV files
df_all, df_normalized = generate_fixed_connection_times()