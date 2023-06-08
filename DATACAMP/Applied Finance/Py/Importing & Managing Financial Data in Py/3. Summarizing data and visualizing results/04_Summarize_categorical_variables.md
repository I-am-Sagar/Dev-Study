1. **Summarize categorical variables**
In this video, you will learn how to summarize categorical variables.

2. **From categorical to quantitative variables**
We have so far focused on quantitative variables. Categorical variables differ because their values represent distinct categories as opposed to numerical values. You can apply different calculations to numerical values, because you can easily compare them to each other, or aggregate them. For many categorical variables, concepts like average do not make much sense. Instead, the frequency distribution, that is, how many times each category occurs, is more informative.

3. **Categorical listing information**
Let's go back to our stock listing information. Columns of data type object are clearly not numerical in nature. Sector and Industry are most interesting because they represent groups of companies. Columns that contain numerical data may also represent categories. The IPO year, for instance, can also be considered a categorical variable that has a well-defined order. Remember that pandas represents integers with missing values as floats.

4. **Categorical listing information**
Let us first take a look at the categories in the sector column, where we have information for 238 of the 359 companies. To learn how many unique values or categories a categorical variable represents, pandas offers the nunique method. Apply it to the Sector column, and you learn that there are 12 different sectors on the AMEX stock exchange. nunique is a Series method. To learn how many unique values there are for each of the columns, use nunique together with apply and the lambda operator to create so-called anonymous functions. apply allows you to loop over the DataFrame columns, and lambda allows you to create a function 'on the fly', ie, without giving it a name so it can't be used afterwards. This function will receive one column at a time as a pandas series, exactly what nunique needs. As a result, you get the number of unique values for each column.

5. **How many observations per sector?**
Pandas has a method called dot-value_counts that you can apply to an individual column to learn how many times each unique value in this column occurs. You see that on the AMEX exchange, Healthcare occurs most frequently which makes it the mode of this distribution. Together with basic Industries, these two sectors are quite dominant, accounting for 93 companies, around 40% of the total number of companies for which we have sector information.

6. **How many IPOs per year?**
We can apply a similar analysis to the number of IPOs per year. Use single brackets to select the column IPO year - you need to enclose the column name in quotation marks because it contains a space. You notice that most IPOs occurred in 2002, the mode of this distribution, right after the dot com bubble burst. You will notice that the years are displayed as floats because they're missing values.

7. **Convert IPO Year to int**
Let's fix this to get a nicer plot. After you select the IPO year column, apply the method dropna a to get rid of the missing values. Then use the method astype to convert the remainder into integers. If you apply value_counts to the result, you see that the years are now displayed properly as integer values.

8. **Convert IPO Year to int**
Let’s now take this result and visualize it as a bar chart. To make the ticks on the x-axis more readable, you can rotate them by 45 degrees as you can see in the example.

9. **Let's practice!**
Let's now move on to practice your new skills.