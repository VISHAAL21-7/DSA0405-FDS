import pandas as pd
import matplotlib.pyplot as plt

# Create sample dataset
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. SORTING
print("\nSorted by Marks:")
sorted_df = df.sort_values(by='Marks', ascending=False)
print(sorted_df)

# 2. GROUPING
print("\nAverage Marks by Department:")
grouped_df = df.groupby('Department')['Marks'].mean()
print(grouped_df)

# 3. RANKING
df['Rank'] = df['Marks'].rank(ascending=False, method='dense')

print("\nStudents with Rank:")
print(df.sort_values(by='Rank'))

# 4. PLOTTING
# Bar chart of students' marks
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Marks'])

plt.title('Student Marks')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot average marks by department
grouped_df.plot(kind='bar')

plt.title('Average Marks by Department')
plt.xlabel('Department')
plt.ylabel('Average Marks')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
