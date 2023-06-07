### Question 1: Using margins in pivot tables and making a bar plot

You just learned the margins functionality of pivot_table().

Setting margins = True while using pivot_table() returns the aggfunc of the whole value, i.e., is the aggfunc of the value not conditioned on its index.

In this exercise, you will practice what you've learned. You will make a plot where you prepare the data using pivot_table() and also make use of the margins functionality.

A pandas DataFrame called dataset has been loaded for you. pandas and Seaborn have been loaded with the aliases pd and sns respectively.

**Instructions 1/3**

1. Print the columns of dataset to identify the ones you need to compute the debt-to-equity ratio.

**Pre Code**

```py
# Print the columns of the dataset
```

**Ans.**

```py
# Print the columns of the dataset
print(dataset.columns)
```

**Instructions 2/3**

1. Compute the debt-to-equity ratio and add it as an additional column called "debt_to_equity" in dataset.
2. Use pivot_table() to get the average debt-to-equity ratio by industry (given by the column "comp_type"), including an aggregated average for all industries.

**Pre Code**

```py
# Print the columns of the dataset
print(dataset.columns)

# Compute debt-to-equity ratio
dataset["debt_to_equity"] = ____

# Use a pivot table to compute average debt-to-equity ratios
pivot_data = ____
```

**Ans.**

```py
# Print the columns of the dataset
print(dataset.columns)

# Compute debt-to-equity ratio
dataset["debt_to_equity"] = dataset["Total Liab"]/dataset["Total Stockholder Equity"]

# Use pivot table to compute average debt-to-equity ratios
pivot_data = dataset.pivot_table(index = "comp_type", values = "debt_to_equity", margins=True)
```

**Instruction 3/3**

1. Make a bar plot using Seaborn with "comp_type" on the x-axis and the debt-to-equity ratio on the y-axis.

**Pre Code**

```py
# Print the columns of the dataset
print(dataset.columns)

# Compute debt-to-equity ratio
dataset["debt_to_equity"] = dataset["Total Liab"]/dataset["Total Stockholder Equity"]

# Use pivot table to compute average debt-to-equity ratios
pivot_data = dataset.pivot_table(index = "comp_type", values = "debt_to_equity", margins=True)

# Make the bar plot
sns.barplot(data=pivot_data.reset_index(), ____)
plt.xlabel("Industry")
plt.ylabel("Debt-to-equity ratio")
plt.show()
plt.close()
```

**Ans.**

```py
# Print the columns of the dataset
print(dataset.columns)

# Compute debt-to-equity ratio
dataset["debt_to_equity"] = dataset["Total Liab"]/dataset["Total Stockholder Equity"]

# Use pivot table to compute average debt-to-equity ratios
pivot_data = dataset.pivot_table(index = "comp_type", values = "debt_to_equity", margins=True)

# Make the bar plot
sns.barplot(data=pivot_data.reset_index(), x="comp_type", y="debt_to_equity")
plt.xlabel("Industry")
plt.ylabel("Debt-to-equity ratio")
plt.show()
plt.close()
```

### Question 2: Preparing data for a facet grid plot

In this exercise, you will prepare the data to make this plot: 

<img src="./img/excersise_3_pic.jpg" width="550">

In the next exercise, you'll practice making the plot. This is a neat plot to observe:

* The gross margin of tech companies is more spread out than those of FMCG companies
* Year by year, how profitable a company is compared to the average company in its industry.

pandas is loaded with the alias pd and seaborn is loaded with the alias sns. A pandas DataFrame dataset is loaded for you which already has a gross_margin column computed.

**Instructions 1/3**

1. Make a DataFrame with only tech and FMCG companies; you can subset "tech" and "fmcg" companies from the column "comp_type" in the DataFrame dataset.

**Pre Code**

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[____]
```

**Ans.**

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[dataset["comp_type"].isin(["tech", "fmcg"])]
```

**Instructions 2/3**

1. Use pivot_table() to compute tech and FMCG companies' average yearly gross margin ratio.

