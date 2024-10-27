## Sampling Techniques

*third edition*

**WILLIAM G. COCHRAN**

*Professor of Statistics, Emeritus  
Harvard University*

**JOHN WILEY & SONS**  
New York · Chichester · Brisbane · Toronto · Singapore

---

Copyright © 1977, by John Wiley & Sons, Inc.

All rights reserved. Published simultaneously in Canada.

Reproduction or translation of any part of this work beyond that permitted by Sections 107 or 108 of the 1976 United States Copyright Act without the permission of the copyright owner is unlawful. Requests for permission or further information should be addressed to the Permissions Department, John Wiley & Sons, Inc.

**Library of Congress Cataloging in Publication Data:**

Cochran, William Gemmell, 1909-  
Sampling techniques.

(Wiley series in probability and mathematical statistics)  
Includes bibliographical references and index.

1. Sampling (Statistics) I. Title.  
QA276.6.C6 1977 001.4'222 77-728  
ISBN 0-471-16240-X

Printed in the United States of America

40 39 38 37 36

---

to Betty

---

## Preface

As did the previous editions, this textbook presents a comprehensive account of sampling theory as it has been developed for use in sample surveys. It contains illustrations to show how the theory is applied in practice, and exercises to be worked by the student. The book will be useful both as a text for a course on sample surveys in which the major emphasis is on theory and for individual reading by the student.

The minimum mathematical equipment necessary to follow the great bulk of the material is a familiarity with algebra, especially relatively complicated algebraic expressions, plus a knowledge of probability for finite sample spaces, including combinatorial probabilities. The book presupposes an introductory statistics course that covers means and standard deviations, the normal, binomial, hypergeometric, and multinomial distributions, the central limit theorem, linear regression, and the simpler types of analyses of variance. Since much of classical sample survey theory deals with the distributions of estimators over the set of randomizations provided by the sampling plan, some knowledge of nonparametric methods is helpful.

The topics in this edition are presented in essentially the same order as in earlier editions. New sections have been included, or sections rewritten, primarily for one of three reasons: (1) to present introductions to topics (sampling plans or methods of estimation) relatively new in the field; (2) to cover further work done during the last 15 years on older methods, intended either to improve them or to learn more about the performance of rival methods; and (3) to shorten, clarify, or simplify proofs given in previous editions.

New topics in this edition include the approximate methods developed for the difficult problem of attaching standard errors or confidence limits to nonlinear estimates made from the results of surveys with complex plans. These methods will be more and more needed as statistical analyses (e.g., regressions) are performed on the results. For surveys containing sensitive questions that some respondents are unlikely to be willing to answer truthfully, a new device is to present the respondent with either the sensitive question or an innocuous question; the specific choice, made by randomization, is unknown to the interviewer. In some sampling problems it may seem economically attractive, or essential in countries with limited sampling resources, to use two overlapping lists (or frames, as they are called) to cover the complete population. The method of double sampling has been extended to cases where the objective is to compare the means.

---

The number of subgroups within the population. There has been interesting work on the attractive properties that the ratio and regression estimators have if it can be assumed that the finite population is itself a random sample from an infinite superpopulation in which a mathematical model appropriate to the ratio or regression estimator holds. This kind of assumption is not new—I noticed recently that Laplace used it around 1800 in a sampling problem—but it clarifies the relation between sample survey theory and standard statistical theory.

An example of further work on topics included in previous editions is Chapter 9a, which has been written partly from material previously in Chapter 9; this was done mainly to give a more adequate account of what seem to me the principal methods produced for sampling with unequal probabilities without replacement. These include the similar methods given independently by Brewer, J. N. K. Rao, and Durbin, Murthy’s method, the Rao, Hartley, Cochran method, and Madow’s method related to systematic sampling, with comparisons of the performances of the methods on natural populations. New studies have been done on the sizes of components of errors of measurement in surveys by repeat measurements by different interviewers, by interpenetrating subsamples, and by a combination of the two approaches. For the ratio estimator, data from natural populations have been used to appraise the small-sample biases in the standard large-sample formulas for the variance and the estimated variance. Attempts have also been made to use lectures based variants of the ratio estimator itself and of the formula for estimating its sampling variance. In stratified sampling there has been additional work on allocating sample sizes to strata when more than one item is of importance and on estimating sample errors when only one unit is to be selected per stratum. Some new systematic sampling methods for handling populations having linear trends are also of interest.

