### Question 1: Explore the credit data

Begin by looking at the data set cr_loan. In this data set, loan_status shows whether the loan is currently in default with 1 being default and 0 being non-default.

You have more columns within the data, and many could have a relationship with the values in loan_status. You need to explore the data and these relationships more with further analysis to understand the impact of the data on credit loan defaults.

Checking the structure of the data as well as seeing a snapshot helps us better understand what's inside the set. Similarly, visualizations provide a high level view of the data in addition to important trends and patterns.

The data set cr_loan has already been loaded in the workspace.

**Instructions 1/3**

1. Print the structure of the cr_loan data.
2. Look at the first five rows of the data.

**Pre Code**

```py
# Check the structure of the data
print(____.dtypes)

# Check the first five rows of the data
print(cr_loan.____)
```

**Ans.**

```py
# Check the structure
print(cr_loan.dtypes)

# Check the first five rows
print(cr_loan.head())
```

**Instructions 2/3**

1. Plot a histogram of loan_amnt within the data.

**Pre Code**

```py
# Look at the distribution of loan amounts with a histogram
n, bins, patches = plt.____(x=cr_loan['____'], bins='auto', color='blue',alpha=0.7, rwidth=0.85)
plt.xlabel("Loan Amount")
plt.____()
```

**Ans.**

```py
# Look at the distribution of loan amounts with a histogram
n, bins, patches = plt.hist(x=cr_loan['loan_amnt'], bins='auto', color='blue',alpha=0.7, rwidth=0.85)
plt.xlabel("Loan Amount")
plt.show()
```

**Instructions 3/3**

1. Create a scatter plot of a person's income and age. In this case, income is the independent variable and age is the dependent variable.

**Pre Code**

```py
print("There are 32 000 rows of data so the scatter plot may take a little while to plot.")

# Plot a scatter plot of income against age
plt.____(cr_loan['____'], cr_loan['____'],c='blue', alpha=0.5)
plt.xlabel('Personal Income')
plt.ylabel('Persone Age')
plt.____()
```

**Ans.**

```py
print("There are 32 000 rows of data so the scatter plot may take a little while to plot.")

# Plot a scatter plot of income against age
plt.scatter(cr_loan['person_income'], cr_loan['person_age'],c='blue', alpha=0.5)
plt.xlabel('Personal Income')
plt.ylabel('Person Age')
plt.show()
```

### Question 2: Crosstab and pivot tables

Often, financial data is viewed as a pivot table in spreadsheets like Excel.

With cross tables, you get a high level view of selected columns and even aggregation like a count or average. For most credit risk models, especially for probability of default, columns like person_emp_length and person_home_ownership are common to begin investigating.

You will be able to see how the values are populated throughout the data, and visualize them. For now, you need to check how loan_status is affected by factors like home ownership status, loan grade, and loan percentage of income.

The data set cr_loan has been loaded in the workspace. 

**Instructions 1/4**

1. Create a cross table of loan_intent and loan_status.

**Pre Code**

```py
# Create a cross table of the loan intent and loan status
print(pd.____(cr_loan[____], cr_loan[____], margins = True))
```

**Ans.**

```py
# Create a cross table of the loan intent and status
print(pd.crosstab(cr_loan['loan_intent'], cr_loan['loan_status'], margins = True))
```

**Instructions 2/4**

1. Create a cross table of home ownership grouped by loan_status and loan_grade.

**Pre Code**

```py
# Create a cross table of home ownership, loan status, and grade
print(pd.crosstab(cr_loan[____],[cr_loan[____],cr_loan[____]])) 
```

**Ans.**

```py
# Create a cross table of home ownership, loan status, and grade
print(pd.crosstab(cr_loan['person_home_ownership'],[cr_loan['loan_status'],cr_loan['loan_grade']]))
```

**Instructions 3/4**

1. Create a cross table of home ownership, loan status, and average loan_percent_income.

**Pre Code**

```py
# Create a cross table of home ownership, loan status, and average percent income
print(pd.____(cr_loan[____], cr_loan[____],
              values=cr_loan[____], aggfunc=____))
```

**Ans.**

```py
# Create a cross table of home ownership, loan status, and average percent income
print(pd.crosstab(cr_loan['person_home_ownership'], cr_loan['loan_status'],
                  values=cr_loan['loan_percent_income'], aggfunc='mean'))
```

**Instructions 4/4**

1. Create a boxplot of the loan's percent of the person's income grouped by loan_status.

**Pre Code**

```py
# Create a box plot of percentage income by loan status
cr_loan.____(column = [____], by = ____)
plt.____('Average Percent Income by Loan Status')
plt.suptitle('')
plt.show()
```

**Ans.**

```py
# Create a box plot of percentage income by loan status
cr_loan.boxplot(column = ['loan_percent_income'], by = 'loan_status')
plt.title('Average Percent Income by Loan Status')
plt.suptitle('')
plt.show()
```

