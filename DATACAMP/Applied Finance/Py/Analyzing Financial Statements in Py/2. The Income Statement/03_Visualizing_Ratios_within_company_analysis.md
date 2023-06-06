1. **Visualizing ratios for within-company analysis**
In this video, we will learn how to visualize financial ratios.

2. **Visualizing financial ratios**
Bar plots are a neat method to check a company's performance as compared to average performance in its industry. In this plot, we see some of Google's financial ratios as compared to those of the average tech industry's ratio.

3. **Preparing data for plotting**
How can we make the plot we just saw? First, we need to prepare the data we want to plot. Let's say we computed all the ratios we saw in the plot and stored the ratios in columns of the DataFrame plot_dat. To compute the average ratios grouped by company and comp type, we can use a pandas function called pivot_table(), which works similarly to groupby. In pivot_table, a list of columns to group over is passed to the index argument. We also specify the columns we wish to analyze to the "values" parameter, in this case, the specific ratios we are interested in. Finally, we use "aggfunc" to specify the aggregation we want to perform, which in this case, is "mean". Mean is also the default function of pivot_table, and can be skipped. When we supply an index parameter to pivot_table(), the resulting DataFrame's index is set to that column. To include it as a column in our output DataFrame rather than as an index, we can use reset_index(). The head of the DataFrame average_company_ratio is printed here.

4. **Preparing data for plotting**
We can also use pivot_table to compute the average ratio by industry. The first five rows of the avg_industry_ratio DataFrame is shown illustrate the average ratio per industry.

5. **Preparing data for plotting**
Plotting data using Seaborn requires the data to be in the so-called longitudinal format. A function of pandas called melt can help us melt wide data into longitudinal data. The id_vars argument in the function corresponds to the identifier variables or columns used when melting the DataFrame. The rest of the columns are the value variables - these are the columns we are un-pivoting.

6. **Preparing data for plotting**
We can see the head of the molten DataFrames in this slide. Notice that the DataFrame molten_plot_company has an extra column called company since it was previously grouped over comp type and company.

7. **Preparing data for plotting**
We want to be able to plot the data in both the molten DataFrames, but Seaborn can plot data from only one DataFrame. So, we need to be able to concatenate both the DataFrames. However, recall that the molten_plot_industry DataFrame does not have the column- company. To be able to concatenate both the molten DataFrames, both of them need to have the same columns, so we add the column company to the molten plot industry. Then, we can concatenate both the molten DataFrames using the pandas concat function.

8. **Make the bar graph**
Finally, now that our data is ready, we can plot it. We use Seaborn to plot a bar plot with the code sns-dot-bar plot. It takes as arguments the DataFrame we want to use to make the plot, what we want to plot on the x-axis and y-axis. It also takes as an argument which dimension we want to add a hue over, which in our case is company. In a figure like this, having an x and y axis label is redundant since we know what is on the x and y axis with no label, so we remove them using the plt-dot-xlabel and ylabel commands with empty quotations in them.

9. **Let's practice!**
Now, lets practice making some plots.