1. **Tips and tricks when working with datasets**
In this lesson, we will cover some tips and tricks we can use in Python when working with financial data.

2. **Common challenges when working with financial data**
When working with financial data, very often the raw data can be in different formats to what we need. Especially when it comes to dates, as there are multiple ways to present the same date, the US version and EU version being one example. Have a look, 09-08 in the US means 8th of September, but 09-08 in EU means the 9th of August...tricky! This can make working with, interpreting and combining datasets with different formats a challenge. We will look at a few tips and tricks that can help us to easily change data formats.

3. **Using a dictionary**
A dictionary is an associative array (also known as hashes). Any key of the dictionary is associated (or mapped) to a value. The values of a dictionary can be any Python data type. So dictionaries are un-ordered key-value-pairs. For example, we could define a dictionary that would let our Python script know that the value equals a key, for example, we would say that 01 equals January, and would be written in code like this.

4. **Remember to use the datetime library**
We will again use the datetime library. We can easily recognize dates and convert the format into a string that recognizes the day, month, and year we specify. To do this, we will use the datetime.strptime() method with the date_string and format arguments to convert the date format into a string using the below table of directives. This is a shortened list of directives. Look at the following example.

5. **Iterate over items**
We will also be using iterate items or iteritems(), which we have used for our raw data processing before. iteritems() iterates over a list of rows in a pandas' DataFrame. We will also use an index over our dictionaries and lists, as we will need to sometimes work with different elements of our data. Here is an example. Here we have a dictionary called wordFrequency which indicates the frequency of several words within a text. The key is the word itself and the value the frequency. All we do is iterate through the dictionary and for each key we get its corresponding value, and we print it out to the console. We will use dictionaries in order to organize the data that was pulled from financial statements from pandas' DataFrames.

6. **Let's practice!**
Great, we will be using these methods in the next exercises, so time to get practicing!