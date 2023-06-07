1. **Working with raw datasets**
Great, we have learned some concepts that are very important in a forecast. We will now learn how to actually extract raw data from an external source, and be able to work with it in order to perform calculations and forecasting.

2. **Obtaining a dataset for forecasting**
We will be looking at a dataset from Tesla Motors Inc. you can find this data online, as it is a public company, and in this example have chosen to download their income statement as a CSV file. Let's have a look.

3. **First look**
Okay, so let's have a look at our raw data. It is set up as an income statement with some rows you should recognize, including revenue (which is another word for sales), cost of goods sold and gross profit. There is also the total operating expenses line and net income, also known as net profit. The financial years are specified at the top. The last column says "TTM", which stands for trailing twelve months. This shows the most recent 12 months data provided by Tesla, usually including the most recent quarterly data, which we will have a look at in later chapters. So at first glance, it seems okay. This extract was taken towards the end of 2017, so it can be used to forecast 2018 figures even though the final figures of 2017 are not yet known. However, there are some problems with this data. In order to use it, we need to make sure that all the numbers are in the correct format and eliminate any headers we do not want to have to use. We could do this manually of course, but this will require editing the file every time we have new data. Much better to do a quick solution in Python!

4. **Filtering the data in Python**
Okay, so how can we create a Python script to help us to work easier with the raw data? I have written some simple code in Python here, but to explain it, let's take it step by step. Step 1 is to create a filter. This filter can be the form of a list, and should only include the rows that we are interested in. I have chosen to name this list "Interesting metrics" and will include the rows called 'Gross profit' and 'Net income'. Step two is to use the method in Python, DataFrame-dot-isin(values) to filter only the values we are interested in. As we have already created a list with the values we are interested in, we can simply pass this list to the dataframe and call the new filtered dataframe "Filtered Income Statement" which can then be printed in the shell. See doesn't that look a lot simpler and cleaner?

5. **Let's practice!**
Okay, so now we have an idea what to do. Time to put this into practice.