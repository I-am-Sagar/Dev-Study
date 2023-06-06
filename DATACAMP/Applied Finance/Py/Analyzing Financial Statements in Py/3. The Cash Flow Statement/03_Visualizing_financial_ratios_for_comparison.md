1. **Visualizing financial ratios for comparison**
In this video, we will learn how to plot financial ratios for a between-company analysis. Previously, we learned how to plot financial ratios for a within-company analysis. Specifically, we made plots to analyze a company's financial ratios over time and within different families of ratios like leverage and liquidity ratios, but for one company. Now we shall extend our knowledge to do these analyses between companies.

2. **Plotting the ratios of two companies**
We can make the plot shown using the knowledge we gained from the previous videos by using sns-dot-line-plot. And the code here would give us this graph. This graph is essentially plotting the current ratio between the Coca-Cola Company and PepsiCo over time. This plot is interpretable, communicates effectively, and is a neat graph overall. So why do we need additional knowledge to be able to plot the financial ratios between multiple companies?

3. **Overcrowding when using sns.lineplot()**
Well, using sns-dot-lineplot might result in a problem of overcrowding. As you can see here, if you use sns-dot-lineplot, the graph gets overcrowded very fast as we start adding more and more financial ratios to the plot. The graph has too much information in too little space. It makes the graph challenging to read and interpret, and overall it doesn't look very neat.

4. **Introducing sns.relplot()**
The solution is to use sns-dot-relplot. Recall that in order to plot data with Seaborn, we need something called longitudinal data. Usually, the DataFrame which we use to analyze and compute ratios is something called a wide DataFrame, which contains multiple financial ratios over some years for some companies.

5. **Introducing sns.relplot()**
We can use the pandas function melt to transform the wide DataFrame to a longitudinal DataFrame. This is the same function that we learned earlier. Using this DataFrame, we can use sns-dot-relplot.

6. **Plot ratios using sns.relplot()**
The logic of sns-dot-relplot and the syntax it uses is very similar to that of sns-dot-lineplot. It takes data in the first argument, in this case df_melt, which is the DataFrame we want to plot. Next, it takes x and y, which is what we want to plot on the x and the y axis, respectively. hue contains additional dimensions over which we want to add and categorize by color (have a look at the legend). The new arguments here are alpha, col and kind. alpha is a number denoting how transparent or opaque we want the lines to be. The smaller the number, the more transparent the line. col is the column on which we want to subset the graphs in making multiple facets or panes. As we see here, col is the company, which gives us two facets or panes of a graph: one for Coca-Cola Company and one for PepsiCo. kind is what type of plot we want to make, which in our case is a line plot because we want to plot the ratios over time.

7. **A closer look at the plot**
Now, looking closely at the graph, it's much clearer than the one we had before. The graphs are not as overcrowded as before. The data between the two companies can be compared more effectively because we can see the ratios side by side. For instance, we can see the equity multiplier ratio for PepsiCo is higher almost every year compared to that of the Coca-Cola company.

8. **Let's practice!**
Let's practice what we just learned!