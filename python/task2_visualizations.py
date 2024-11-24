import matplotlib.pyplot as plt
import numpy as np

# Data for visualization
family_travelers_metrics = {
    'Total Net Orders': 4457498,
    'Total Gross Booking Amount': 3251474902,
    'Average Length of Stay (Days)': 2.68,
    'Average Booking Window (Days)': 26.79
}

non_family_travelers_metrics = {
    'Total Net Orders': 20844790,
    'Total Gross Booking Amount': 10130646882,
    'Average Length of Stay (Days)': 2.73,
    'Average Booking Window (Days)': 23.16
}

# Set up bar width for both charts
bar_width = 0.35

### Part 1: Bar Chart for Average Booking Window and Length of Stay ###
# Define the metrics and corresponding values for family and non-family travelers
labels = ['Average Length of Stay (Days)', 'Average Booking Window (Days)']
family_values = [family_travelers_metrics[label] for label in labels]
non_family_values = [non_family_travelers_metrics[label] for label in labels]

# X positions for bars
x = np.arange(len(labels))

# Create figure and axis for the first plot
fig, ax = plt.subplots()
bar1 = ax.bar(x - bar_width/2, family_values, bar_width, label='Family Travelers', color='blue')
bar2 = ax.bar(x + bar_width/2, non_family_values, bar_width, label='Non-Family Travelers', color='green')

# Adding value labels on top of each bar
for bar in bar1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', color='blue')
for bar in bar2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', color='green')

# Setting labels, title, and ticks for the x-axis
ax.set_xlabel('Metrics')
ax.set_ylabel('Days')
ax.set_title('Comparison of Average Length of Stay and Booking Window')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Adjust layout and save the first plot
plt.tight_layout()
plt.savefig('../output/average_length_stay_booking_window_comparison.png')
plt.show()

### Part 2: Bar Chart for Total Net Orders and Gross Booking Amount ###
# Define the metrics and corresponding values for total net orders and booking amount
labels = ['Total Net Orders', 'Total Gross Booking Amount']
family_values = [family_travelers_metrics[label] for label in labels]
non_family_values = [non_family_travelers_metrics[label] for label in labels]

# X positions for bars for the second plot
x = np.arange(len(labels))

# Create figure and axis for the second plot
fig, ax = plt.subplots()

# Plotting the bars with color differentiation for Family and Non-Family Travelers
bar1 = ax.bar(x - bar_width/2, family_values, bar_width, label='Family Travelers', color='blue')
bar2 = ax.bar(x + bar_width/2, non_family_values, bar_width, label='Non-Family Travelers', color='green')

# Adding value labels on top of each bar for better readability
for bar in bar1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}', ha='center', va='bottom', color='blue')
for bar in bar2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}', ha='center', va='bottom', color='green')

# Setting labels, title, and ticks for the x-axis
ax.set_xlabel('Metrics')
ax.set_ylabel('Total Amount')
ax.set_title('Comparison of Total Net Orders and Gross Booking Amount')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Adjust layout and save the second plot
plt.tight_layout()
plt.savefig('../output/total_net_orders_gross_booking_amount_comparison.png')
plt.show()