**Pre Code**

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[dataset["comp_type"].isin(["tech", "fmcg"])

# Compute yearly average gross margin ratio of tech and fmcg companies
subset_dat_avg = subset_dat.pivot_table(____).reset_index()
```

**Ans.**

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[dataset["comp_type"].isin(["tech", "fmcg"])]

# Compute yearly average gross margin ratio of tech and fmcg companies
subset_dat_avg = subset_dat.pivot_table(index=["Year", "comp_type"], values = "gross_margin").reset_index()
```

**Instructions 3/3**

1. Add the column "company" to the DataFrame subset_dat_avg, using np.where so that the entries of the column "company" is "Avg tech" when the entries of the column "comp_type" is "tech" and "Avg fmcg" when the entries of the column "comp_type" is "fmcg".
2. Concatenate both DataFrames subset_dat and subset_dat_avg to prepare them for plotting.

**Pre Code**

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[dataset["comp_type"].isin(["tech", "fmcg"])]

# Compute yearly average gross margin ratio of tech and fmcg companies
subset_dat_avg = subset_dat.pivot_table(index=["Year", "comp_type"], values = "gross_margin").reset_index()

# Add company column
subset_dat_avg["company"] = np.where(____)
                         
# Concatenate the DataFrames
plot_df = pd.concat(____)
```

**Ans.**

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[dataset["comp_type"].isin(["tech", "fmcg"])]

# Compute yearly average gross margin ratio of tech and fmcg companies
subset_dat_avg = subset_dat.pivot_table(index=["Year", "comp_type"], values = "gross_margin").reset_index()

# Add company column
subset_dat_avg["company"] = np.where(subset_dat_avg["comp_type"]=="tech", "Avg tech", "Avg fmcg")
                         
# Concatenate the DataFrames
plot_df = pd.concat([subset_dat, subset_dat_avg], axis=0)
```

### Question 3: Making a facet grid plot

In the previous exercise, you wrote the following code:

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[dataset["comp_type"].isin(["tech", "fmcg"])]

# Compute yearly average gross margin ratio of tech and fmcg companies
subset_dat_avg = subset_dat.pivot_table(index=["Year", "comp_type"], values = "gross_margin").reset_index()

#Add column company
subset_dat_avg["company"] = np.where(subset_dat_avg["comp_type"]=="tech", "Avg tech", "Avg fmcg")

#Concat the DataFrames
plot_df = pd.concat([subset_dat, subset_dat_avg], axis=0)
```

The code prepared the data to make the following plot:

<img src="./img/excersise_3_pic.jpg" width="550">

Now it's time to make the plot.

**Instructions**

1. Use the DataFrame plot_df to make the facet grid plot in the description using seaborn.

**Pre Code**

```py
# Make the plot
sns.relplot(data=plot_df.reset_index(drop=True), ____)
plt.show()
plt.close()
```

**Ans.**

```py
# Make the plot
sns.relplot(data=plot_df.reset_index(drop=True), x="Year", y="gross_margin", hue="company", col="comp_type", kind="line")
plt.show()
plt.close()
```

### Question 4: User-defined function to make plots

In the last exercise, you had to write this code to make the plot:

```py
# Subset tech and fmcg companies
subset_dat = dataset.loc[dataset["comp_type"].isin(["tech", "fmcg"])]

# Compute yearly average gross margin ratio of tech and fmcg companies
subset_dat_avg = subset_dat.pivot_table(index=["Year", "comp_type"], values = "gross_margin").reset_index()

# Add column company
subset_dat_avg["company"] = np.where(subset_dat_avg["comp_type"]=="tech", "Avg tech", "Avg fmcg")

# Concat the DataFrames
plot_df = pd.concat([subset_dat, subset_dat_avg], axis=0)

# Make the plot
sns.relplot(data=plot_df.reset_index(drop=True), x="Year", y="gross_margin", hue="company", col="comp_type", kind="line")
plt.show()
plt.close()
```

Notice that we perform the same actions on the tech and FMCG DataFrames in this exercise. This is repetitive and goes against a coding principle called DRY - Don't repeat yourself. Repetitive code is bad since it increases your work and makes your code more prone to mistakes. In this exercise, you will define your function to process data and plot figures.

**Instructions 1/2**

Look at this function - this function can make the same plot that you did in the last exercise but with the repetitiveness stripped out.

```py
def make_plot(dataset, ratio, comp_type):
  whole_dat = []
  for industry in comp_type:
    dat = dataset.loc[dataset["comp_type"]==industry]
    dat_avg = dat.pivot_table(index="Year", values=ratio).reset_index()
    dat_avg["company"], dat_avg["comp_type"] = f"Avg {type}", industry"
    whole_dat.append(pd.concat([dat, dat_avg]))

  plot_df = pd.concat(whole_dat).reset_index(drop=True)
  sns.relplot(data=plot_df, x="Year", y="gross_margin", hue="company", col="comp_type", kind="line")
  plt.show()
  plt.close()
```

This function uses an f-string, with f"Avg {industry}". This f-string will return Avgand the value of industry as an output. Also notice a drop=True in reset_index(). This will reset the index of the DataFrame but not add the old index as a column.

How many comp_types can this function take? The function is loaded in the console for you to test it. The pandas DataFrame dataset is also available with gross margin computed.

1. The function can take as many "comp_type" as the user wants in the account. However, it must be passed as a list where the entries are the types of companies.
2. The function can take as many "comp_type" as the user wants in the account. However, it should not be passed as a list where the entries are the types of companies.
3. The function can take only one "comp_type"

**Ans.** 1

**Instructions 2/2**

1. Use the function make_plot() to plot the gross margin ratio of real estate, FMCG, and tech companies over the years, along with their industry average gross margin over the years.

**Pre Code**

```py
# Plot the gross margin ratio
make_plot(____)
```

**Ans.**

```py
# Plot the gross margin ratio
make_plot(dataset, "gross_margin", ["fmcg","tech", "real_est"])
```

### Question 5: Relationship between operating margin and debt-to-equity for real estate companies

Scatter plots are a great way of seeing the relationship between two variables. In this exercise, you'll practice computing the operating margin and debt-to-equity ratio. You'll then make a scatter plot to see if there is any relationship between the operating margin and debt-to-equity ratio for real estate companies.

pandas ans Seaborn have been loaded with the alias pd and sns, respectively. You can use the pandas DataFrame dataset to compute the ratios. The console will have the columns of dataset printed so you see which columns to use to compute the ratios.

**Instructions 1/2**

1. Compute the operating margin ratio.
2. Compute the debt-to-equity ratio.

**Pre Code**

```py
# Compute the operating margin
dataset["operating_margin"] = ____

# Compute debt-to-equity
dataset["debt_to_equity"] = ____
```

**Ans.**

```py
# Compute the operating margin
dataset["operating_margin"] = (dataset["Total Revenue"] - dataset["Total Operating Expenses"])/dataset["Total Revenue"]

# Compute debt-to-equity
dataset["debt_to_equity"] = dataset["Total Liab"]/dataset["Total Stockholder Equity"]
```

**Instruction 2/2**

1. Subset the dataset DataFrame using the column comp_type to get only real_est companies.
2. Use seaborn to make a scatter plot with debt-to-equity on the x-axis and operating margin on the y-axis.

**Pre Code**

```py
# Check the columns
print(dataset.columns)

# Compute the operating margin
dataset["operating_margin"] = (dataset["Total Revenue"] - dataset["Total Operating Expenses"])/dataset["Total Revenue"]

# Compute debt-to-equity
dataset["debt_to_equity"] = dataset["Total Liab"]/dataset["Total Stockholder Equity"]

# Subset the fmcg companies
dataset_real_est = dataset.loc[____]

# Make the plot
sns.____
plt.show()
plt.close()
```

**Ans.**

```py
# Check the columns
print(dataset.columns)

# Compute the operating margin
dataset["operating_margin"] = (dataset["Total Revenue"] - dataset["Total Operating Expenses"])/dataset["Total Revenue"]

# Compute debt-to-equity
dataset["debt_to_equity"] = dataset["Total Liab"]/dataset["Total Stockholder Equity"]

# Subset the fmcg companies
dataset_real_est = dataset.loc[dataset["comp_type"]=="real_est"]

# Make the plot
sns.scatterplot(data = dataset_real_est, x="debt_to_equity", y="operating_margin")
plt.show()
plt.close()
```

### Question 6: Practice with sns.regplot()

In this exercise, you will check for any relationship between the operating margin and debt-to-equity ratio for all the companies in our dataset. You will first make a scatter plot to analyze the relationship and will be able to discern a relatively clear positive relationship between the debt-to-equity ratio and operating margin. Then you will use sns.regplot to get a line of best fit to confirm or reject the hypothesis that there is a positive relationship between the two ratios.

The pandas DataFrame dataset is loaded with debt-to-equity and operating margin ratio already computed. pandas and seaborn is loaded with alias pd and sns respectively.

**Instructions 1/2**

1. Use Seaborn to make a scatter plot with the debt-to-equity ratio on the x-axis and the operating margin on the y-axis.

**Pre Code**

```py
# Make the scatterplot
sns.___
plt.show()
plt.close()
```

**Ans.**

```py
# Make the scatterplot
sns.scatterplot(data=dataset, x="debt_to_equity", y="operating_margin")
plt.show()
plt.close()
```

**Instructions 2/2**

1. Use Seaborn to make a scatter plot along with a line of best fit with debt-to-equity ratio on the x-axis and operating margin on the y-axis.

**Pre Code**

```py
# Make the reg plot
sns.____
plt.show()
plt.close()
```

**Ans.**

```py
# Make the reg plot
sns.regplot(data=dataset, x="debt_to_equity", y="operating_margin")
plt.show()
plt.close()
```

### Question 7: Updating the user-defined function for plotting

Recall the function to make plots from an earlier exercise:

```py
def make_plot(dataset, ratio, comp_type):
  whole_dat = []
  for industry in comp_type:
    dat = dataset.loc[dataset["comp_type"]==industry]
    dat_avg = dat.pivot_table(index="Year",
                              values=ratio).reset_index()
    dat_avg["company"] = f"Avg {type}"
    dat_avg["comp_type"] = industry
    whole_dat.append(pd.concat([dat,
                                dat_avg]))

  plot_df = pd.concat(whole_dat).reset_index(drop=True)
  sns.relplot(data=plot_df,
              x="Year",
              y="gross_margin",
              hue="company",
              col="comp_type",
              kind="line")
  plt.show()
  plt.close()
```

Notice how this function can only make line plots with year on the x-axis. In this exercise, you will be introduced to an updated version of this function.

**Instructions 1/3**

The function has been updated like this:

```py
def make_plot_updated(dataset, x, y, kind, comp_type):
  whole_dat = []
  for industry in comp_type:
    dat = dataset.loc[dataset["comp_type"]==industry]
    values = [x,y if y!="Year" else x]
    dat_avg = dat.pivot_table(index="Year",
                              values=values).reset_index()
    dat_avg = dat_avg.loc[:,
                          ~dat_avg.columns.duplicated()]
    dat_avg["company"] = f"Avg {type}"
    dat_avg["comp_type"] = industry
    whole_dat.append(pd.concat([dat, dat_avg]))

  plot_df = pd.concat(whole_dat).reset_index(drop=True)
  sns.relplot(data=plot_df,
              x=x,
              y=y,
              hue="company",
              col="comp_type",
              kind=kind)
  plt.show()
  plt.close()
```

In the code above, whole_dat is a list, and the command .append(x) essentially affixes x to the list it is applied to, which in this case is whole_dat.

Choose the correct option below. The function is loaded in the console for you to test it. The pandas DataFrame dataset is also available with operating margin and debt-to-equity ratio computed.

1. The function can be used to make line plots and scatter plots.
2. The function can be used to make line plots, scatter plots and bar plots.
3. The function is wrong and cannot make anything.

**Ans.** 1

**Instruction 2/3**

The function has been updated like this:

```py
def make_plot_updated(dataset, x, y, kind, comp_type):
  whole_dat = []
  for industry in comp_type:
    dat = dataset.loc[dataset["comp_type"]==industry]
    values = [x,y if y!="Year" else x]
    dat_avg = dat.pivot_table(index="Year",
                              values=values).reset_index()
    dat_avg = dat_avg.loc[:,
                          ~dat_avg.columns.duplicated()]
    dat_avg["company"] = f"Avg {type}"
    dat_avg["comp_type"] = industry
    whole_dat.append(pd.concat([dat, dat_avg]))

  plot_df = pd.concat(whole_dat).reset_index(drop=True)
  sns.relplot(data=plot_df,
              x=x, y=y,
              hue="company",
              col="comp_type",
              kind=kind)
  plt.show()
  plt.close()
```
What is the purpose of (1) values = [x,y if y!="Year" else x], and (2) dat_avg = dat_avg.loc[:,~dat_avg.columns.duplicated()]?

You can paste the following code in the console and have a look at the output to figure it out. ~ negates the object it is attached to. So ~x means not x.

```py
dat = dataset.loc[dataset["comp_type"]=="fmcg"]

x,y = "operating_margin", "Year"
values = [x,y if y!="Year" else x]
dat_avg = dat.pivot_table(index="Year", values=values).reset_index()
print(dat_avg)
print(dat_avg.columns.duplicated())
dat_avg = dat_avg.loc[:,~dat_avg.columns.duplicated()]
print(values)
print(dat_avg)


x,y = "operating_margin", "debt_to_equity"
values = [x,y if y!="Year" else x]
dat_avg = dat.pivot_table(index="Year", values=values).reset_index()
print(dat_avg)
print(dat_avg.columns.duplicated())
dat_avg = dat_avg.loc[:,~dat_avg.columns.duplicated()]
print(values)
print(dat_avg)
```

1. (1) and (2) serve no purpose and are there to confuse me.
2. (1) only checks if `y = "Year"` and (2) does nothing.
3. (1) takes the out "Year" from y argument, if `"y = Year"` and (2) drops duplicate columns from df_avg.
4. (1) does nothing and (2) drops duplicate columns from `df_avg`.

**Ans.** 3

**Instructions 3/3**

1. Use the function make_plot_updated() to make a scatter plot with the debt-to-equity ratio on the x-axis, operating margin on the y-axis, and different facets for tech, FMCG, and real estate companies.

**Pre Code**

```py
# Use the new user-defined function to make the plot
make_plot_updated(____)
```

**Ans.**

```py
# Use the new user-defined function to make the plot
make_plot_updated(dataset = dataset, x="debt_to_equity", y="operating_margin", kind="scatter", comp_type = ["tech", "fmcg", "real_est"])
```

### Question 8: Practice making heat maps

Heat maps are a great way to visualize correlations between various financial ratios. They can be used to see which ratios correlate strongly with profitability ratios and thus aid us in deciding which companies to invest in.

In this exercise, you'll practice making heat maps. A pandas DataFrame merged_dat has been loaded for you with some ratios already computed. pandas and Seaborn have been loaded with the aliases pd and sns.

**Instructions 1/3**

1. Use merged_dat with the selected columns to make a correlation matrix.

**Pre Code**

```py
# Make the correlation matrix
corr_mat = merged_dat[["Gross Margin", "Operating Margin", "Debt-to-equity",
                             "Equity Multiplier", "Current Ratio"]]____
```

**Ans.**

```py
# Make the correlation matrix
corr_mat = merged_dat[["Gross Margin", "Operating Margin", "Debt-to-equity",
                             "Equity Multiplier", "Current Ratio"]].corr()
```

**Instructions 2/3**

1. Make a heat map using the correlation matrix you made.

**Pre Code**
```py
# Make the correlation matrix
corr_mat = merged_dat[["Gross Margin", "Operating Margin", "Debt-to-equity",
                             "Equity Multiplier", "Current Ratio"]].corr()

# Make heat map
____
plt.show()
plt.close()
```

**Ans.**
```py
# Make the correlation matrix
corr_mat = merged_dat[["Gross Margin", "Operating Margin", "Debt-to-equity",
                             "Equity Multiplier", "Current Ratio"]].corr()

# Make heat map
sns.heatmap(data=corr_mat)
plt.show()
plt.close()
```
**Instructions 3/3**

1. Make a heat map where the correlations are also mentioned in the rectangular cells on the plot.

**Pre Code**

```py
# Make the correlation matrix
corr_mat = merged_dat[["Gross Margin", "Operating Margin", "Debt-to-equity",
                             "Equity Multiplier", "Current Ratio"]].corr()

# Make heat map
sns.heatmap(data = corr_mat)
plt.show()
plt.close()

# Make heat map with annotations
____
plt.show()
plt.close()
```

**Ans.**

```py
# Make the correlation matrix
corr_mat = merged_dat[["Gross Margin", "Operating Margin", "Debt-to-equity",
                             "Equity Multiplier", "Current Ratio"]].corr()

# Make heat map
sns.heatmap(data = corr_mat)
plt.show()
plt.close()

# Make heat map with annotations
sns.heatmap(data = corr_mat, annot=True)
plt.show()
plt.close()
```

### Question 9: Broad analysis

To check whether a company is doing well financially, you should check how it compares to its competitors in the same industry.

In this exercise, you'll compute the companies' average debt-to-equity ratio, asset turnover ratio, current ratio, and gross margin over several years.

You'll also compute the average of these ratios in the FMCG, Tech, and Real Estate industries over several years and see how the companies' ratios compare to their industry average.

**Instructions 1/2**

1. Use .pivot_table() to compute the average "debt_to_equity","current_ratio", "asset_turnover", "gross_margin" of the companies in the DataFrame statement_info; the column "comp_type" has industry information.
2. Use .pivot_table() to compute the average "debt_to_equity", "current_ratio", "asset_turnover", "gross_margin" of the industries in the DataFrame statement_info; the column "comp_type" has industry information.

**Pre Code**

```py
# Compute average by company in each industry
company_avg = statement_info.pivot_table(index=____, values=["debt_to_equity"
                  ,"current_ratio"
                  ,"asset_turnover", "gross_margin"]).reset_index()
# Compute average in industry
industry_avg = statement_info.pivot_table(index=____, values=["debt_to_equity"
                  ,"current_ratio"
                  ,"asset_turnover", "gross_margin"]).reset_index()


industry_avg["company"] = "average"
plot_df = pd.concat([company_avg, industry_avg])
```

**Ans.**

```py
# Compute average by company in each industry
company_avg = statement_info.pivot_table(index=["company", "comp_type"], values=["debt_to_equity"
                  ,"current_ratio"
                  ,"asset_turnover", "gross_margin"]).reset_index()

# Compute average in industry
industry_avg = statement_info.pivot_table(index=["comp_type"], values=["debt_to_equity"
                  ,"current_ratio"
                  ,"asset_turnover", "gross_margin"]).reset_index()


industry_avg["company"] = "average"
plot_df = pd.concat([company_avg, industry_avg])
```

**Instructions 2/2**

1. Melt plot_df to be able to plot it using seaborn.
2. Use sns.catplot() to plot the ratios over the x axis and the companies over the y axis with facets - columns per comp_type and rows per the ratios.

**Pre Code**

```py
# Compute average by company in each industry
company_avg = statement_info.pivot_table(index=["company", "comp_type"], values=["debt_to_equity","current_ratio","asset_turnover","gross_margin"]).reset_index()

# Compute average in industry
industry_avg = statement_info.pivot_table(index=["comp_type"], values=["debt_to_equity","current_ratio","asset_turnover", "gross_margin"]).reset_index()
industry_avg["company"] = "average"
plot_df = pd.concat([company_avg, industry_avg])

# Melt plot_df to plot it
melt_df = plot_df.melt(id_vars=____, value_vars =["debt_to_equity"
                  ,"current_ratio","asset_turnover", "gross_margin"], value_name="Ratio" )

# Plot melt_df
sns.catplot(data=____, x=____, y=____,row=____, col=____, kind=____, sharey=False)
plt.subplots_adjust(hspace=0.25, wspace=2)
plt.show()
plt.close()
```

**Ans.**

```py
# Compute average by company in each industry
company_avg = statement_info.pivot_table(index=["company", "comp_type"], values=["debt_to_equity","current_ratio","asset_turnover","gross_margin"]).reset_index()

# Compute average in industry
industry_avg = statement_info.pivot_table(index=["comp_type"], values=["debt_to_equity","current_ratio","asset_turnover", "gross_margin"]).reset_index()
industry_avg["company"] = "average"
plot_df = pd.concat([company_avg, industry_avg])

# Melt plot_df to plot it
melt_df = plot_df.melt(id_vars=["company","comp_type"], value_vars =["debt_to_equity","current_ratio","asset_turnover", "gross_margin"], value_name="Ratio" )

# Plot melt_df
sns.catplot(data=melt_df, x="Ratio", y="company",row="variable", col="comp_type"
,kind="bar", sharey=False)
plt.subplots_adjust(hspace=0.25, wspace=2)
plt.show()
plt.close()
```