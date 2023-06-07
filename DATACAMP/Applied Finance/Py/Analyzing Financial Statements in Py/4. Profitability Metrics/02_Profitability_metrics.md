1. **Profitability metrics**
In this video, we will cover some profitability metrics. These metrics can come in handy when making investment decisions.

2. **Profitability ratios**
Profitability ratios tell us how much profit a company can generate from its revenue. Recall the two efficiency ratios we covered earlier - the gross margin and operating margin ratio. These ratios are also profitability ratios.

3. **High current ratio leads to high profitability?**
Now that we know a bit about profitability ratios and other financial ratios in general, we can study the relationship between some ratios and the profitability of a business. The figure shown is a scatter plot of the current ratio of tech companies against their gross margin. From this scatter plot, we can make out a slightly positive relationship between the current ratio and the gross margin of tech companies - the higher the current ratio, the higher the gross margin.

4. **Make the scatter plot**
We can use the Seaborn functionality sns-dot-scatterplot to make the plot. The syntax used to make the plot follows the same format as the sns-dot-barplot and sns-dot-lineplot, which we had learned earlier.

5. **Scatter plot with all the companies**
Now, if we make a scatter plot to see the relationship between the current ratio and gross margin, but this time including all the companies in our dataset, finding the relationship becomes tricky. With a cursory look at the plot, we might conclude that the relationship is still positive. However, we should notice that there is a bunching of points in the left top and middle portion of the plot. The bunching of many points in that area implies that there are many companies with a low current ratio but still a relatively high gross margin. Adding a line that best fits the points of this plot can help us discern the relationship.

6. **Add a line of best fit**
The line of best fit is the thick blue line running through the plot. We can now see that the line of best fit is sloping upwards, meaning that there is still a positive relationship between the current ratio and gross margin when we add all the companies in our dataset to the mix. Or is there a positive relation? Notice the blue bands around the thick line. The blue bands indicate the area where this line could have been. It is computed by the seaborn package using a statistical method called bootstrapping. You can read more about it on the seaborn documentation website. So, this line could also be negatively sloping, or it could also be flat, which indicates no relationship between the current ratio and gross margin. Thus, when we include all the companies in the mix to find out if there is a positive relationship between the current ratio and gross margin, the answer is that the relationship is ambiguous.

7. **Making scatter plot with a line of best fit**
We can use the Seaborn functionality sns-dot-regplot to make the plot. The syntax to make the plot follows the same format as sns-dot-barplot and sns-dot-lineplot.

8. **Let's practice!**
Now that we know something about profitability metrics, lets practice!