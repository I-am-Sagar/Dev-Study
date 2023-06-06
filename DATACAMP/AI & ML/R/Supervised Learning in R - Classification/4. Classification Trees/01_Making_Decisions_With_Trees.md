Classification trees use flowchart-like structures to make decisions. Because humans can readily understand these tree structures, classification trees are useful when transparency is needed, such as in loan approval. We'll use the Lending Club dataset to simulate this scenario.

1. **Making decisions with trees**
Sometimes a difficult or complex decision can be made simpler by breaking it down into a series of smaller decisions. If you're considering whether to take a new job offer, you might define requirements for accepting the position. Does it offer a high enough salary? Does it have a long commute or require long hours? Does it provide free coffee? Classification trees, also known as decision trees, work much the same way. They are used to find a set of if/else conditions that are helpful for taking action. As you will see soon, because their decisions are easily understood without statistics, they can be useful for business strategy, especially in areas where transparency is needed, like loan application approval.

2. **A decision tree model**
Let's start by considering the decision tree structure. As you might expect, it closely resembles real-world trees. The goal is to model the relationship between predictors and an outcome of interest. Beginning at the root node, data flows through if/else decision nodes that split the data according to its attributes. The branches indicate the potential choices, and the leaf nodes denote the final decisions. These are also known as terminal nodes because they terminate the decision making process.

3. **Decision trees for prediction**
To understand how the tree structure is built, let's consider a business process like whether or not to provide someone a loan. After an applicant fills out a form with personal information like income, credit history, and loan purpose, the bank must quickly decide whether or not the individual is likely to repay the debt. Using historical applicant data and loan outcomes, a classification tree can be built to learn the criteria that were most predictive of future loan repayment.

4. **Divide-and-conquer**
Growing the decision tree uses a process called divide-and-conquer because it attempts to divide the dataset into partitions with similar values for the outcome of interest. For loan applications, it needs to separate the applicants who are likely to repay from those who are likely to default on the debt. Suppose the tree considers two aspects of each applicant: the credit score and the requested loan amount. This figure visualizes these characteristics in relation to whether the loan was repaid. To divide-and-conquer, the algorithm looks for an initial split that creates the two most homogeneous groups.

5. **Divide-and-conquer**
First, it splits into groups of "high" and "low" credit scores.

6. **Divide-and-conquer**
Then, it divides-and-conquers again with another split, creating groups for "high" and "low" requested loan amounts.

7. **The resulting tree**
Each one of these splits results in an if/else decision in the tree structure, as shown here. If the credit score is low, it predicts "loan default." If the credit score is high and the loan value is large, it also predicts "default." Otherwise, it predicts "repaid." Obviously, a decision tree built on actual lending data is likely to be much more complex. But this illustrates the basic process of how such a tree might be built; you'll learn more about how it works shortly. For now, let's ignore the implementation details to focus on putting the algorithm to work.

8. **Building trees in R**
There are several packages that can be used to build classification trees in R. One of the most widely used is called rpart for recursive partitioning, a synonym for divide-and-conquer. Simply use the rpart function with the R formula interface to specify the outcome and predictors. The "class" parameter tells rpart to build a classification tree. And like the other machine learning methods you've seen before, the predict function obtains the predicted class values for the test dataset.

9. **Let's practice!**
In the next exercise, you'll have a chance to apply what you've learned to actual Lending Club loan data.