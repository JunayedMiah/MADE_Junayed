import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import folium

# Load cleaned data from SQLite databases
def load_data():
    db1 = sqlite3.connect('data/crash_reporting.db')
    db2 = sqlite3.connect('data/vehicle_collision.db')

    df1 = pd.read_sql('SELECT * FROM crash_reporting', db1)
    df2 = pd.read_sql('SELECT * FROM vehicle_collision', db2)

    return df1, df2

# Merge the datasets on latitude and longitude (if necessary)
def merge_data(df1, df2):
    merged_df = pd.merge(df1, df2, how='inner', on=['latitude', 'longitude'], suffixes=('_crash', '_collision'))
    return merged_df

# Analyze factors contributing to crash severity
def analyze_factors():
    # Load data
    df1, df2 = load_data()

    # Define severity for vehicle collision data
    df2['severity'] = df2['number_of_persons_injured'] + 2 * df2['number_of_persons_killed']

    # Bar chart: Severity of crashes by borough
    plt.figure(figsize=(12, 6))
    sns.barplot(x='borough', y='severity', data=df2, errorbar=None, estimator=sum, palette='viridis')
    plt.title('Total Severity of Crashes by Borough')
    plt.xticks(rotation=45)
    plt.ylabel('Total Severity')
    plt.xlabel('Borough')
    plt.show()

    # Pie chart: Distribution of crashes by light condition
    light_condition_counts = df1['light'].value_counts()
    plt.figure(figsize=(8, 8))
    light_condition_counts.plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Crashes by Light Condition')
    plt.ylabel('')  # Hide y-axis label
    plt.show()

    # Histogram: Distribution of speed limits
    plt.figure(figsize=(12, 6))
    sns.histplot(df1['speed_limit'], kde=True, bins=20, color='orange')
    plt.title('Distribution of Speed Limits in Crashes')
    plt.xlabel('Speed Limit')
    plt.ylabel('Frequency')
    plt.show()

    # Line chart: Crashes over time (using df2)
    df2['crash_date'] = pd.to_datetime(df2['crash_date'])
    crashes_over_time = df2.groupby(df2['crash_date'].dt.to_period('M')).size()
    crashes_over_time.index = crashes_over_time.index.to_timestamp()
    plt.figure(figsize=(12, 6))
    crashes_over_time.plot(kind='line', marker='o', color='blue')
    plt.title('Crashes Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Crashes')
    plt.grid(True)
    plt.show()

    # Heatmap: Correlation of numerical factors with severity (df2)
    numerical_cols = ['number_of_persons_injured', 'number_of_persons_killed', 'severity']
    correlation_matrix = df2[numerical_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation of Numerical Factors with Severity')
    plt.show()

    # Scatter plot: Speed limit vs severity (df1)
    if 'speed_limit' in df1.columns:
        df1['severity'] = df1.get('severity', 0)
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='speed_limit', y='severity', data=df1, hue='light', palette='tab10')
        plt.title('Speed Limit vs Severity by Light Condition')
        plt.xlabel('Speed Limit')
        plt.ylabel('Severity')
        plt.legend(title='Light Condition')
        plt.show()
    else:
        print("Column 'speed_limit' not found in df1.")

    # Bar chart: Crashes by weather condition
    weather_severity = df1.groupby('weather').size().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    weather_severity.plot(kind='bar', color='skyblue')
    plt.title('Crashes by Weather Condition')
    plt.xlabel('Weather Condition')
    plt.ylabel('Number of Crashes')
    plt.xticks(rotation=45)
    plt.show()

    # Area chart: Crashes over time (cumulative)
    cumulative_crashes = crashes_over_time.cumsum()
    plt.figure(figsize=(12, 6))
    cumulative_crashes.plot(kind='area', color='lightblue', alpha=0.6)
    plt.title('Cumulative Crashes Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Number of Crashes')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    analyze_factors()
