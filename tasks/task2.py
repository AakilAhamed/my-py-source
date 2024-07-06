import pandas as pd

# Load the data
df1 = pd.read_csv("tasks\data\industry.csv")

# Remove duplicates
df1.drop_duplicates(inplace=True)

# Remove null values
df1.dropna(inplace=True)

# Filter the data (filter rows where 'Y-Kappa' is greater than 25)
df1 = df1[df1["Y-Kappa"] > 25]

# Sort the data (sort by 'ChipRate' in descending order)
df1.sort_values(by="ChipRate", ascending=False, inplace=True)

# Group the data (group by 'Observation' and calculate mean of 'Y-Kappa')
grouped_df = df1.groupby("Observation")["Y-Kappa"].mean()

# Save the cleaned, filtered, sorted and grouped data to a new CSV file
df1.to_csv("cleaned_data.csv", index=False)
grouped_df.to_csv("grouped_data.csv")