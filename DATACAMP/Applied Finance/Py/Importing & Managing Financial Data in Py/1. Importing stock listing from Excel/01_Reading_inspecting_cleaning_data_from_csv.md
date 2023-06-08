1. **Reading, inspecting, and cleaning data from CSV**
Hi, and welcome to the course Importing and Managing Financial data in Python! My name is Stefan Jansen and I'll be your instructor for this course. I have been working in international finance, investment, and economic research for over 15 years, and have been using Python for data science for over five years. Today I advise companies on data strategy, machine learning, and artificial intelligence in various industries.

2. **Import and clean data**
In this first video, you will learn about how to import data in csv files to Python. When moving data from one format to another, you need to make sure that all information is accurately captured, and nothing gets lost in the process. To illustrate how to address some issues that often arise when you import data, we will use a file with info on companies listed on the AmEx Stock Exchange. This file contains a company's name and stock ticker, which is the symbol needed to get price and other information about a company from an exchange. It also contains its sector, industry and IPO year, that is the year when it started trading on a stock exchange. It also contains the most recent share price, and the market capitalization, which the combined value of all its shares, and the date of the latest update. A quick look at the file reveals a few missing values: they are identified by the string "n/a". You can also see that this CSV file contains three different types of data: 4 columns contain text data, also called strings, 3 columns contain numeric data, and one column has date information.

3. **How pandas stores data**
pandas assigns a different data type to each column, and stores this information in a property called ‘dtype’. The dtype of a column affects how you can use its content in calculation and visualization. In particular, pandas distinguishes between four main dtypes: The dtype `object` is reserved for columns with text data, or a mix of text and numeric data. There are two numeric data types: int64 is for columns containing whole numbers, represented using 64 bits so that the largest number can be 2 to the power of 64. float64 is the second numeric data type, reserved for columns containing either decimals, or whole numbers and some missing values. Lastly, the datetime64 dtype is for columns with date and time information.

4. **Import & inspect**
You can use the pandas read_csv method to import the data. Just tell read_csv where to find the file, and assign the result to the variable amex. Then, call the DataFrame method dot-info to display useful information and identify some mismatches. The index has 360 entries, so the DataFrame has 360 rows. As expected, there are eight data columns, but each has 360 valid observations, and no missing data points as you would have expected. Seven columns are of dtype object, ie, text data, and only one has dtype float. Instead, you would have expected 3 numeric and 1 datetime column.

5. **Dealing with missing values**
Let's fix the import result. The read CSV function takes several parameters to help you parse a csv file. To deal with missing values, use the parameter na_values. Just pass a string that identifies missing values in the source file, and pandas will replace them with the numpy value np-dot-nan, which stands for not-a-number. This makes sure that calculations with missing values work as expected. The numeric columns now have the correct data types. The IPO Year contains whole numbers, but is also signed the data type float because values are missing for some companies.

6. **Properly parsing dates**
We are not quite done yet: to parse the date information, use the parameter parse_dates, and pass a list with the names of one or several columns with date information. pandas will then interpret the data correctly, and, as you can see, now all columns have the expected data types.

7. **Showing off the result**
To display the result of your import, use the method .head(): it displays the content of the first few rows. It defaults to the first 5 rows, but you can pass another integers to display fewer or more rows. As you can see, the missing values are now represented as numpy nan values, and the dates are also properly displayed.

8. **Let's practice!**
Now it's time to put these new methods into practice!