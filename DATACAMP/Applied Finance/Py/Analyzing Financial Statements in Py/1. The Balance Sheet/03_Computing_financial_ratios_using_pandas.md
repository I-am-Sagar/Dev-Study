1. **Computing financial ratios using pandas**
Now that we know the formulas of some financial ratios, let's learn how to use pandas to compute and analyze them.

2. **Structure of balance sheet data**
We will now learn how to compute financial ratios when a company's financial statement data is loaded into pandas. In this video, we'll use a DataFrame containing various companies' balance sheets. The DataFrame contains financial information from different companies over several years. We also have information about the industries the companies belong to, contained in the column named comp type.

3. **Computing current ratio**
We already know that new columns in a DataFrame can be added as shown. Here, we create a new column called current_ratio, which is the proportion of current assets to current liabilities.

4. **Using .groupby() to get results by group**
pandas groupby is a method that can be used to split a DataFrame into groups based on categorical variables in the DataFrame, and then apply a function to each group. We can use it to aggregate and analyze financial statement information over certain categories. For instance, we can use it to compute average current ratio per industry by grouping by comp_type, selecting current_ratio, and then applying the dot-mean() function.

5. **Using .groupby() to get results by group**
We can group over several columns in groupby too. In the last slide, we computed average current ratio per industry, by grouping by comp_type. But what if we want the average current ratio by industry, broken down by year? We will now group by two columns, by adding the year in addition to the comp type inside a list and passing this to the groupby function.

6. **Using groupby().transform()**
Using groupby alone returns a new DataFrame containing the results. However, what if we wanted the results of groupby appended to the rows of our existing DataFrame, corresponding to the group each row belongs to? We can use the transform function. In the code shown, we compute the average yearly current ratio by industry, and then append the result to the DataFrame balance sheet. We can see that the correct yearly average current ratio has been appended to the row the group applies to by looking closely at the columns: industry curr ratio, company, and year. All the companies in this image here are tech companies, so their average current ratio by year will be the same. The 2019 industry current ratio of Apple is the same as Microsoft. This indicates that the code is doing what it is supposed to do.

7. **Using .groupby().transform()**
The transform function is useful when we want to compare the results of an individual observation with that of a group. For instance, if we want to see the relative difference between the current ratio of a company with its industry, we can use transform. Since we compute a relative difference, we see the proportion of the company's ratio with that of its average industry and subtract one from it which gives us the relative difference.

8. **Using .isin()**
Another useful pandas function is dot-isin(). We can use this when we want to subset a larger DataFrame into a smaller part that is of interest to us for analysis. In this example, isin is used to subset the DataFrame to obtain tech and FMCG companies over the years 2019 and 2020.

9. **Let's practice!**
Now that we know how to compute financial ratios using pandas, and can use some of their functionality to do an in-depth analysis, let's practice what we learned.