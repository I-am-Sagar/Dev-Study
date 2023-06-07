1. **More on analyzing profitability**
In this video we will see more methods of visualizing a company's profitability.

2. **Checking correlations between different ratios**
This plot is called a heat map and can be used to show correlations between different financial ratios. This heat map shows the correlation between different financial ratios of companies in the real estate industry. Each rectangular block in the plot has a color representing the correlation between the ratios on their respective axes. For instance, the bottom left rectangle shows the correlation between the gross margin and the current ratio. The rectangular block above that shows the correlation between the gross margin and the equity multiplier ratio.

3. **How to make a heat map**
Making the heat map we just saw requires something called a correlation matrix. A correlation matrix is essentially a tabular representation of a heat map. Notice that the same column names are on the index as well - this format of the data is necessary to be able to make a heat map using seaborn. Notice how the correlation matrix has a correlation of one on the diagonal - this is because the diagonal represents the correlation of financial ratios with themselves, which will always be one.

4. **How to make a correlation plot**
We can use Seaborn's heatmap function to make the heat map using the code shown.

5. **How to make a correlation plot**
Setting annot equal to True will also add the actual correlations between the ratios on the plot. This might come in handy if a person struggles to perceive different shades of color, or if we don't want to continuously refer back to the legend.

6. **Multifaceted bar chart**
A bar chart with facets like this is a great way of seeing how the ratios of industries evolve over time and compare to each other. Just as we saw earlier, in this image, we can see that the debt-to-equity ratio of real estate companies is consistently larger than that of other companies.

7. **How to make a multifaceted bar chart?**
Recall how a molten DataFrame looks - we learned earlier how to make DataFrames like this using the melt functionality from pandas. We need the data to be in this format to be able to make the plot in the previous slide.

8. **How to make a multifaceted bar chart?**
We will use Seaborn's catplot function to make this type of plot. It is very similar to Seaborn's relplot, which takes data, x, and y as arguments. Just like Seaborn's relplot, it also takes row and col as arguments which is how we want to make the facets of the plot. Finally, the argument kind refers to what plot we want to make, which in this case is a bar plot. Notice the additional plt command apart from plt-dot-show and plt-dot-close. That exists to put some horizontal space, hence hspace, between the facets.

9. **Let's practice!**
Now, lets put our new learned knowledge to practice.