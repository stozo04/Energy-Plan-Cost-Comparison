# Energy Plan Cost Comparison

## Overview
This project calculates and compares monthly energy costs for different energy plans based on provided input parameters. It is designed to assist users in evaluating which plan best suits their usage patterns and financial preferences.

## Features
- Hourly energy usage analysis.
- Cost calculation for:
  - Current Plan
  - Option 1: 12-Month Fixed with off-peak rate
  - Option 2: Month-to-Month with peak rate
- Incorporates Electric Vehicle (EV) charging fees.
- Outputs a detailed summary of the calculated monthly costs for all plans.
- **Visualizes results with a bar chart for easy comparison.**

## Requirements
- Python 3.x
- pandas library
- matplotlib library (install with `pip install matplotlib`)

## Usage
1. Update the input parameters in the script to reflect your energy usage and plan details:
   - Hourly energy usage (`hourly_usage`)
   - Plan rates and fees (e.g., `current_base_rate`, `option1_off_peak_rate`, etc.)
2. Run the script.
3. View the generated summary table and graph for a comparison of monthly costs.

## Example Output
```
                Plan                     Monthly Cost (USD)
----------------------------------------------------------
    Current Plan                           $XXX.XX
    Option 1 (12-Month Fixed)              $XXX.XX
    Option 2 (Month-to-Month)              $XXX.XX
```

### Bar Chart Example
A bar chart is displayed after running the script:
- X-axis: Energy Plans
- Y-axis: Monthly Cost (USD)

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please submit a pull request or report issues in the repository.

## Contact
For further assistance, please contact me.
