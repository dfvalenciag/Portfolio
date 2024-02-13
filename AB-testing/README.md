# A/B Testing Project: Redesigning for Increased Conversions
In this A/B testing project, we undertake the task of designing, creating, and evaluating an A/B test using subscription data for a service similar to Medium, which offers annual subscriptions priced at 200 units and paid in a single installment.

The primary objective of this project is to enhance the conversion rates, particularly focusing on encouraging users to create an account, through the redesign of the website. With the front-end UX/UI prepared for the implementation of the new page layout, the project aims to assess the impact of this redesign on conversion metrics.

## Exploratory Data Analysis
Before delving into the A/B test, an exploratory analysis of the data has been conducted. This preliminary examination provides insights into the distribution and characteristics of the subscription data. It helps in understanding the baseline metrics before the redesign implementation.

## Hypothesis Test Design
Hypotheses Formulation
The hypothesis test is structured around two main hypotheses:

### Null Hypothesis ($H_0$)
The null hypothesis states that the redesign of the page has no significant effect on the conversion rate. In statistical terms:

$H_0: \ \ \ \ \ \ p = p_0$

where $p_0$ represents the conversion probability of the original page.

### Alternative Hypothesis ($H_1$)
Conversely, the alternative hypothesis asserts that the redesigned page impacts the probability of conversion. It is formulated as:

$H_1: \ \ \ \ \ \ p \neq p_0$

This implies that the conversion rate may either increase or decrease following the redesign.

### Significance Level
A significance level of $5%$ ($\alpha = 0.05$) is chosen for this hypothesis test. This implies that any observed effect with a probability of occurrence less than $5%$ under the assumption of the null hypothesis will lead to its rejection. In other words, we aim for a $95%$ level of confidence in our conclusions.

### Control Groups
To conduct the A/B test effectively, two distinct groups are established:

#### Control Group
The control group comprises users who will continue to interact with the original page design. They serve as the baseline against which the performance of the redesigned page is evaluated.

#### Treatment Group
The treatment group consists of users exposed to the newly redesigned page layout. Any differences in conversion rates observed between the control and treatment groups can be attributed to the effects of the redesign.

It is imperative that the allocation of users to these groups is entirely random, ensuring the validity and reliability of the test results. The front-end team is tasked with implementing a robust randomization mechanism to guarantee unbiased group assignment.