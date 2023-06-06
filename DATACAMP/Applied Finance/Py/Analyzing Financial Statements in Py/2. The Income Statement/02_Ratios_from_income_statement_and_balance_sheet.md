1. **Ratios from the income statement and balance sheet**
Some financial ratios require information from both the balance sheet and the income statement to be computed. This video will cover one such ratio. In addition, we will go over defining a function to compute financial ratios. This can minimize repetitive work.

2. **Asset turnover ratio**
The asset turnover ratio is an efficiency ratio that requires information from the income statement and the balance sheet to be computed. It is the proportion of total revenue to total assets. The ratio measures how efficiently the company is using its assets to generate revenue.

3. **Computing asset turnover ratio using pandas**
The asset turnover ratio requires information from the income statement and the balance sheet to be computed. However, data from a company's balance sheet and income statement are usually recorded in separate tables. So our first step towards computing the ratio is merging both the tables, represented in the income_statement and balance_sheet DataFrames. Let's begin by merging the income statement with balance sheet and creating a new DataFrame called merged_dat. We merge by matching the "Year" and "company" columns in both datasets using the "on" keyword. Then, we can compute the ratio as the proportion of total revenue to total assets, and add it as an additional column to the merged DataFrame called "asset_turnover", just as we have done before.

4. **User-defined functions to compute ratios**
Python can be used to define our own functions which can help us reduce repetitive work. In the example shown, we can see how computing two new ratios as a column in a DataFrame requires quite a lot of typing. We will define our own function to reduce repetitive work for us.

5. **User-defined functions to compute ratios**
Here, we define our own function called compute ratio which takes a DataFrame, a numerator column, a denominator column, and the name of the ratio as arguments. It returns the DataFrame with a new column added to it, containing the computed ratio. Using this function, we can compute the current ratio and debt-to-equity ratio more easily.

6. **User-defined functions to compute ratios**
If we want to compute multiple ratios and add them to our DataFrame, we can loop over the function we defined. Instead of a single numerator, denominator and ratio name, we can define a list of numerators, denominators, and ratio names and loop over them one-by-one to compute multiple ratios. When we want to loop over multiple lists at the same time, we can use a function called "zip". This function takes the different lists and "zips" them together, so that we can loop over each grouping of numerators, denominators and ratio names one-by-one. In each iteration of the for loop, the "zip" function returns the corresponding element from each of the lists, so we can access and work with all the relevant values at once. Notice that we compute the ratios using information from the DataFrame balance_sheet and append the results to the same DataFrame. So, the DataFrame can stay unchanged in the loop. This enables us to compute a lot of ratios with very little repetitive work.

7. **Let's practice!**
Now, that we know how to write our own functions in Python, let's practice what we've learned.