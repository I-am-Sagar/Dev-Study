1. **Combine data from multiple worksheets**
Now that you can load data from multiple worksheets into pandas DataFrames, let us look at how you can combine these worksheets into a single DataFrame to analyze all this data together.

2. **Combine DataFrames**
In this video, you will learn how to concatenate or 'stack' multiple DataFrames. For this purpose, pandas has a function called pd-dot-concat: if you pass a list of two or more DataFrames to this function, it combines these DataFrames vertically. It does so by looking for matching column names in the DataFrames, and aligning the columns accordingly as it appends the DataFrames in the order that they appear in the list. As you can see in the example, pd.concat combines the three DataFrames containing the listings from the three exchanges

3. **Combine DataFrames**
4. **Combine DataFrames**
into a new DataFrame that contains the original information in stacked form.

5. **Concatenate two DataFrames**
Let's take a look at how this works in practice: As before, you can read two worksheets from the 'listings-dot-xlsx' file using pd-read_excel, while passing the respective exchange names to the sheet_name parameter. As a result, the listing data is now contained in two pandas DataFrames, assigned to variables with the same name. You can now combine these data frames by passing as list with the variables to the pd-dot-concat function. When you inspect the result using the method dot-info, you'll notice that the result contains over 3500 rows, around 400 from the AMEX exchange and 3,100 from the NASDAQ.

6. **Add a reference column**
If you combine the information from several DataFrames, you want to keep a reference about the data source with each listing. To this end, you can add a column to each DataFrame with the information about which exchange the companies are listed on before combining the DataFrames. This example shows you how to do that. Creating a new column is similar to selecting a column. Just use square brackets with the name you would like to use, and assign a value to the new column like the name of the exchange. Pandas will make sure that this value propagates across all the rows. This feature is also called broadcasting. You then use pd-dot-concat with the new DataFrames, and you will notice that the additional column appears in the combined version.

7. **Combine three DataFrames**
Let's now automate this process of reading and combining the exchange listing data with a for loop. First, you can use the ExcelFile object to obtain the sheet names from the attribute of the same name. Accessing this attribute returns a list with the names of the worksheets. Let's assign this list to a variable called exchanges so that you can later use it in a for loop to read the three sheets. Next, create an empty list to collect the DataFrames when you iterate over the three exchange names. Now you are ready to start looping through the 3 worksheets: just read the sheet containing the data on the stock exchange and assign it to a variable called listing. Then create a new column called Exchange to reference the stock exchange. As the last step in the loop, add the DataFrame with the listing information to the list. Once the loop is completed, the variable 'listings' contains all three DataFrames. You can use this list as the argument for pd-dot-concat to combine the three DataFrames, and assign the result to a new variable called combined_listings.

8. **Combine three DataFrames**
Inspecting the result using info shows that combined_listings contains now 6674 rows, the companies reported as listed on the three stock exchanges.

9. **Let's practice!**
Let's now move on to practice your new skills.