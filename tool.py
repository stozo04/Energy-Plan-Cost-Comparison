import pandas as pd
import matplotlib.pyplot as plt

# Define constants and inputs based on the user's details
# Current plan and both options

# Monthly usage in kWh
monthly_kwh = 1500

# Flat EV charging fees
current_ev_fee = 25
option1_ev_fee = 15
option2_ev_fee = 25

# Current plan details
current_base_rate = 10.9 / 100  # cents to dollars
current_tdsp_rate = 5.3 / 100  # cents to dollars

# Option 1 details
option1_base_rate = 10.3 / 100  # cents to dollars
option1_tdsp_rate = 5.2 / 100  # cents to dollars
option1_off_peak_rate = 5.1 / 100  # cents to dollars
option1_off_peak_hours = 4

# Option 2 details
option2_base_rate = 7.6 / 100  # cents to dollars
option2_tdsp_rate = 5.2 / 100  # cents to dollars
option2_peak_rate = 11 / 100  # cents to dollars
option2_peak_hours = 3

# Define hourly usage (averaged over the day based on screenshot data)
hourly_usage = [2] * 12  # First 12 hours with usage of 2
hourly_usage += [3.5] * 4  # Hours 12-16 with usage of 3.5
hourly_usage += [5.5] * 4  # Hours 16-20 with usage of 5.5
hourly_usage += [4] * 4  # Hours 20-24 with usage of 4

# Helper function to calculate costs
def calculate_plan_cost(base_rate, tdsp_rate, ev_fee, plan_option):
    total_cost = 0

    for hour, usage in enumerate(hourly_usage):
        print(f"Hour: {hour}, Usage: {usage}")
        if plan_option == 1:  # Option 1: 12am–4am off-peak rate
            if 0 <= hour < 4:
                total_cost += usage * (option1_off_peak_rate + tdsp_rate)
            else:
                total_cost += usage * (base_rate + tdsp_rate)
        elif plan_option == 2:  # Option 2: 6pm–9pm peak rate
            if 18 <= hour < 21:
                total_cost += usage * (option2_peak_rate + tdsp_rate)
            else:
                total_cost += usage * (base_rate + tdsp_rate)
        else:  # Current plan (no special time windows)
            total_cost += usage * (base_rate + tdsp_rate)

        # Print the current total_cost after this hour's calculation
        print(f"Current total cost after Hour {hour}: {total_cost}")

    # Save the total cost without EV fee for monthly calculation
    total_cost_without_ev_fee = total_cost

    # Add EV fee (one-time charge)
    total_cost += ev_fee

    # Calculate monthly cost based on the usage cost only, adding EV fee once
    monthly_cost = total_cost_without_ev_fee * 30 + ev_fee
    print(f"Final monthly cost (with one-time EV fee): {monthly_cost}")
    return monthly_cost

# Calculate costs for each plan
current_plan_cost = calculate_plan_cost(current_base_rate, current_tdsp_rate, current_ev_fee, 0)
option1_cost = calculate_plan_cost(option1_base_rate, option1_tdsp_rate, option1_ev_fee, 1)
option2_cost = calculate_plan_cost(option2_base_rate, option2_tdsp_rate, option2_ev_fee, 2)

# Create a summary table
summary = pd.DataFrame({
    "Plan": ["Current Plan", "Option 1 (12-Month Fixed)", "Option 2 (Month-to-Month)"],
    "Monthly Cost (USD)": [current_plan_cost, option1_cost, option2_cost]
})
print(summary)

# Plotting the results
def plot_cost_comparison(summary):
    plt.figure(figsize=(8, 6))
    plt.bar(summary["Plan"], summary["Monthly Cost (USD)"], edgecolor="black", alpha=0.7)
    plt.title("Energy Plan Monthly Cost Comparison", fontsize=16)
    plt.xlabel("Energy Plans", fontsize=12)
    plt.ylabel("Monthly Cost (USD)", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

# Call the function to display the graph
plot_cost_comparison(summary)
