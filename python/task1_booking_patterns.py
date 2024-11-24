# Import necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

# Step 1: Load the data from the Excel file into a DataFrame.
# I'm setting up the data path to point to the Excel file where my data resides.
data_path = '../data/2025 DSA Case Study Dataset.xlsx'
df = pd.read_excel(data_path, sheet_name='in')

### Part 1: Monthly Net Orders and Gross Booking Amount ###

# I need to clean the 'booking_window_days' column to make sure it has meaningful values.
# This function takes care of any range values (e.g., "10-20") by averaging the two numbers.
def convert_booking_window(value):
    if isinstance(value, str) and '-' in value:
        start, end = map(int, value.split('-'))
        return (start + end) / 2
    return value

# Apply the cleaning function to create a new column for cleaned booking window values.
df['booking_window_days_cleaned'] = df['booking_window_days'].apply(convert_booking_window)

# Next, I want to aggregate the data by month-year to get the total net orders and total gross booking amount for each month.
# This creates a summary table that I can use to visualize the data monthly.
monthly_summary = df.groupby('bkg_month_year').agg(
    total_net_orders=('net_orders', 'sum'),
    total_gross_booking_amt=('gross_booking_amt', 'sum')
).reset_index()

# Define the width of each bar and set up the x positions for the bars.
bar_width = 0.35
x = range(len(monthly_summary['bkg_month_year']))  # Creating x-axis positions based on the number of months

# Setting up the plot for Monthly Net Orders and Gross Booking Amount with two y-axes.
fig, ax1 = plt.subplots(figsize=(10, 6))

# First, I'm drawing the Net Orders in blue on the primary y-axis (on the left).
# This is the blue bar graph that represents monthly net orders.
# I offset the bars slightly to the left for the Net Orders so that it doesn't overlap with the Gross Booking Amount.
bar1 = ax1.bar(
    [pos - bar_width/2 for pos in x], 
    monthly_summary['total_net_orders'], 
    color='blue', label='Net Orders', width=bar_width, align='center'
)
ax1.set_ylabel('Net Orders', color='blue')  # Labeling the primary y-axis for Net Orders
ax1.yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))  # Formatting y-axis labels to show commas

# Adding annotations on top of each blue bar for Net Orders.
# This makes it easy to see the exact values for each month.
for bar in bar1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:,.0f}', ha='center', va='bottom', color='blue')

# Next, I’m plotting the Gross Booking Amount on a secondary y-axis (on the right).
# These bars are green and are slightly offset to the right.
ax2 = ax1.twinx()
bar2 = ax2.bar(
    [pos + bar_width/2 for pos in x], 
    monthly_summary['total_gross_booking_amt'], 
    color='green', label='Gross Booking Amount', width=bar_width, align='center'
)
ax2.set_ylabel('Gross Booking Amount ($)', color='green')  # Labeling the secondary y-axis for Gross Booking Amount
ax2.yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))  # Formatting y-axis labels to show dollar signs

# Adding annotations on top of each green bar for Gross Booking Amount.
for bar in bar2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval, f'${yval:,.0f}', ha='center', va='bottom', color='green')

# Setting up the title, x-axis labels, and moving the legend outside the plot for clarity.
plt.title('Monthly Net Orders and Gross Booking Amount')
ax1.set_xlabel('Month-Year')
ax1.set_xticks(x)
ax1.set_xticklabels(monthly_summary['bkg_month_year'], rotation=45)
fig.legend(loc="upper left", bbox_to_anchor=(1.05, 1), frameon=False)

# Adding grid lines for both y-axes to improve readability.
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Saving the plot to the output folder
plt.tight_layout()
plt.savefig('../output/monthly_net_orders_and_gross_booking_amount.png')
plt.show()

### Part 2: Family vs Non-Family Bookings ###

# Now, I want to analyze bookings based on family presence.
# This grouping aggregates the total net orders and gross booking amount for family and non-family bookings.
family_summary = df.groupby('if_child_present').agg(
    total_net_orders=('net_orders', 'sum'),
    total_gross_booking_amt=('gross_booking_amt', 'sum')
).reset_index()

# Replace True/False values with 'Family' and 'Non-Family' labels for better readability.
family_summary['if_child_present'] = family_summary['if_child_present'].replace({True: 'Family', False: 'Non-Family'})

# Define the width and x-axis positions for the bars.
bar_width = 0.35
x = np.arange(len(family_summary['if_child_present']))

# Setting up the plot for Family vs Non-Family Bookings.
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting Net Orders in blue for family vs. non-family.
bars1 = ax.bar(
    x - bar_width/2, family_summary['total_net_orders'], color='blue', width=bar_width, label='Net Orders'
)

# Plotting Gross Booking Amount in green for family vs. non-family.
bars2 = ax.bar(
    x + bar_width/2, family_summary['total_gross_booking_amt'], color='green', width=bar_width, label='Gross Booking Amount'
)

# Adding data labels on top of each Net Orders bar for clarity.
for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}', ha='center', va='bottom', color='blue')

# Adding data labels on top of each Gross Booking Amount bar.
for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'${int(yval):,}', ha='center', va='bottom', color='green')

# Setting labels for x-axis and y-axis and giving a title to the plot.
ax.set_xlabel('Family Presence')
ax.set_ylabel('Total (in billions)')
ax.set_title('Family vs Non-Family Bookings')
ax.set_xticks(x)
ax.set_xticklabels(family_summary['if_child_present'])
ax.legend()

# Formatting the y-axis to show values in billions for better readability.
ax.set_yticks([0, 2_000_000_000, 4_000_000_000, 6_000_000_000, 8_000_000_000, 10_000_000_000])
ax.set_yticklabels(['0', '2B', '4B', '6B', '8B', '10B'])

# Adding grid lines on the y-axis for visual clarity.
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Saving the Family vs Non-Family plot to the output folder.
plt.tight_layout()
plt.savefig('../output/family_vs_non_family_bookings_with_net_orders.png')
plt.show()
