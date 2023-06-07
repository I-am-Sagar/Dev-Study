1. **Working with variances in the forecast**
Now we will be exploring variances in a forecast and how to handle them.

2. **What are variances?**
In forecasting, variances occur frequently. It is difficult to predict the future, even when the data is relatively solid. Customers can cancel their orders, there could be a crash in the market, or other issues like an IT failure could cause the forecast to change. Often when these events happen, this results in a forecast variance, when actual results differ from the forecast. Usually, this results in the need to recalculate the forecast. However, Python can help us minimize the duplication of work and enable us to analyze the difference between actual values and forecast values, in order to perform analysis later.

3. **A gap analysis**
It is important to know why the forecast differed from the actual results. On top of this, now that the actual results are different, we can no longer rely on the original forecast and have to investigate how the forecast will evolve when taking this change into account. Identifying, quantifying and investigating this difference between the old forecast and the updated forecast is called a gap analysis. This is usually represented as per the graph here, where you can see the gap between the original forecast and the new forecast.

4. **Gap analysis and alternative forecasts**
Let's look at an example. A company forecast sales of 1200 in 2018. However, halfway through the year, the sales were only 300, with six months to go. It is probably unrealistic to expect sales to more than double for the next six months. So there is a gap. The first thing to do is perform a gap analysis - what caused this? Usually, there is an underlying dependency, in this case, sales were based on volumes of 120 to a key supplier, but they have only bought 30 thus far and only expect to buy a maximum of 45 in the next 6 months meaning the total volumes for the year will be only 75, not 120. This is the dependency. We have to adjust the forecasted volumes. So, an alternate forecast must be calculated. Using our skills with defining Python functions and working with dependencies, we can now see how to work with these scenarios in Python in the following exercises.

5. **Congratulations!**
Great job! Now you have the first look at using Python to help you in Financial forecasting! I hope to see you again soon in future courses!