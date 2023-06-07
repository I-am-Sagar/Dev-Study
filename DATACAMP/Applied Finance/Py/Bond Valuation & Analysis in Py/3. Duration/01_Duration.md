1. **Duration**
Let's examine the sensitivity of bonds to interest rates in more detail.

2. **The context behind duration**
So far, we have seen that prices and yields move inversely; the lower the price of a bond, the higher its yield. What we don't yet know is how sensitive a particular bond is to interest rates. Different bonds will have a different sensitivity to interest rates; the same change in interest rates will affect different bonds differently. Duration is a measure of interest rate risk that helps us to quantify this sensitivity.

3. **Motivating example**
To see an example of this, let's consider a five year bond and a ten year bond, both paying a five percent annual coupon. If interest rates are at five percent, then they will both have a price of one hundred since their coupon rate equals the yield. Pricing each bond using the pv function confirms this.

4. **Motivating example**
Now let's move interest rates up to six percent and price the same two bonds using this higher level of interest rates. By comparing the new prices of these bonds to their old prices of one hundred each, we can see that the five year bond lost four point two one percent of its value, while the ten year bond lost seven point three six percent of its value. In other words, the ten year bond lost more of its value than the five year bond for the same change in interest rates; the ten year bond was more sensitive to interest rate changes.

5. **What is duration?**
There are several ways of defining duration. In this course, we define duration as the percentage price change of a bond for a one percentage point change in interest rates. Higher duration means higher interest rate risk. Duration is used by traders and investors to help assess the interest rate risk of a bond or portfolio of bonds, hedge this interest rate risk, or predict how much money will be made or lost for a given change in interest rates.

6. **Calculating duration**
As the formula for duration is quite complicated, in this course, we will use a simplified version. We calculate duration by pricing a bond at both a one percent higher and lower level of interest rates, and divide this by two times the original price of the bond times the amount we shifted interest rates by. This gives us an approximate estimate for how much bond prices will change for a one percent change in yields.

7. **Duration example**
Let's look at an example by taking a ten year bond with a five percent annual coupon and four percent yield. We want to calculate its duration using the formula from the previous slide. First, we find the price of the bond in the usual way and assign the result to the variable 'price'. Next, we find the price of the same bond for a one percent higher and lower level of yields, and assign the results to 'price up' and 'price down', respectively. Finally, we use our duration formula along with our assigned variables, and print the result. We get a result of seven point seven four, meaning that for a one percent change in yields, the price of our bond will change by approximately seven point seven four percent.

8. **Summary**
In summary, different bonds can behave differently for the same change in yields because they have different levels of interest rate sensitivity. Duration is the percentage price change of a bond for a one percent change in yields, and it is used to measure this interest rate sensitivity.

9. **Let's practice!**
Now it's time for you to practice finding the duration of some bonds!