### Question 3: Finding outliers with cross tables

Now you need to find and remove outliers you suspect might be in the data. For this exercise, you can use cross tables and aggregate functions.

Have a look at the person_emp_length column. You've used the aggfunc = 'mean' argument to see the average of a numeric column before, but to detect outliers you can use other functions like min and max.

It may not be possible for a person to have an employment length of less than 0 or greater than 60. You can use cross tables to check the data and see if there are any instances of this!

The data set cr_loan has been loaded in the workspace.

**Instructions 1/4**

1. Print the cross table of loan_status and person_home_ownership with the max person_emp_length.

**Pre Code**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.____(cr_loan[____],cr_loan[____],
        values=cr_loan[____], aggfunc=____))
```

**Ans.**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.crosstab(cr_loan['loan_status'],cr_loan['person_home_ownership'],
                  values=cr_loan['person_emp_length'], aggfunc='max'))
```

**Instructions 2/4**

1. Create and array of indices for records with an employment length greater than 60. Store it as indices.

**Pre Code**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.crosstab(cr_loan['loan_status'],cr_loan['person_home_ownership'],
                  values=cr_loan['person_emp_length'], aggfunc='max'))

# Create an array of indices where employment length is greater than 60
____ = cr_loan[cr_loan[____] > ____].index
```

**Ans.**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.crosstab(cr_loan['loan_status'],cr_loan['person_home_ownership'],
                  values=cr_loan['person_emp_length'], aggfunc='max'))

# Create an array of indices where employment length is greater than 60
indices = cr_loan[cr_loan['person_emp_length'] > 60].index
```

**Instructions 3/4**

1. Drop the records from the data using the array indices and create a new dataframe called cr_loan_new.

**Pre Code**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.crosstab(cr_loan['loan_status'],cr_loan['person_home_ownership'],
                  values=cr_loan['person_emp_length'], aggfunc='max'))

# Create an array of indices where employment length is greater than 60
indices = cr_loan[cr_loan['person_emp_length'] > 60].index

# Drop the records from the data based on the indices and create a new dataframe
____ = cr_loan.____(____)
```

**Ans.**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.crosstab(cr_loan['loan_status'],cr_loan['person_home_ownership'],
                  values=cr_loan['person_emp_length'], aggfunc='max'))

# Create an array of indices where employment length is greater than 60
indices = cr_loan[cr_loan['person_emp_length'] > 60].index

# Drop the records from the data based on the indices and create a new dataframe
cr_loan_new = cr_loan.drop(indices)
```

**Instructions 4/4**

1. Print the cross table from earlier, but instead use both min and max

**Pre Code**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.crosstab(cr_loan['loan_status'],cr_loan['person_home_ownership'],
                  values=cr_loan['person_emp_length'], aggfunc='max'))

# Create an array of indices where employment length is greater than 60
indices = cr_loan[cr_loan['person_emp_length'] > 60].index

# Drop the records from the data based on the indices and create a new dataframe
cr_loan_new = cr_loan.drop(indices)

# Create the cross table from earlier and include minimum employment length
print(pd.____(____[____],____[____],
            values=____['person_emp_length'], aggfunc=['min','max']))
```

**Ans.**

```py
# Create the cross table for loan status, home ownership, and the max employment length
print(pd.crosstab(cr_loan['loan_status'],cr_loan['person_home_ownership'],
                  values=cr_loan['person_emp_length'], aggfunc='max'))

# Create an array of indices where employment length is greater than 60
indices = cr_loan[cr_loan['person_emp_length'] > 60].index

# Drop the records from the data based on the indices and create a new dataframe
cr_loan_new = cr_loan.drop(indices)

# Create the cross table from earlier and include minimum employment length
print(pd.crosstab(cr_loan_new['loan_status'],cr_loan_new['person_home_ownership'],
            values=cr_loan_new['person_emp_length'], aggfunc=['min','max']))
```

### Question 4: Visualizing credit outliers

You discovered outliers in person_emp_length where values greater than 60 were far above the norm. person_age is another column in which a person can use a common sense approach to say it is very unlikely that a person applying for a loan will be over 100 years old.

Visualizing the data here can be another easy way to detect outliers. You can use other numeric columns like loan_amnt and loan_int_rate to create plots with person_age to search for outliers.

The data set cr_loan has been loaded in the workspace.

**Instructions 1/2**

1. Create a scatter plot of person age on the x-axis and loan_amnt on the y-axis.

**Pre Code**

```py
# Create the scatter plot for age and amount
plt.scatter(____[____], ____[____], c='blue', alpha=0.5)
plt.xlabel("Person Age")
plt.ylabel("Loan Amount")
plt.____()
```

**Ans.**

```py
# Create the scatter plot for age and amount
plt.scatter(cr_loan['person_age'], cr_loan['loan_amnt'], c='blue', alpha=0.5)
plt.xlabel("Person Age")
plt.ylabel("Loan Amount")
plt.show()
```

**Instructions 2/2**

1. Use the .drop() method from Pandas to remove the outliers and create cr_loan_new.
2. Create a scatter plot of age on the x-axis and loan interest rate on the y-axis with a label for loan_status.

**Pre Code**

```py
# Use Pandas to drop the record from the data frame and create a new one
cr_loan_new = cr_loan.____(____[____[____] > ____].index)

