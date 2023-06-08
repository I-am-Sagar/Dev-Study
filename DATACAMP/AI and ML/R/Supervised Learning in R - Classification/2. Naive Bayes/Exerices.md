### Question 1: Computing probabilities

**Exercise**

The `where9am` data frame contains 91 days (thirteen weeks) worth of data in which Brett recorded his location at 9am each day as well as whether the daytype was a weekend or weekday.

Using the conditional probability formula below, you can compute the probability that Brett is working in the office, given that it is a weekday.

$P(A|B) = \frac {P(A\space and\space B)}{P(B)} $

Calculations like these are the basis of the Naive Bayes destination prediction model you'll develop in later exercises.

**Instructions**

1. Find P(office) using nrow() and subset() to count rows in the dataset and save the result as p_A.
2. Find P(weekday), using nrow() and subset() again, and save the result as p_B.
3. Use nrow() and subset() a final time to find P(office and weekday). Save the result as p_AB.
4. Compute P(office | weekday) and save the result as p_A_given_B.
5. Print the value of p_A_given_B.

**Pre Code**

```r
# Compute P(A) 
p_A <- ___

# Compute P(B)
p_B <- ___

# Compute the observed P(A and B)
p_AB <- ___

# Compute P(A | B) and print its value
p_A_given_B <- ___
___
```

**Ans.**

```r
# Compute P(A) 
p_A <- nrow(subset(where9am, location == "office")) / nrow(where9am)

# Compute P(B)
p_B <- nrow(subset(where9am, daytype == "weekday")) / nrow(where9am)

# Compute the observed P(A and B)
p_AB <- nrow(subset(where9am, location == "office" & daytype == "weekday")) / nrow(where9am)

# Compute P(A | B) and print its value
p_A_given_B <- p_AB / p_B
p_A_given_B
```

### Question 2: Understanding dependent events

In the previous exercise, you found that there is a 60% chance Brett is in the office at 9am given that it is a weekday. On the other hand, if Brett is never in the office on a weekend, which of the following is/are true?

1. P(office and weekend) = 0.
2. P(office | weekend) = 0.
3. Brett's location is dependent on the day of the week.
4. All of the above.

**Ans.** 4

### Question 3: A simple Naive Bayes location model

**Exercise**

The previous exercises showed that the probability that Brett is at work or at home at 9am is highly dependent on whether it is the weekend or a weekday.

To see this finding in action, use the where9am data frame to build a Naive Bayes model on the same data.

You can then use this model to predict the future: where does the model think that Brett will be at 9am on Thursday and at 9am on Saturday?

The data frame where9am is available in your workspace. This dataset contains information about Brett's location at 9am on different days.

**Instructions**

1. Load the naivebayes package.
2. Use naive_bayes() with a formula like y ~ x to build a model of location as a function of daytype.
3. Forecast the Thursday 9am location using predict() with the thursday9am object as the newdata argument.
4. Do the same for predicting the saturday9am location.

**Pre Code**

```r
# Load the naivebayes package

# Build the location prediction model
locmodel <- naive_bayes(___, data = ___)

# Predict Thursday's 9am location
predict(___, ___)

# Predict Saturdays's 9am location
```

**Ans.**

```r
# Load the naivebayes package
library(naivebayes)

# Build the location prediction model
locmodel <- naive_bayes(location ~ daytype, data = where9am)

# Predict Thursday's 9am location
predict(locmodel, thursday9am)

# Predict Saturdays's 9am location
predict(locmodel, saturday9am)
```

### Question 4: Examining "raw" probabilities

**Exercise**

The naivebayes package offers several ways to peek inside a Naive Bayes model.

Typing the name of the model object provides the a priori (overall) and conditional probabilities of each of the model's predictors. If one were so inclined, you might use these for calculating posterior (predicted) probabilities by hand.

Alternatively, R will compute the posterior probabilities for you if the type = "prob" parameter is supplied to the predict() function.

Using these methods, examine how the model's predicted 9am location probability varies from day-to-day. The model locmodel that you fit in the previous exercise is available for you to use, and the naivebayes package has been pre-loaded.

**Instructions**

1. Print the locmodel object to the console to view the computed a priori and conditional probabilities.
2. Use the predict() function similarly to the previous exercise, but with type = "prob" to see the predicted probabilities for Thursday at 9am.
3. Compare these to the predicted probabilities for Saturday at 9am.

**Pre Code**

```r
# Examine the location prediction model

# Obtain the predicted probabilities for Thursday at 9am
predict(___, ___ , type = ___)

# Obtain the predicted probabilities for Saturday at 9am
```

**Ans.**

