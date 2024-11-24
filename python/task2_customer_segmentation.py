import pandas as pd

# Load the data
data_path = '../data/2025 DSA Case Study Dataset.xlsx'
df = pd.read_excel(data_path, sheet_name='in')

# Clean the 'booking_window_days' column to handle any ranges or non-numeric values
def convert_booking_window(value):
    if isinstance(value, str) and '-' in value:
        start, end = map(int, value.split('-'))
        return (start + end) / 2
    elif isinstance(value, (int, float)):  # Keep numeric values as is
        return value
    return None  # Return None if not numeric

# Apply the cleaning function to booking window days
df['booking_window_days_cleaned'] = df['booking_window_days'].apply(convert_booking_window)

# Convert 'length_of_stay' to numeric, setting non-numeric values to NaN
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')

# Segment 1: Family Travelers
family_travelers = df[df['if_child_present'] == True]

# Calculate metrics for Family Travelers
family_metrics = {
    'Total Net Orders': family_travelers['net_orders'].sum(),
    'Total Gross Booking Amount': family_travelers['gross_booking_amt'].sum(),
    'Average Length of Stay (Days)': family_travelers['length_of_stay'].mean(),
    'Average Booking Window (Days)': family_travelers['booking_window_days_cleaned'].mean()
}

# Segment 2: Non-Family Travelers
non_family_travelers = df[df['if_child_present'] == False]

# Calculate metrics for Non-Family Travelers
non_family_metrics = {
    'Total Net Orders': non_family_travelers['net_orders'].sum(),
    'Total Gross Booking Amount': non_family_travelers['gross_booking_amt'].sum(),
    'Average Length of Stay (Days)': non_family_travelers['length_of_stay'].mean(),
    'Average Booking Window (Days)': non_family_travelers['booking_window_days_cleaned'].mean()
}

# Display the metrics for both segments
print("Family Travelers Metrics:", family_metrics)
print("Non-Family Travelers Metrics:", non_family_metrics)
