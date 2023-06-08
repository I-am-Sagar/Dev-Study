1. **Read data from Excel worksheets**
Let us now look at how to import data from Excel worksheets.

2. **Import data from Excel**
As example, you will be using an Excel workbook with 3 worksheets containing listing information for 3 exchanges: the AmEx Exchange and the NASDAQ that you are already familiar with, and also the NYSE. Each sheet contains the same information as the AMEX CSV file you have seen before, we just omitted the 'Last Update' column. You can use the parameter sheet_name to tell read_excel which worksheet to import. You have several options to import either a single sheet, or multiple sheets simultaneously: You can provide an integer that refers to the position of the worksheet. The number 0 means you want to import the first sheet. You can also refer to a sheet by its name. Second, you can import several sheets at the same time. Just provide a list with the names or positions of the sheets you would like read_excel to import. The result will be a dictionary, where the keys are the sheet names, and the values are DataFrames with the sheet content.

3. **Import data from one sheet**
Let's look at an example. To read the worksheet for the AmEx exchange, simply provide the label to the read_excel parameter sheet_name. Note that read_excel also uses the na_values parameter to parse missing values. If you call the info method on the result, you will notice the same output you obtained earlier from the read_csv method.

4. **Import data from two sheets**
Let's now import data from two worksheets. Just supply a list with the labels 'amex' and 'nasdaq' to the sheet_name parameter. The result contained in the variable 'listings' is a dictionary that contains two key-value pairs. The keys contain the names of the worksheets, and the values are the corresponding DataFrames. Since listings is a dictionary, you can access the DataFrame with the NASDAQ data by providing the matching key. Once you apply the dot-info method to the result, you can view the structure of the data about the listings on this stock exchange.

5. **Get sheet names**
pandas also allows us to retrieve the sheet names from an Excel workbook. To obtain this information, create an ExcelFile object using the path to an Excel workbook, as illustrated here for the 'listings-xlsx' file. One you have created this object, you can access its sheet_names attribute. This attribute contains a list with the names of the worksheets for this workbook. Here, we retrieve the list of all the exchange names, and assign it to the variable exchanges. In the next step, you can pass the ExcelFile object to read_excel to import its content, instead of the path to the file. You can then select the name of the target worksheet from the list stored the exchanges variable. Assigning the resulting DataFrame to the variable nyse,

6. **Get sheet names**
and call the method dot-info on this DataFrame to show the expected output.

7. **Let's practice!**
Let's now practice your new skills.