```r
# Examine the location prediction model
locmodel

# Obtain the predicted probabilities for Thursday at 9am
predict(locmodel, thursday9am, type = "prob")

# Obtain the predicted probabilities for Saturday at 9am
predict(locmodel, saturday9am, type = "prob")
```

### Question 5: Understanding independence

Understanding the idea of event independence will become important as you learn more about how "naive" Bayes got its name. Which of the following is true about independent events?

1. The events cannot occur at the same time.
2. A Venn diagram will always show no intersection.
3. Knowing the outcome of one event does not help predict the other.
4. At least one of the events is completely random.

**Ans.** 3

[Feedback: The Venn diagram shows an intersection if the events can occur together, but this doesn't mean they're dependent.]

### Question 6: Who are you calling naive?

The Naive Bayes algorithm got its name because it makes a "naive" assumption about event independence.

What is the purpose of making this assumption?

1. Independent events can never have a joint probability of zero.
2. The joint probability calculation is simpler for independent events.
3. Conditional probability is undefined for dependent events.
4. Dependent events cannot be used to make predictions.

**Ans.** 2

### Question 7: A more sophisticated location model

**Exercise**

The locations dataset records Brett's location every hour for 13 weeks. Each hour, the tracking information includes the daytype (weekend or weekday) as well as the hourtype (morning, afternoon, evening, or night).

Using this data, build a more sophisticated model to see how Brett's predicted location not only varies by the day of week but also by the time of day. The dataset locations is already loaded in your workspace.

You can specify additional independent variables in your formula using the + sign (e.g. y ~ x + b).

The naivebayes package has been pre-loaded.

**Instructions**

1. Use the R formula interface to build a model where location depends on both daytype and hourtype. Recall that the function naive_bayes() takes 2 arguments: formula and data.
2. Predict Brett's location on a weekday afternoon using the data frame weekday_afternoon and the predict() function.
3. Do the same for a weekday_evening.

**Pre Code**

```r
# Build a NB model of location
locmodel <- ___

# Predict Brett's location on a weekday afternoon
___

# Predict Brett's location on a weekday evening
___
```

**Ans.**

```r
# Build a NB model of location
locmodel <- naive_bayes(location ~ daytype + hourtype, data = locations)

# Predict Brett's location on a weekday afternoon
predict(locmodel, weekday_afternoon)

# Predict Brett's location on a weekday evening
predict(locmodel, weekday_evening)
```

### Question 8: Preparing for unforeseen circumstances

**Exercise**

While Brett was tracking his location over 13 weeks, he never went into the office during the weekend. Consequently, the joint probability of P(office and weekend) = 0.

Explore how this impacts the predicted probability that Brett may go to work on the weekend in the future. Additionally, you can see how using the Laplace correction will allow a small chance for these types of unforeseen circumstances.

The model locmodel is available for you to use, along with the data frame weekend_afternoon. The naivebayes package has also been pre-loaded.

**Instructions**

1. Use the locmodel to output predicted probabilities for a weekend afternoon by using the predict() function. Remember to set the type argument.
2. Create a new naive Bayes model with the Laplace smoothing parameter set to 1. You can do this by setting the laplace argument in your call to naive_bayes(). Save this as locmodel2.
3. See how the new predicted probabilities compare by using the predict() function on your new model.

**Pre Code**

```r
# Observe the predicted probabilities for a weekend afternoon

# Build a new model using the Laplace correction
locmodel2 <- ___

# Observe the new predicted probabilities for a weekend afternoon
```
**Ans.**

```r
# Observe the predicted probabilities for a weekend afternoon
predict(locmodel, weekend_afternoon, type = "prob")

# Build a new model using the Laplace correction
locmodel2 <- naive_bayes(location ~ daytype + hourtype, data = locations, laplace = 1)

# Observe the new predicted probabilities for a weekend afternoon
predict(locmodel2, weekend_afternoon, type = "prob")
```

### Question 9: Understanding the Laplace correction

By default, the naive_bayes() function in the naivebayes package does not use the Laplace correction. What is the risk of leaving this parameter unset?

1. Some potential outcomes may be predicted to be impossible.
2. The algorithm may have a divide by zero error.
3. Naive Bayes will ignore features with zero values.
4. The model may not estimate probabilities for some cases.

**Ans.** 1

### Question 10: Handling numeric predictors

Numeric data is often binned before it is used with Naive Bayes. Which of these is not an example of binning?

1. Age values recoded as 'child' or 'adult' categories
2. Geographic coordinates recoded into geographic regions (West, East, etc.)
3. Test scores divided into four groups by percentile
4. Income values standardized to follow a normal bell curve

**Ans.** 4

<hr>