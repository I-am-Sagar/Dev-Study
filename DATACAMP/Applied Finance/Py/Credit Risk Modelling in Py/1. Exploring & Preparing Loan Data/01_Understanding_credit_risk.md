1. **Understanding credit risk**
Hi, my name is Michael Crabtree and I am a data scientist at Ford Motor Company. I will show you some concepts and techniques for credit risk modeling using Python.

2. **What is credit risk?**
What exactly is credit risk? Credit risk is the risk that someone who has borrowed money will not repay it all. Think of this risk as the difference between lending money to a person and purchasing a government bond. With government bonds, it's almost guaranteed to be paid back, but not when lending money to people. A loan is in default when the lending agency is reasonably certain the loan will not be repaid. We will use machine learning models to determine this.

3. **What is credit risk?**
Consider this example: we've loaned 300 dollars to someone who has made two payments but not the final payment. It is at this point we consider the loan to be in default. Predicting this beforehand is useful for us to estimate expected loss.

4. **Expected loss**
The expected loss is the amount that the firm loses as a result of the default on a loan. Expected loss is a simple calculation of the following three components. The probability of default, which is the likelihood someone will default on a loan. The exposure at default which is the amount outstanding at the time of default. And the loss given default which is the ratio of the exposure against any recovery from the loss. From our example the 100 dollars we were owed is our exposure, and if we sell that debt for 20 dollars, our loss given default would be 80 percent. The formula for expected loss is probability of default times exposure at default and loss given default. This course will focus on probability of default.

5. **Types of data used**
For modeling probability of default we generally have two primary types of data available. The first is application data, which is data that is directly tied to the loan application like loan grade. The second is behavioral data, which describes the recipient of the loan, such as employment length.

6. **Data columns**
The data we will use for our predictions of probability of default includes a mix. This is important because application data alone is not as good as application and behavioral data together. Included are two columns which emulate data that can be purchased from credit bureaus. Acquiring external data is a common practice in most organizations. These are the columns available in the data set. Some examples are: personal income, the loan amount's percentage of the person's income, and credit history length. Consider the percentage of income. This could affect loan status if the loan amount is more than their income, because they may not be able to afford payments.

7. **Exploring with cross tables**
Our data has 32 thousand rows, which can be difficult to see all at once. Here is where we use cross tables using the crosstab function available within Pandas. We can use this function to help get a high level view of the data similar to pivot tables in Excel. Here, we see the data has been grouped by loan status and home ownership, and then the average interest rate has been calculated.

8. **Exploring with visuals**
In addition to using cross tables, we can explore the data set visually. Here, we use matplotlib to create a scatter plot of the loan's interest rate and the recipient's income. Just like the cross table, plots help us get a high level view of our data.

9. **Let's practice!**
So, we've defined credit risk and the components of expected loss and methods for exploring the credit risk data with the intent of estimating the probability of default. Now test your skills on some programming exercises. Good luck!