Alva I. Funkner and Emil H. Jebe prepared a large part of the lecture notes from which the first edition of this book was written. Some investigations that provided background material were supported by the Office of Naval Research, Navy Department. From discussions of recent developments in sampling or suggestions about this edition, I have been greatly helped by Tore Dalenius, David J. Finney, Daniel G. Horvitz, Leslie Kish, P. S. R. S. Ambasiva Rao, Martin Sandelands, Joseph Sedransk, Arnold R. Sen, and especially J. N. K. Rao, whose painstaking reading of the new and revised sections of this edition resulted in many constructive suggestions about gaps, weaknesses, obscurities, and selection of topics. For typing and other work involved in production of a typescript I am indebted to Rowena Foss, Holly Grano, and Edith Klotz. My thanks to all.

William G. Cochran  
South Orleans, Massachusetts  
February, 1977

---

## Contents

| CHAPTER | PAGE |
|---------|------|
| 1 INTRODUCTION | 1 |

### 1.1 Advantages of the Sampling Method
- Page 1

### 1.2 Some Uses of Sample Surveys
- Page 2

### 1.3 The Principal Steps in a Sample Survey
- Page 4

### 1.4 The Role of Sampling Theory
- Page 8

### 1.5 Probability Sampling
- Page 9

### 1.6 Alternatives to Probability Sampling
- Page 11

### 1.7 Use of the Normal Distribution
- Page 12

### 1.8 Bias and Its Effects
- Page 15

### 1.9 The Mean Square Error
- Page 15

**Exercises**
- Page 16

---

| CHAPTER | PAGE |
|---------|------|
| 2 SIMPLE RANDOM SAMPLING | 18 |

### 2.1 Simple Random Sampling
- Page 18

### 2.2 Selection of a Simple Random Sample
- Page 20

### 2.3 Definitions and Notation
- Page 23

### 2.4 Properties of the Estimates
- Page 25

### 2.5 Variances of the Estimates
- Page 26

### 2.6 The Finite Population Correction
- Page 32

### 2.7 Estimation of the Standard Error from a Sample
- Page 34

### 2.8 Confidence Limits
- Page 35

### 2.9 An Alternative Method of Proof
- Page 37

### 2.10 Random Sampling with Replacement
- Page 38

### 2.11 Estimation of a Ratio
- Page 39

### 2.12 Estimates of Means Over Subpopulations
- Page 41

### 2.13 Estimates of Totals Over Subpopulations
- Page 42

### 2.14 Comparisons Between Domain Means
- Page 43

### 2.15 Validity of the Normal Approximation
- Page 44

### 2.16 Linear Estimators of the Population Mean
- Page 45

**Exercises**
- Page 45

---

## Contents

| CHAPTER | PAGE |
|---------|------|
| 3 SAMPLING PROPORTIONS AND PERCENTAGES | 50 |

### 3.1 Qualitative Characteristics
- Page 50

### 3.2 Variances of the Sample Estimates
- Page 52

### 3.3 The Effect of $p$ on the Standard Errors
- Page 53

### 3.4 The Binomial Distribution
- Page 54

### 3.5 The Hypergeometric Distribution
- Page 56

### 3.6 Confidence Limits
- Page 57

### 3.7 Classification into More than Two Classes
- Page 59

### 3.8 Confidence Limits with More than Two Classes
- Page 61

### 3.9 The Conditional Distribution of $p$
- Page 62

### 3.10 Proportions and Totals Over Subpopulations
- Page 63

