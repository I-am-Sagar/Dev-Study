1. **Model evaluation and implementation**
We've fully developed two models to predict the probability of default, and we need to use many different metrics to compare them to ensure we select the best one.

2. **Comparing classification reports**
First, we will use classification reports. For comparison, we will look at two side-by-side and focus on one metric, the macro average F-1 score. The calculation behind the F1 score combines precision and recall to create a single metric and is shown here. The unweighted average of the F1 scores for default and non-default is the macro average F1 score. With this, we can use a single number to get a good understanding of each models' performance across defaults and non-defaults.

3. **ROC and AUC analysis**
We will also use ROC charts and AUC scores. The ROC chart will have a line for each model which allows us to compare the lift for both. The greater the lift means that the AUC score is higher and the model has better performance overall for defaults and non-defaults. In this example, we see two models compared to the random prediction going through the middle. Here, the gradient boosted tree model has more lift, and will have a higher AUC score.

4. **Model calibration**
Another method we will use to compare models is to check how well calibrated their predicted probabilities are. What this means is we want to be able to interpret these probabilities as a confidence level for default. A model is well-calibrated when a sample of loans has an average predicted probability of default close to that sample's percentage of actual defaults. For example, if we take 10 loans and their average predicted probability of default is 0.12, we expect 12% of the sample to be defaults. If our model has an average predicted probability of default of 0.25 and that sample is 65% defaults, then we have several loans that we predicted to be non-default that are actually defaults which we are very costly.

1 http://datascienceassn.org/sites/default/files/Predicting%20good%20probabilities%20with%20supervised%20learning.pdf

5. **Calculating calibration**
To calculate these values we use the calibration curve function. It is imported from the sci-kit learn package like this, and is used on the test set and the predicted probabilities of default. The n-bins parameter sets the number of samples to take. So, with this example, our test data is split into 5 samples and the function will calculate the average predicted probability of default and percentage of true defaults for each sample.

6. **Plotting calibration curves**
With the outputs from the calibration curve function, we make a calibration curve plot by calling the plot function from matplotlib. The result plots all our average predicted probabilities against all our percentage of actual defaults for each sample. Here, I used 20 samples.

7. **Checking calibration curves**
To interpret this plot, let's look at two different events. One where the model is above the perfectly calibrated line, and one where it's below.

8. **Calibration curve interpretation**
In this event, we see that our average predicted probability of default was 0.56, but this sample contained 75% defaults. Here is where we find the majority of our false negatives, which are quite costly. Our model is having a difficult time accurately predicting the probability of default for the loans in this sample.

9. **Calibration curve interpretation**
In the second event, the model's average predicted probability for the sample is 0.94 but the sample is only 66% defaults. Here we will find most of our false positives. These are missed opportunities for profit, but are not as damaging as the false negatives.

10. **Let's practice!**
Now let's do some programming exercises to see which model will come out on top!