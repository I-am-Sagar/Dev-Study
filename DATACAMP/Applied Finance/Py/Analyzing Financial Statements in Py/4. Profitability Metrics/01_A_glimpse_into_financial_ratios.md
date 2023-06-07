1. **A glimpse into financial ratios of some industries**
Welcome! In this video, we will go over some of the average financial ratios of companies in the tech, real estate, and fast-moving consumer goods industries, which we'll call FMCG. We will see that the average ratios varies by industry and learn what drives these differences.

2. **Average current ratio**
Recall that the current ratio is current assets divided by current liabilities. We can get the average current ratio grouped by industry using pivot_table(), which we learned earlier. Notice that the average current ratio of FMCG companies is lower compared to the tech and real estate companies. Now, the ideal current ratio is between one and three; however, it is not uncommon to see FMCG companies with a low current ratio. This is because some FMCG companies purchase lots of raw materials on credit, pushing up their current liabilities. Some FMCG companies are also very efficient, resulting in low inventory; that is, they sell off their goods fast, causing their current assets to be low, resulting in a low current ratio.

3. **Average debt-to-equity ratio**
Recall that debt-to-equity ratio is the total liabilities divided by the total shareholders' equity. We can use the code provided here to get the average debt-to-equity ratio per industry. Notice that the debt-to-equity ratio of real estate companies is much higher than the others. This is because real estate companies invest huge amounts of money into buying real estate, and they usually fund these purchases with loans, pushing up their total liabilities. A high debt-to-equity ratio is common in companies that invest heavily in fixed assets which are long-term assets that cannot be liquidated easily. A high debt-to-equity ratio is not necessarily bad if the company is bringing in enough money to pay off its debt.

4. **Visually compare ratios with industry average**
This plot shows the average current ratio of the tech companies in our dataset and also the average current ratio of all the tech companies, which is the brown bar in the plot. It is a neat plot to quickly see the average current ratio of different tech companies juxtaposed with the average current ratio of the entire tech industry. We can capture necessary high-level information from the plot. We see that Meta's current ratio is the highest and that Meta and Google have a higher-than-average current ratio. This would take longer to infer if the information was presented as numbers in a table.

5. **Making the bar plot**
Let's say we have a dataset of only tech companies, along with their current ratio computed. The data for the plot in the previous slide can be made with the help of pivot_table() using an additional argument called margins. Setting the option margins to true tells the pivot table also to compute an aggregated average, which in this case is the average current ratio of all tech companies. The DataFrame used for the plot now has a row in the column company called "All" which is the average current ratio of all tech companies.

6. **Making the bar plot**
With the data for the bar plot prepared, we can now make the plot using seaborn with our knowledge from the previous videos.

7. **Let's practice!**
Now, let us put our knowledge into practice.