# Create a scatter plot of age and interest rate
colors = ["blue","red"]
plt.____(____[____], ____[____],
            c = ____['loan_status'],
            cmap = matplotlib.colors.ListedColormap(colors),
            alpha=0.5)
plt.xlabel("Person Age")
plt.ylabel("Loan Interest Rate")
plt.____()
```

**Ans.**

```py
# Use Pandas to drop the record from the data frame and create a new one
cr_loan_new = cr_loan.drop(cr_loan[cr_loan['person_age'] > 100].index)

# Create a scatter plot of age and interest rate
colors = ["blue","red"]
plt.scatter(cr_loan_new['person_age'], cr_loan_new['loan_int_rate'],
            c = cr_loan_new['loan_status'],
            cmap = matplotlib.colors.ListedColormap(colors),
            alpha=0.5)
plt.xlabel("Person Age")
plt.ylabel("Loan Interest Rate")
plt.show()
```

### Question 5: Replacing missing credit data

Now, you should check for missing data. If you find missing data within loan_status, you would not be able to use the data for predicting probability of default because you wouldn't know if the loan was a default or not. Missing data within person_emp_length would not be as damaging, but would still cause training errors.

So, check for missing data in the person_emp_length column and replace any missing values with the median.

The data set cr_loan has been loaded in the workspace.

**Instructions**

1. Print an array of column names that contain missing data using .isnull().
2. Print the top five rows of the data set that has missing data for person_emp_length.
3. Replace the missing data with the median of all the employment length using .fillna().
4. Create a histogram of the person_emp_length column to check the distribution.

**Pre Code**

```py
# Print a null value column array
print(____.columns[____.____().any()])

# Print the top five rows with nulls for employment length
print(____[____[____].____()].head())

# Impute the null values with the median value for all employment lengths
____[____].____((cr_loan['person_emp_length'].____()), inplace=True)

# Create a histogram of employment length
n, bins, patches = plt.____(____[____], bins='auto', color='blue')
plt.xlabel("Person Employment Length")
plt.____()
```

**Ans.**

```py
# Print an array of columns with null values
print(cr_loan.columns[cr_loan.isnull().any()])

# Print the top five rows with nulls for employment length
print(cr_loan[cr_loan['person_emp_length'].isnull()].head())

# Replace the null values with the median value for all employment lengths
cr_loan['person_emp_length'].fillna((cr_loan['person_emp_length'].median()), inplace=True)

# Create a histogram of employment length
n, bins, patches = plt.hist(cr_loan['person_emp_length'], bins='auto', color='blue')
plt.xlabel("Person Employment Length")
plt.show()
```

### Question 6: Removing missing data

You replaced missing data in person_emp_length, but in the previous exercise you saw that loan_int_rate has missing data as well.

Similar to having missing data within loan_status, having missing data within loan_int_rate will make predictions difficult.

Because interest rates are set by your company, having missing data in this column is very strange. It's possible that data ingestion issues created errors, but you cannot know for sure. For now, it's best to .drop() these records before moving forward.

The data set cr_loan has been loaded in the workspace.

**Instructions**

1. Print the number of records that contain missing data for interest rate.
2. Create an array of indices for rows that contain missing interest rate called indices.
3. Drop the records with missing interest rate data and save the results to cr_loan_clean.

**Pre Code**

```py
# Print the number of nulls
print(____[____].____().____())

# Store the array on indices
____ = ____[____[____].____].____

# Save the new data without missing data
____ = ____.____(____)
```

**Ans.**

```py
# Print the number of nulls
print(cr_loan['loan_int_rate'].isnull().sum())

# Store the array on indices
indices = cr_loan[cr_loan['loan_int_rate'].isnull()].index

# Save the new data without missing data
cr_loan_clean = cr_loan.drop(indices)
```

### Question 7: Missing data intuition

Here's an intuition check! When handling missing data, you have three options: keep, replace, and remove.

You've been looking at numeric columns, but what about a non-numeric column? How would you handle missing data in the column person_home_ownership which has string values?

The object ownership_table has already been created to show how many records occur in each unique value of person_home_ownership with the following code:

```py
# Count the number of records for each unique value
cr_loan['person_home_ownership'].value_counts()
```

ownership_table and cr_loan are already loaded in the workspace.

1. Remove the records, they aren't going to be useful for prediction anyway.
2. Replace the data with the value 'Other'.
3. Replace the data with most frequently occuring value, 'Rent'.
4. Keep the missing values because we don't know what to choose.

**Ans.** 2

<hr>