### 3.11 Comparisons Between Different Domains
- Page 64

### 3.12 Estimation of Proportions in Cluster Sampling
- Page 65

**Exercises**
- Page 68

---

| CHAPTER | PAGE |
|---------|------|
| 4 THE ESTIMATION OF SAMPLE SIZE | 72 |

### 4.1 A Hypothetical Example
- Page 72

### 4.2 Analysis of the Problem
- Page 73

### 4.3 The Specification of Precision
- Page 74

### 4.4 The Formula for $n$ in Sampling for Proportions
- Page 75

### 4.5 Rare Items—Inverse Sampling
- Page 76

### 4.6 The Formula for $n$ with Continuous Data
- Page 77

### 4.7 Advance Estimates of Population Variances
- Page 78

### 4.8 Sample Size with More than One Item
- Page 80

### 4.9 Sample Size when Estimates Are Wanted for Subdivisions of the Population
- Page 82

### 4.10 Sample Size in Decision Problems
- Page 85

### 4.11 The Design Effect (Deff)
- Page 86

**Exercises**
- Page 86

---

| CHAPTER | PAGE |
|---------|------|
| 5 STRATIFIED RANDOM SAMPLING | 89 |

### 5.1 Description
- Page 89

### 5.2 Notation
- Page 90

### 5.3 Properties of the Estimates
- Page 91

### 5.4 The Estimated Variance and Confidence Limits
- Page 93

### 5.5 Optimum Allocation
- Page 96

---

## Contents

### 5.6 Relative Precision of Stratified Random and Simple Random Sampling
- Page 99

### 5.7 When Does Stratification Produce Large Gains in Precision?
- Page 101

### 5.8 Allocation Requiring More than 100 Per Cent Sampling
- Page 104

### 5.9 Estimation of Sample Size with Continuous Data
- Page 105

### 5.10 Stratified Sampling for Proportions
- Page 107

### 5.11 Gains in Precision in Stratified Sampling for Proportions
- Page 109

### 5.12 Estimation of Sample Size with Proportions
- Page 110

**Exercises**
- Page 111

---

| CHAPTER | PAGE |
|---------|------|
| 5A FURTHER ASPECTS OF STRATIFIED SAMPLING | 115 |

### 5A.1 Effects of Deviations from the Optimum Allocation
- Page 115

### 5A.2 Effects of Errors in the Stratum Sizes
- Page 117

### 5A.3 The Problem of Allocation with More than One Item
- Page 121

### 5A.4 Other Methods of Allocation with More than One Item
- Page 123

### 5A.5 Two-Way Stratification with Small Samples
- Page 124

### 5A.6 Controlled Selection
- Page 126

### 5A.7 The Construction of Strata
- Page 128

### 5A.8 Number of Strata
- Page 136

### 5A.9 Stratification After Selection of the Sample (Poststratification)
- Page 137

### 5A.10 Quota Sampling
- Page 138

### 5A.11 Estimation from a Sample of the Gain Due to Stratification
- Page 142

### 5A.12 Estimation of Variance with One Unit per Stratum
- Page 143

### 5A.13 Strata as Domain of Study
- Page 144

### 5A.14 Estimating Totals and Means Over Subpopulations
- Page 145

### 5A.15 Sampling from Two Frames
- Page 146

**Exercises**
- Page 146

---

| CHAPTER | PAGE |
|---------|------|
| 6 RATIO ESTIMATORS | 150 |

### 6.1 Methods of Estimation
- Page 150

### 6.2 The Ratio Estimate
- Page 150

### 6.3 Approximate Variance of the Ratio Estimate
- Page 154

### 6.4 Estimation of the Variance from a Sample
- Page 155

### 6.5 Confidence Limits
- Page 157

### 6.6 Comparison of the Ratio Estimate with Mean per Unit
- Page 158

### 6.7 Conditions Under Which the Ratio Estimate Is a Best Linear Unbiased Estimate
- Page 161

### 6.8 Bias of the Ratio Estimate
- Page 162