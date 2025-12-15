# Task 01:
# Create a bar chart to visualize the distribution of acategorical variable. In this task, we visualize the
# number of countries across different world regions
# using World Bank metadata.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
)

region_counts = df['Region'].value_counts()

plt.figure()
region_counts.plot(kind='bar')
plt.title("Number of Countries by Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
