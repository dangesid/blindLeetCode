import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'Category': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C'],
    'Value': [10, 15, 14, 13, 12, 23, 22, 25, 21, 24, 30, 28, 29, 31, 27]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Set the backend explicitly to avoid deprecation warnings
plt.switch_backend('TkAgg')

# Creating the box plot
plt.figure(figsize=(10, 8))
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Box Plot of Values by Category')

# Annotate the plot with min, Q1, median, Q3, and max values
for category in df['Category'].unique():
    subset = df[df['Category'] == category]['Value']
    min_val = subset.min()
    q1_val = subset.quantile(0.25)
    median_val = subset.median()
    q3_val = subset.quantile(0.75)
    max_val = subset.max()

    # Position for annotations
    x = df['Category'].unique().tolist().index(category)

    # Annotating each box plot
    plt.text(x, min_val, f'Min: {min_val}', horizontalalignment='center', verticalalignment='bottom', color='black',
             weight='semibold')
    plt.text(x, q1_val, f'Q1: {q1_val}', horizontalalignment='center', verticalalignment='bottom', color='blue',
             weight='semibold')
    plt.text(x, median_val, f'Median: {median_val}', horizontalalignment='center', verticalalignment='bottom',
             color='white', weight='semibold')
    plt.text(x, q3_val, f'Q3: {q3_val}', horizontalalignment='center', verticalalignment='bottom', color='blue',
             weight='semibold')
    plt.text(x, max_val, f'Max: {max_val}', horizontalalignment='center', verticalalignment='bottom', color='black',
             weight='semibold')

plt.show()
