## Sampling Techniques

*third edition*

**WILLIAM G. COCHRAN**  
*Professor of Statistics, Emeritus  
Harvard University*

**JOHN WILEY & SONS**  
New York • Chichester • Brisbane • Toronto • Singapore

---

## Copyright Information

Copyright © 1977, by John Wiley & Sons, Inc.  
All rights reserved. Published simultaneously in Canada.

Reproduction or translation of any part of this work beyond that permitted by Sections 107 or 108 of the 1976 United States Copyright Act without the permission of the copyright owner is unlawful. Requests for permission or further information should be addressed to the Permissions Department, John Wiley & Sons, Inc.

## Library of Congress Cataloging in Publication Data

**Cochran, William Gemmell, 1909–**  
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

""

---

## Preface

As did the previous editions, this textbook presents a comprehensive account of sampling theory as it has been developed for use in sample surveys. It contains illustrations to show how the theory is applied in practice, and exercises to be worked by the student. The book will be useful both as a text for a course on sample surveys in which the major emphasis is on theory and for individual reading by the student.

The minimum mathematical equipment necessary to follow the great bulk of the material is a familiarity with algebra, especially relatively complicated algebraic expressions, plus a knowledge of probability for finite sample spaces, including combinatorial probabilities. The book presupposes an introductory statistics course that covers means and standard deviations, the normal, binomial, hypergeometric, and multinomial distributions, the central limit theorem, linear regression, and the simpler types of analyses of variance. Since much of classical sample survey theory deals with the distributions of estimators over the set of randomizations provided by the sampling plan, some knowledge of nonparametric methods is helpful.

The topics in this edition are presented in essentially the same order as in earlier editions. New sections have been included, or sections rewritten, primarily for one of three reasons: (1) to present introductions to topics (sampling plans or methods of estimation) relatively new in the field; (2) to cover further work done during the last 15 years on older methods, intended either to improve them or to learn more about the performance of rival methods; and (3) to shorten, clarify, or simplify proofs given in previous editions.

New topics in this edition include the approximate methods developed for the difficult problem of attaching standard errors or confidence limits to nonlinear estimates made from the results of surveys with complex plans. These methods will be more and more needed as statistical analyses (e.g., regressions) are performed on the results. For surveys containing sensitive questions that some respondents are unlikely to be willing to answer truthfully, a new device is to present the respondent with either the sensitive question or an innocuous question; the specific choice, made by randomization, is unknown to the interviewer. In some sampling problems it may seem economically attractive, or essential in countries with limited sampling resources, to use two overlapping lists (or frames, as they are called) to cover the complete population. The method of double sampling has been extended to cases where the objective is to compare the means.

---

## PREFACE

There has been interesting work on the attractive properties that the ratio and regression estimators have if it can be assumed that the finite population is itself a random sample from an infinite superpopulation in which a mathematical model appropriate to the ratio or regression estimator holds. This kind of assumption is not new—I noticed recently that Laplace used it around 1800 in a sampling problem—but it clarifies the relation between sample survey theory and standard statistical theory.

An example of further work on topics included in previous editions is Chapter 9a, which has been written partly from material previously in Chapter 9; this was done mainly to give a more adequate account of what seem to me the principal methods produced for sampling with unequal probabilities without replacement. These include the similar methods given independently by Brewer, J. N. K. Rao, and Durbin, Murthy's method, the Rao, Hartley, Cochran method, and Madow's method related to systematic sampling, with comparisons of the performances of the methods on natural populations. New studies have been done of the sizes of components of errors of measurement in surveys by repeat measurements by different interviewers, by interpenetrating subsamples, and by a combination of the two approaches. For the ratio estimator, data from natural populations have been used to appraise the small-sample biases in the standard large-sample formulas for the variance and the estimated variance. Attempts have also been made to create less biased variants of the ratio estimator itself and of the formula for estimating its sampling variance. In stratified sampling there has been additional work on allocating sample sizes to strata when more than one item is of importance and on estimating sample errors when only one unit is to be selected per stratum. Some new systematic sampling methods for handling populations having linear trends are also of interest.

Alva L. Finkner and Emil H. Jebe prepared a large part of the lecture notes from which the first edition of this book was written. Some investigations that provided background material were supported by the Office of Naval Research, Navy Department. From discussions of recent developments in sampling or suggestions about this edition, I have been greatly helped by Tore Dalenius, David J. Finney, Daniel G. Horvitz, Leslie Kish, P. S. R. S. Sambasiva Rao, Martin Sandelijs, Joseph Sedransk, Amode R. Sen, and especially J. N. K. Rao, whose painstaking reading of the new and revised sections of this edition resulted in many constructive suggestions about gaps, weaknesses, obscurities, and selection of topics. For typing and other work involved in production of a typescript I am indebted to Rowena Foss, Holly Grano, and Edith Klotz. My thanks to all.

William G. Cochran

South Orleans, Massachusetts  
February, 1977

---

## Contents

### CHAPTER 1: INTRODUCTION

- 1.1 Advantages of the Sampling Method - Page 1
- 1.2 Some Uses of Sample Surveys - Page 2
- 1.3 The Principal Steps in a Sample Survey - Page 4
- 1.4 The Role of Sampling Theory - Page 8
- 1.5 Probability Sampling - Page 9
- 1.6 Alternatives to Probability Sampling - Page 11
- 1.7 Use of the Normal Distribution - Page 11
- 1.8 Bias and Its Effects - Page 12
- 1.9 The Mean Square Error - Page 15

  **Exercises** - Page 16

### CHAPTER 2: SIMPLE RANDOM SAMPLING

- 2.1 Simple Random Sampling - Page 18
- 2.2 Selection of a Simple Random Sample - Page 18
- 2.3 Definitions and Notation - Page 20
- 2.4 Properties of the Estimates - Page 24
- 2.5 Variances of the Estimates - Page 26
- 2.6 The Finite Population Correction - Page 29
- 2.7 Estimation of the Standard Error from a Sample - Page 31
- 2.8 Confidence Limits - Page 32
- 2.9 An Alternative Method of Proof - Page 34
- 2.10 Random Sampling with Replacement - Page 35
- 2.11 Estimation of a Ratio - Page 35
- 2.12 Estimates of Means Over Subpopulations - Page 37
- 2.13 Estimates of Totals Over Subpopulations - Page 39
- 2.14 Comparisons Between Domain Means - Page 41
- 2.15 Validity of the Normal Approximation - Page 42
- 2.16 Linear Estimators of the Population Mean - Page 44

  **Exercises** - Page 45

---

## CONTENTS

### CHAPTER 3  
SAMPLING PROPORTIONS AND PERCENTAGES  
50

- 3.1 Qualitative Characteristics  
- 3.2 Variances of the Sample Estimates  
- 3.3 The Effect of p on the Standard Errors  
- 3.4 The Binomial Distribution  
- 3.5 The Hypergeometric Distribution  
- 3.6 Confidence Limits  
- 3.7 Classification into More than Two Classes  
- 3.8 Confidence Limits with More than Two Classes  
- 3.9 The Conditional Distribution of p  
- 3.10 Proportions and Totals Over Subpopulations  
- 3.11 Comparisons Between Different Domains  
- 3.12 Estimation of Proportions in Cluster Sampling  

Exercises  
68

### CHAPTER 4  
THE ESTIMATION OF SAMPLE SIZE  
72

- 4.1 A Hypothetical Example  
- 4.2 Analysis of the Problem  
- 4.3 The Specification of Precision  
- 4.4 The Formula for n in Sampling for Proportions  
- 4.5 Rare Items—Inverse Sampling  
- 4.6 The Formula for n with Continuous Data  
- 4.7 Advance Estimates of Population Variances  
- 4.8 Sample Size with More than One Item  
- 4.9 Sample Size when Estimates Are Wanted for Subdivisions of the Population  
- 4.10 Sample Size in Decision Problems  
- 4.11 The Design Effect (Deff)  

Exercises  
86

### CHAPTER 5  
STRATIFIED RANDOM SAMPLING  
89

- 5.1 Description  
- 5.2 Notation  
- 5.3 Properties of the Estimates  
- 5.4 The Estimated Variance and Confidence Limits  
- 5.5 Optimum Allocation  

---

## CONTENTS

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

---

## CHAPTER 5A

### FURTHER ASPECTS OF STRATIFIED SAMPLING
- Page 115

#### 5A.1 Effects of Deviations from the Optimum Allocation
- Page 115

#### 5A.2 Effects of Errors in the Stratum Sizes
- Page 117

#### 5A.3 The Problem of Allocation with More than One Item
- Page 119

#### 5A.4 Other Methods of Allocation with More than One Item
- Page 121

#### 5A.5 Two-Way Stratification with Small Samples
- Page 122

#### 5A.6 Controlled Selection
- Page 123

#### 5A.7 The Construction of Strata
- Page 124

#### 5A.8 Number of Strata
- Page 126

#### 5A.9 Stratification After Selection of the Sample (Poststratification)
- Page 127

#### 5A.10 Quota Sampling
- Page 129

#### 5A.11 Estimation from a Sample of the Gain Due to Stratification
- Page 132

#### 5A.12 Estimation of Variance with One Unit per Stratum
- Page 134

#### 5A.13 Strata as Domains of Study
- Page 136

#### 5A.14 Estimating Totals and Means Over Subpopulations
- Page 142

#### 5A.15 Sampling from Two Frames
- Page 144

**Exercises**
- Page 146

---

## CHAPTER 6

### RATIO ESTIMATORS
- Page 150

#### 6.1 Methods of Estimation
- Page 150

#### 6.2 The Ratio Estimate
- Page 151

#### 6.3 Approximate Variance of the Ratio Estimate
- Page 153

#### 6.4 Estimation of the Variance from a Sample
- Page 155

#### 6.5 Confidence Limits
- Page 156

#### 6.6 Comparison of the Ratio Estimate with Mean per Unit
- Page 157

#### 6.7 Conditions Under Which the Ratio Estimate Is a Best Linear Unbiased Estimate
- Page 160

#### 6.8 Bias of the Ratio Estimate
- Page 162

---

## CONTENTS

### 6.9 Accuracy of the Formulas for the Variance and Estimated Variance
- Page 162

### 6.10 Ratio Estimates in Stratified Random Sampling
- Page 164

### 6.11 The Combined Ratio Estimate
- Page 165

### 6.12 Comparison of the Combined and Separate Estimates
- Page 167

### 6.13 Short-Cut Computation of the Estimated Variance
- Page 169

### 6.14 Optimum Allocation with a Ratio Estimate
- Page 172

### 6.15 Unbiased Ratio-type Estimates
- Page 174

### 6.16 Comparison of the Methods
- Page 177

### 6.17 Improved Estimation of Variance
- Page 178

### 6.18 Comparison of Two Ratios
- Page 180

### 6.19 Ratio of Two Ratios
- Page 182

### 6.20 Multivariate Ratio Estimates
- Page 184

### 6.21 Product Estimators
- Page 186

**Exercises**
- Page 186

## CHAPTER 7: REGRESSION ESTIMATORS
- Page 189

### 7.1 The Linear Regression Estimate
- Page 189

### 7.2 Regression Estimates with Preassigned b
- Page 190

### 7.3 Regression Estimates when b is Computed from the Sample
- Page 191

### 7.4 Sample Estimate of Variance
- Page 193

### 7.5 Large-Sample Comparison with the Ratio Estimate and the Mean per Unit
- Page 195

### 7.6 Accuracy of the Large-Sample Formulas for V(ȳ) and V(b)
- Page 197

### 7.7 Bias of the Linear Regression Estimate
- Page 199

### 7.8 The Linear Regression Estimator Under a Linear Regression Model
- Page 200

### 7.9 Regression Estimates in Stratified Sampling
- Page 201

### 7.10 Regression Coefficients Estimated from the Sample
- Page 202

### 7.11 Comparison of the Two Types of Regression Estimate
- Page 203

**Exercises**
- Page 203

## CHAPTER 8: SYSTEMATIC SAMPLING
- Page 205

### 8.1 Description
- Page 205

### 8.2 Relation to Cluster Sampling
- Page 207

### 8.3 Variance of the Estimated Mean
- Page 208

### 8.4 Comparison of Systematic with Stratified Random Sampling
- Page 212

### 8.5 Populations in "Random" Order
- Page 214

---

## CONTENTS

### 8.6 Populations with Linear Trend
- Page 214

### 8.7 Methods for Populations with Linear Trends
- Page 217

### 8.8 Populations with Periodic Variation
- Page 219

### 8.9 Autocorrelated Populations
- Page 221

### 8.10 Natural Populations
- Page 222

### 8.11 Estimation of the Variance from a Single Sample
- Page 224

### 8.12 Stratified Systematic Sampling
- Page 227

### 8.13 Systematic Sampling in Two Dimensions
- Page 229

### 8.14 Summary
- Page 229

### Exercises
- Page 231

## CHAPTER 9
### SINGLE-STAGE CLUSTER SAMPLING: CLUSTERS OF EQUAL SIZES
- Page 233

#### 9.1 Reasons for Cluster Sampling
- Page 233

#### 9.2 A Simple Rule
- Page 234

#### 9.3 Comparisons of Precision Made from Survey Data
- Page 235

#### 9.4 Variance in Terms of Intracluster Correlation
- Page 236

#### 9.5 Variance Functions
- Page 238

#### 9.6 A Cost Function
- Page 243

#### 9.7 Cluster Sampling for Proportions
- Page 244

### Exercises
- Page 247

## CHAPTER 9A
### SINGLE-STAGE CLUSTER SAMPLING: CLUSTERS OF UNEQUAL SIZES
- Page 249

#### 9A.1 Cluster Units of Unequal Sizes
- Page 249

#### 9A.2 Sampling with Probability Proportional to Size
- Page 250

#### 9A.3 Selection with Unequal Probabilities with Replacement
- Page 255

#### 9A.4 The Optimum Measure of Size
- Page 258

#### 9A.5 Relative Accuracies of Three Techniques
- Page 259

#### 9A.6 Sampling with Unequal Probabilities Without Replacement
- Page 262

#### 9A.7 The Horvitz-Thompson Estimator
- Page 263

#### 9A.8 Brewer’s Method
- Page 265

#### 9A.9 Murthy’s Method
- Page 266

#### 9A.10 Methods Related to Systematic Sampling
- Page 267

#### 9A.11 The Rao, Hartley, Cochran Method
- Page 268

#### 9A.12 Numerical Comparisons
- Page 270

#### 9A.13 Stratified and Ratio Estimates
- Page 272

### Exercises
- Page 272

---

## CHAPTER 10  
### SUBSAMPLING WITH UNITS OF EQUAL SIZE  
- **10.1** Two-Stage Sampling ........................................ 274  
- **10.2** Finding Means and Variances in Two-Stage Sampling .......... 275  
- **10.3** Variance of the Estimated Mean in Two-Stage Sampling ....... 276  
- **10.4** Sample Estimation of the Variance .......................... 277  
- **10.5** The Estimation of Proportions .............................. 278  
- **10.6** Optimum Sampling and Subsampling Fractions ................. 279  
- **10.7** Estimation of m<sub>opt</sub> from a Pilot Survey ................. 280  
- **10.8** Three-Stage Sampling ....................................... 281  
- **10.9** Stratified Sampling of the Units ........................... 288  
- **10.10** Optimum Allocation with Stratified Sampling ............... 289  

**Exercises** ......................................................... 290  

## CHAPTER 11  
### SUBSAMPLING WITH UNITS OF UNEQUAL SIZES  
- **11.1** Introduction ............................................... 292  
- **11.2** Sampling Methods when n = 1 ................................ 293  
- **11.3** Sampling with Probability Proportional to Estimated Size ... 294  
- **11.4** Sampling Methods for n > 1 ................................. 297  
- **11.5** Sampling Methods When n = 1 ................................ 298  
- **11.6** Two Useful Results ......................................... 299  
- **11.7** Units Selected with Equal Probabilities: Unbiased Estimator  300  
- **11.8** Units Selected with Equal Probabilities: Ratio to Size Estimator 301  
- **11.9** Units Selected with Unequal Probabilities with Replacement:  
  - Unbiased Estimator ............................................... 302  
- **11.10** Units Selected Without Replacement ........................ 303  
- **11.11** Comparison of the Methods ................................. 304  
- **11.12** Ratios to Another Variable ................................ 305  
- **11.13** Choice of Sampling and Subsampling Fractions. Equal Probabilities .................................................. 306  
- **11.14** Optimum Selection Probabilities and Sampling and Subsampling Fractions ........................................... 313  
- **11.15** Rates ..................................................... 314  
- **11.16** Stratified Sampling. Unbiased Estimators .................. 315  
- **11.17** Stratified Sampling. Ratio Estimates ...................... 316  
- **11.18** Nonlinear Estimation in Complex Surveys ................... 317  
- **11.19** Taylor Series Expansion ................................... 318  
- **11.20** Balanced Repeated Replications ............................ 319  
- **11.21** The Jackknife Method ...................................... 320  
- **11.22** Comparison of the Three Approaches ........................ 323  

**Exercises** ......................................................... 324  

---

## CHAPTER 12  
DOUBLE SAMPLING  
327  

### 12.1 Description of the Technique  
327  

### 12.2 Double Sampling for Stratification  
328  

### 12.3 Optimum Allocation  
331  

### 12.4 Estimated Variance in Double Sampling for Stratification  
333  

### 12.5 Double Sampling for Analytical Comparisons  
334  

### 12.6 Regression Estimators  
335  

### 12.7 Optimum Allocation and Comparison with Single Sampling  
343  

### 12.8 Estimated Variance in Double Sampling for Regression  
344  

### 12.9 Ratio Estimators  
345  

### 12.10 Repeated Sampling of the Same Population  
346  

### 12.11 Sampling on Two Occasions  
348  

### 12.12 Sampling on More than Two Occasions  
353  

### 12.13 Simplifications and Further Developments  
355  

**Exercises**  
355  

## CHAPTER 13  
SOURCES OF ERROR IN SURVEYS  
359  

### 13.1 Introduction  
359  

### 13.2 Effects of Nonresponse  
360  

### 13.3 Types of Nonresponse  
361  

### 13.4 Call-backs  
362  

### 13.5 A Mathematical Model of the Effects of Call-backs  
363  

### 13.6 Optimum Sampling Fraction Among the Nonrespondents  
364  

### 13.7 Adjustment for Bias Without Call-backs  
365  

### 13.8 A Mathematical Model for Errors of Measurement  
366  

### 13.9 Effects of Constant Bias  
368  

### 13.10 Effects of Errors That Are Uncorrelated Within the Sample  
369  

### 13.11 Effects of Intrasample Correlation Between Errors of Measurement  
370  

### 13.12 Summary of the Effects of Errors of Measurement  
371  

### 13.13 The Study of Errors of Measurement  
372  

### 13.14 Repeated Measurement of Subsamples  
373  

### 13.15 Interpenetrating Subsamples  
374  

### 13.16 Combination of Interpenetration and Repeated Measurement  
375  

### 13.17 Sensitive Questions: Randomized Responses  
376  

### 13.18 The Unrelated Second Question  
393  

### 13.19 Summary  
395  

**Exercises**  
396  

---

## Contents

- References ........................................... 400
- Answers to Exercises .......................... 412
- Author Index ........................................ 419
- Subject Index ....................................... 422

---

## Chapter 1

### Introduction

#### 1.1 Advantages of the Sampling Method

Our knowledge, our attitudes, and our actions are based to a very large extent on samples. This is equally true in everyday life and in scientific research. A person's opinion of an institution that conducts thousands of transactions every day is often determined by the one or two encounters he has had with the institution in the course of several years. Travelers who spend 10 days in a foreign country and then proceed to write a book telling the inhabitants how to revive their industries, reform their political system, balance their budget, and improve the food in their hotels are a familiar figure of fun. But in a real sense they differ from the political scientist who devotes 20 years to living and studying in the country only in that they base their conclusions on a much smaller sample of experience and are less likely to be aware of the extent of their ignorance. In science and human affairs alike we lack the resources to study more than a fragment of the phenomena that might advance our knowledge.

This book contains an account of the body of theory that has been built up to provide a background for good sampling methods. In most of the applications for which this theory was constructed, the aggregate about which information is desired is finite and delimited—the inhabitants of a town, the machines in a factory, the fish in a lake. In some cases it may seem feasible to obtain the information by taking a complete enumeration or census of the aggregate. Administrators accustomed to dealing with censuses were at first inclined to be suspicious of samples and reluctant to use them in place of censuses. Although this attitude no longer persists, it may be well to list the principal advantages of sampling as compared with complete enumeration.

**Reduced Cost**

If data are secured from only a small fraction of the aggregate, expenditures are smaller than if a complete census is attempted. With large populations, results accurate enough to be useful can be obtained from samples that represent only a small fraction of the population. In the United States the most important recurrent surveys taken by the government use samples of around 105,000.

---

## Greater Speed

For the same reason, the data can be collected and summarized more quickly with a sample than with a complete count. This is a vital consideration when the information is urgently needed.

## Greater Scope

In certain types of inquiry, highly trained personnel or specialized equipment, limited in availability, must be used to obtain the data. A complete census is impracticable: the choice lies between obtaining the information by sampling or not at all. Thus surveys that rely on sampling have more scope and flexibility regarding the types of information that can be obtained. On the other hand, if accurate information is wanted for many subdivisions of the population, the size of sample needed to do the job is sometimes so large that a complete enumeration offers the best solution.

## Greater Accuracy

Because personnel of higher quality can be employed and given intensive training and because more careful supervision of the field work and processing of results becomes feasible when the volume of work is reduced, a sample may produce more accurate results than the kind of complete enumeration that can be taken.

## 1.2 Some Uses of Sample Surveys

To an observer of developments in sampling over the last 25 years the most striking feature is the rapid increase in the number and types of surveys taken by sampling. The Statistical Office of the United Nations publishes reports from time to time on "Sample Surveys of Current Interest" conducted by member countries. The 1968 report lists surveys from 46 countries. Many of these surveys seek information of obvious importance to national planning on topics such as agricultural production and land use, unemployment and the size of the labor force, industrial production, wholesale and retail prices, health status of the people, and family incomes and expenditures. But more specialized inquiries can also be found: for example, annual earnings (Australia), causes of divorce (Hungary), rural debt and investment (India), household water consumption (Israel), radio listening (Malaysia), holiday spending (Netherlands), waste production of cows (Czechoslovakia), and job vacancies (United States).

Sampling has come to play a prominent part in national decennial censuses. In the United States a 5% sample was introduced into the 1940 Census by asking.

---

## Introduction

Extra questions about occupation, parentage, fertility, and the like, of those persons whose names fell on two of the 40 lines on each page of the schedule. The use of sampling was greatly extended in 1950. From a 20% sample (every fifth line) information was obtained on items such as income, years in school, migration, and service in armed forces. By taking every sixth person in the 20% sample, a further sample of 3½% was created to give information on marriage and fertility. A series of questions dealing with the condition and age of housing was split into five sets, each set being filled in at every fifth house. Sampling was also employed to speed up publication of the results. Preliminary tabulations for many important items, made on a sample basis, appeared more than a year and a half before the final reports.

This process continued in the 1960 and 1970 Censuses. Except for certain basic information required from every person for constitutional or legal reasons, the whole census was shifted to a sample basis. This change, accompanied by greatly increased mechanization, resulted in much earlier publication and substantial savings.

In addition to their use in censuses, continuing samples are employed by government bureaus to obtain current information. In the United States, examples are the Current Population Survey, which provides monthly data on the size and composition of the labor force and on the number of unemployed, the National Health Survey, and the series of samples needed for the calculation of the monthly Consumer Price Index.

On a smaller scale, local governments—city, state, and county—are making increased use of sample surveys to obtain information needed for future planning and for meeting pressing problems. In the United States most large cities have commercial agencies that make a business of planning and conducting sample surveys for clients.

Market research is heavily dependent on the sampling approach. Estimates of the sizes of television and radio audiences for different programs and of newspaper and magazine readership (including the advertisements) are kept continually under scrutiny. Manufacturers and retailers want to know the reactions of people to new products or new methods of packaging, their complaints about old products, and their reasons for preferring one product to another.

Business and industry have many uses for sampling in attempting to increase the efficiency of their internal operations. The important areas of quality control and acceptance sampling are outside the scope of this book. But, obviously, decisions of batches with respect to level or change of quality or to acceptance or rejection of the entire sample could be void only if results obtained from the sample are also valid (within a reasonable tolerance) for the whole batch. The sampling of records of business transactions (accounts, payrolls, stock, personnel)—usually much easier than the sampling of people—can provide serviceable information quickly and economically. Savings can also be made through sampling in the estimation of inventories, in studies of the condition and length of the life of equipment, in the...

---

## Sampling Techniques

Inspection of the accuracy and rate of output of clerical work, in investigating how key personnel distribute their working time among different tasks, and, more generally, in the field known as operations research. The books by Deming (1960) and Slonin (1960) contain many interesting examples showing the range of applications of the sampling method in business.

Opinion, attitude, and election polls, which did much to bring the technique of sampling before the public eye, continue to be a popular feature of newspapers. In the field of accounting and auditing, which has employed sampling for many years, a new interest has arisen in adapting modern developments to the particular problems of this field. Thus, Neter (1972) describes how airlines and railways save money by using samples of records to apportion income from freight and passenger service. The status of sample surveys as evidence in lawsuits has also been subject to lively discussion. Gallup (1972) has noted the major contribution that sample surveys can make to the process of informed government by determining quickly people's opinions on proposed or new government programs and has stressed their role as sources of information in social science.

Sample surveys can be classified broadly into two types—**descriptive** and **analytical**. In a descriptive survey the objective is simply to obtain certain information about large groups: for example, the numbers of men, women, and children who view a television program. In an analytical survey, comparisons are made between different subgroups of the population, in order to discover whether differences exist among them and to form or to verify hypotheses about the reasons for these differences. The Indianapolis fertility survey, for instance, was an attempt to determine the extent to which married couples plan the number and spacing of their children, the husband's and wife's attitudes toward this planning, the reasons for these attitudes, and the degree of success attained (Kiser and Whelpton, 1953).

The distinction between descriptive and analytical surveys is not, of course, clear-cut. Many surveys provide data that serve both purposes. Along with the rise in the number of descriptive surveys, there has, however, been a noticeable increase in surveys taken primarily for analytical purposes, particularly in the study of human behavior and health. Surveys of the teeth of school children before and after fluoridation of water, of the death rates and causes of death of people who smoke different amounts, and the huge study of the effectiveness of the Salk polio vaccine may be cited. The study by Coleman (1966) on equality of educational opportunity, conducted on a national sample of schools, contained many regression analyses that estimated the relative contributions of school characteristics, home background, and the child's outlook to variations in exam results.

### 1.3 The Principal Steps in a Sample Survey

As a preliminary to a discussion of the role that theory plays in a sample survey, it is useful to describe briefly the steps involved in the planning and execution of a

---

## Introduction

Surveys vary greatly in their complexity. To take a sample from 5000 cards, neatly arranged and numbered in a file, is an easy task. It is another matter to sample the inhabitants of a region where transport is by water through the forests, where there are no maps, where 15 different dialects are spoken, and where the inhabitants are very suspicious of an inquisitive stranger. Problems that are baffling in one survey may be trivial or nonexistent in another.

The principal steps in a survey are grouped somewhat arbitrarily under 11 headings.

### Objectives of the Survey

A lucid statement of the objectives is most helpful. Without this, it is easy in a complex survey to forget the objectives when engrossed in the details of planning, and to make decisions that are at variance with the objectives.

### Population to be Sampled

The word **population** is used to denote the aggregate from which the sample is chosen. The definition of the population may present no problem, as when sampling a batch of electric light bulbs in order to estimate the average length of life of a bulb. In sampling a population of farms, on the other hand, rules must be set up to define a farm, and borderline cases arise. These rules must be usable in practice: the enumerator must be able to decide in the field, without much hesitation, whether or not a doubtful case belongs to the population.

The population to be sampled (the **sampled population**) should coincide with the population about which information is wanted (the **target population**). Sometimes, for reasons of practicability or convenience, the sampled population is more restricted than the target population. If so, it should be remembered that conclusions drawn from the sample apply to the sampled population. Judgment about the extent to which these conclusions will also apply to the target population must depend on other sources of information. Any supplementary information that can be gathered about the nature of the differences between sampled and target population may be helpful.

### Data to be Collected

It is well to verify that all the data are relevant to the purposes of the survey and that no essential data are omitted. There is frequently a tendency, particularly with human populations, to ask too many questions, some of which are never subsequently analyzed. An overlong questionnaire lowers the quality of the answers to important as well as unimportant questions.

### Degree of Precision Desired

The results of sample surveys are always subject to some uncertainty because only part of the population has been measured and because of errors of measurement. This uncertainty can be reduced by taking larger samples and by using...

---

## Methods of Measurement

There may be a choice of measuring instrument and of method of approach to the population. Data about a person's state of health may be obtained from statements that he or she makes or from a medical examination. The survey may employ a self-administered questionnaire, an interview where the respondent is asked a set of questions with no discretion, or an interviewing process that allows much latitude in the form and ordering of the questions. The approach may be by mail, by telephone, by personal visit, or by a combination of the three. Much study has been made of interviewing methods and problems (see, e.g., Hyman, 1954 and Payne, 1951).

A major part of the preliminary work is the construction of record forms on which the questions and answers are to be entered. With simple questionnaires, the answers can sometimes be precoded—that is, entered in a manner in which they can be routinely transferred to mechanical equipment. In fact, for the construction of good record forms, it is necessary to visualize the structure of the final summary tables that will be used for drawing conclusions.

## The Frame

Before selecting the sample, the population must be divided into parts that are called sampling units, or units. These units must cover the whole of the population and they must not overlap, in the sense that every element in the population belongs to one and only one unit. Sometimes the appropriate unit is obvious, as in a population of light bulbs, in which the unit is the single bulb. Sometimes there is a choice of unit. In sampling the people in a town, the unit might be an individual person, the members of a family, or all persons living in the same city block. In sampling an agricultural crop, the unit might be a field, a farm, or an area of land whose shape and dimensions are at our disposal.

The construction of this list of sampling units, called a frame, is often one of the major practical problems. From bitter experience, samplers have acquired a critical attitude toward lists that have been routinely collected for some purpose. These assurances to the contrary, such lists are often found to be incomplete, partly illegible, or to contain an unknown amount of duplication. A good frame may be hard to come by when the population is specialized, as in populations of bookkeepers or people who keep turkeys. Jessen (1955) presents an interesting method of constructing a frame from the branches of a fruit tree.

---

## Selection of the Sample

There is now a variety of plans by which the sample may be selected. For each plan that is considered, rough estimates of the size of sample can be made from a knowledge of the degree of precision desired. The relative costs and time involved for each plan are also compared before making a decision.

## The Pretest

It has been found useful to try out the questionnaire and the field methods on a small scale. This nearly always results in improvements in the questionnaire and may reveal other troubles that will be serious on a large scale, for example, that the cost will be much greater than expected.

## Organization of the Field Work

In extensive surveys many problems of business administration are met. The personnel must receive training in the purpose of the survey and in the methods of measurement to be employed and must be adequately supervised in their work. A procedure for early checking of the quality of the returns is invaluable. Plans must be made for handling nonresponse, that is, the failure of the enumerator to obtain information from certain of the units in the sample.

## Summary and Analysis of the Data

The first step is to edit the completed questionnaires, in the hope of amending recording errors, or at least of deleting data that are obviously erroneous. Decisions about computing procedure are needed in cases in which answers to certain questions were omitted by some respondents or were deleted in the editing process. Thereafter, the computations that lead to the estimates are performed. Different methods of estimation may be available for the same data.

In the presentation of results it is good practice to report the amount of error to be expected in the most important estimates. One of the advantages of probability sampling is that such statements can be made, although they have to be severely qualified if the amount of nonresponse is substantial.

## Information Gained for Future Surveys

The more information we have initially about a population, the easier it is to devise a sample that will give accurate estimates. Any completed sample is potentially a guide to improved future sampling, in the data that it supplies about the means, standard deviations, and nature of the variability of the principal variables and about the costs involved in getting the data. Sampling practice advances more rapidly when provisions are made to assemble and record information of this type.

There is another important respect in which any completed sample facilitates future samples. Things never go exactly as planned in a complex survey. The after

---

## 1.4 The Role of Sampling Theory

The list of steps in a sample survey has been given in order to emphasize that sampling is a practical business, which calls for several different types of skill. In some of the steps—the definition of the population, the determination of the data to be collected and of the methods of measurement, and the organization of the field work—sampling theory plays at most a minor role. Although these topics are not discussed further in this book, their importance should be realized. Sampling demands attention to all phases of the activity: poor work in one phase may ruin a survey in which everything else is done well.

The purpose of sampling theory is to make sampling more efficient. It attempts to develop methods of sample selection and of estimation that provide, at the lowest possible cost, estimates that are precise enough for our purpose. This principle of specified precision at minimum cost recurs repeatedly in the presentation of theory.

In order to apply this principle, we must be able to predict, for any sampling procedure that is under consideration, the precision and the cost to be expected. So far as precision is concerned, we cannot foretell exactly how large an error will be present in an estimate in any specific situation, for this would require a knowledge of the true value for the population. Instead, the precision of a sampling procedure is judged by examining the frequency distribution generated for the estimate if the procedure is applied again and again to the same population. This is, of course, the standard technique by which precision is judged in statistical theory.

A further simplification is introduced. With samples of the sizes that are common in practice, there is often good reason to suppose that the sample estimates are approximately normally distributed. With a normally distributed estimate, the whole shape of the frequency distribution is known if we know the mean and the standard deviation (or the variance). A considerable part of sample survey theory is concerned with finding formulas for these means and variances.

There are two differences between standard sample survey theory and the classical sampling theory as taught in books on mathematical statistics. In classical theory the measurements that are made on the sampling units in the population are usually assumed to follow a frequency distribution, for example, the normal distribution, of known mathematical form apart from certain population parameters such as the mean and variance whose values have to be estimated from the sample data. In sample survey theory, on the other hand, the attitude has been to proceed with very limited information about the frequency distribution. In particular, its mathematical form is not assumed known, so that the approach might be described as model-free or distribution-free. This attitude is natural for

---

## 1.5 Probability Sampling

The sampling procedures considered in this book have the following mathematical properties in common.

1. We are able to define the set of distinct samples, \( S_1, S_2, \ldots, S_k \), which the procedure is capable of selecting if applied to a specific population. This means that we can say precisely what sampling units belong to \( S_1, S_2, \) and so on. For example, suppose that the population contains six units, numbered 1 to 6. A common procedure for choosing a sample of size 2 gives three possible candidates—\( S_1 = (1, 4); S_2 = (2, 5); S_3 = (3, 6) \). Note that not all possible samples of size 2 need be included.

2. Each possible sample \( S_i \) has assigned to it a known probability of selection \( \pi_i \).

3. We select one of the \( S_i \) by a random process in which each \( S_i \) receives its appropriate probability of \( \pi_i \) of being selected. In the example we might assign equal probabilities to the three samples. Then the draw itself can be made by choosing a random number between 1 and 3. If this number is \( j \), \( S_j \) is the sample that is taken.

4. The method for computing the estimate from the sample must be stated and must lead to a unique estimate for any specific sample. We may declare, for example, that the estimate is to be the average of the measurements on the individual units in the sample.

For any sampling procedure that satisfies these properties, we are in a position to calculate the frequency distribution of the estimates it generates if repeatedly applied to the same population. We know how frequently any particular sample \( S_i \) will be selected, and we know how to calculate the estimate from the data in \( S_i \). We are, therefore, at a sampling theory can be developed for any procedure that satisfies these conditions. Much of the development may be intricate: these probability sampling refers to a method of this type.

In practice we seldom draw a probability sample by writing down the \( S_i \) and \( \pi_i \) as outlined above. This is intolerably laborious with a large population, where a sampling procedure may produce billions of possible samples. The draw is most...

---

## 1.6 Alternatives to Probability Sampling

The following are some common types of nonprobability sampling:

1. **Sample Restriction**: The sample is restricted to a part of the population that is readily accessible.  
   - Example: A sample of coal from an open wagon may be taken from the top 6 to 9 inches.

2. **Haphazard Selection**: The sample is selected haphazardly.  
   - Example: In picking 10 rabbits from a large cage in a laboratory, the investigator may take those that his hands rest on, without conscious planning.

3. **Small but Heterogeneous Population**: The sampler inspects the whole and selects a small sample of "typical" units—units that are close to his impression of the average of the population.

4. **Volunteer Samples**: The sample consists essentially of volunteers, in studies in which the measuring process is unpleasant or troublesome to the person being measured.

Under the right conditions, any of these methods can give useful results. They are not, however, amenable to the development of a sampling theory that is model-free, since no element of random selection is involved. Another way of examining how good one of them may be is to find a situation in which the results are known, either for the whole population or for a probability sample, and make comparisons. Even if a method appears to do well in one such comparison, this does not guarantee that it will do well under different circumstances.

In this connection, some of the earliest uses of sampling by country and city governments from 1850 onward were intended to save money in making estimates from the results of a Census. For the most important items in the Census, the country or city totals were calculated from the complete Census data. For other items a sample of 15% or 25% of the Census returns was selected in order to lighten the work of estimating country or city totals for these items. Two rival methods of sample selection came into use. One, called **random selection**, was an application of probability sampling in which each unit in the population (e.g., each Census return) had an equal chance of being included in the sample. For this method it was realized that by use of sampling theory and the normal distribution, as noted previously, the sampler could predict approximately from the sample data the amount of error to be expected in the estimates made from the sample. Moreover, for the most important items for which complete Census data were available, he could check to some extent the accuracy of the predictions.

The other method was **purposive selection**. This was not a sampling method in detail but usually had two common features. The sampling unit consisted of groups of returns, often relatively large groups. For example, in the 1921 Italian Census...

---

## Introduction

Census the country consisted of 8354 communes grouped into 214 districts. In drawing a 14% sample, the Italian statisticians Gini and Galvani selected 29 districts purposely rather than 1250 communes. Second, the 29 districts were chosen so that the sample gave accurate estimates for 7 important control variables for which results were known for the whole country. The hope was that this sample would give good estimates for other variables highly correlated with the control variables.

In the 1920s the International Statistical Institute appointed a commission to report on the advantages and disadvantages of the two methods. The report, by Jensen (1926), seemed on balance to favor purposive selection. However, purposive selection was abandoned relatively soon as a method of sampling for obtaining national estimates in surveys in which many items were measured. It lacked the flexibility that later developments of probability sampling produced, it was unable to predict from the sample the accuracy to be expected in the estimates, and it used sampling units that were too large. Gini and Galvani concluded that the probability method called stratified random sampling (Chapter 5), with the commune as a sampling unit, would have given better results than their method.

### 1.7 Use of the Normal Distribution

It is sometimes useful to employ the word **estimator** to denote the rule by which an estimate of some population characteristic is calculated from the sample results, the word **estimate** being applied to the value obtained from a specific sample. An estimator of given by a sampling plan is called unbiased if the mean value of , taken over all possible samples provided by the plan, is equal to . In the notation of section 1.5, this condition may be written

\[ E(\hat{\mu}) = \sum_{i} \pi_i \hat{\mu}_i = \mu \]

where is the estimate given by the th sample. The symbol stands for "the expected value of," is used frequently.

As mentioned in section 1.4, the samples in surveys are often large enough so that estimates made from them are approximately normally distributed. Furthermore, with probability sampling, we have formulas that give the mean and variance of the estimates. Suppose that we have taken a sample by a procedure known to give an unbiased estimator and have computed the sample estimate and its standard deviation (often called, alternatively, its standard error). How good is the estimate? We cannot know the exact value of the error of estimate , but from the properties of the normal curve, the chances are

- 0.32 (about 1 in 3) that the absolute error exceeds 
- 0.05 (1 in 20) that the absolute error exceeds 
- 0.01 (1 in 100) that the absolute error exceeds 

---

```markdown
## Sampling Techniques

For example, if a probability sample of the records of batteries in routine use in a large factory shows an average life \( \bar{x} = 394 \) days, with a standard error \( \sigma_{\bar{x}} = 4.6 \) days, the chances are 99 in 100 that the average life in the population of batteries lies between

\[
\hat{\mu} = 394 - (2.58)(4.6) = 382 \text{ days}
\]

and

\[
\hat{\mu} = 394 + (2.58)(4.6) = 406 \text{ days}
\]

The limits, 382 days and 406 days, are called lower and upper confidence limits. With a single estimate from a single survey, the statement "μ lies between 382 and 406 days" is not certain to be correct. The "99% confidence" figure implies that if the same sampling plan were used many times in a population, a confidence statement being made from each sample, about 99% of those statements would be correct and 1% wrong. When sampling is being introduced into an operation in which complete censuses have previously been used, a demonstration of this property is sometimes made by drawing repeated samples of the type proposed from a population for which complete records exist, so that μ is known (see, e.g., Trueblood and Cyert, 1957). The practical verification that approximately the stated proportion of statements is correct does much to educate and reassure administrators about the nature of sampling. Similarly, when a single sample is taken from each of a series of different populations, about 95% of the 95% confidence statements are correct.

The preceding discussion assumes that \( \sigma_{\bar{x}} \), as computed from the sample, is known exactly. Actually, \( \sigma_{\bar{x}} \), like \( \bar{x} \), is subject to a sampling error. With a normally distributed variable, tables of Student's t distribution are used instead of the normal tables to calculate confidence limits for μ when the sample is small. Replacement of the normal table by the t table makes almost no difference if the number of degrees of freedom in \( \sigma_{\bar{x}} \) exceeds 50. With certain types of stratified sampling and with the method of replicated sampling (section 11.19) the degrees of freedom are small and the t table is needed.

## 1.8 Bias and Its Effects

In sample survey theory it is necessary to consider biased estimators for two reasons.

1. In some of the most common problems, particularly in the estimation of ratios, estimators that are otherwise convenient and suitable are found to be biased.

2. Even with estimators that are unbiased in probability sampling, errors of measurement and nonresponse may produce biases in the numbers that we are able to compute from the data. This happens, for instance, if the persons who refuse to be interviewed are almost all opposed to some expenditure of public funds, whereas those who are interviewed are split evenly for and against.
```

---

## Introduction

![Fig 1.1](image-url)  
**Fig 1.1** Effect of bias on errors of estimation.

To examine the effect of bias, suppose that the estimate \(\hat{μ}\) is normally distributed about a mean \(m\) that is a distance \(B\) from the true population value \(\mu\), as shown in Fig. 1.1. The amount of bias is \(B = m - \mu\). Suppose that we do not know that any bias is present. We compute the standard deviation \(\sigma\) of the frequency distribution of the estimate—this will, of course, be the standard deviation about the mean \(m\) of the distribution, not about the true mean \(\mu\). We are using \(\sigma\) in place of \(\sigma_{\hat{μ}}\). As a statement about the accuracy of the estimate, we declare that the probability is 0.05 that the estimate \(\hat{μ}\) is in error by more than 1.96σ.

We will consider how the presence of bias distorts this probability. To do this, we calculate the true probability that the estimate is in error by more than 1.96σ, where error is measured from the true mean \(\mu\). The two tails of the distribution must be examined separately. For the upper tail, the probability of an error of more than +1.96σ is the shaded area above \(Q\) in Fig. 1.1. This area is given by

\[
\frac{1}{\sqrt{2\pi}} \int_{x=1.96-\frac{B}{\sigma}}^{\infty} e^{-x^2/2} dx
\]

Put \(\hat{μ} - m = \sigma t\). The lower limit of the range of integration for \(t\) is

\[
\frac{\mu - m}{\sigma} + 1.96 = 1.96 - \frac{B}{\sigma}
\]

Thus the area is

\[
\frac{1}{\sqrt{2\pi}} \int_{t=1.96-(B/\sigma)}^{\infty} e^{-t^2/2} dt
\]

---

## Table 1.1  
**Effect of a Bias B on the Probability of an Error Greater than 1.96σ**

| B/σ | Probability of Error | Total |
|-----|----------------------|-------|
|     | < -1.96σ             | > 1.96σ |       |
| 0.02| 0.0238               | 0.0262 | 0.0500 |
| 0.04| 0.0228               | 0.0274 | 0.0502 |
| 0.06| 0.0217               | 0.0287 | 0.0504 |
| 0.08| 0.0207               | 0.0301 | 0.0508 |
| 0.10| 0.0197               | 0.0314 | 0.0511 |
| 0.20| 0.0154               | 0.0392 | 0.0546 |
| 0.40| 0.0095               | 0.0504 | 0.0599 |
| 0.60| 0.0052               | 0.0609 | 0.0661 |
| 0.80| 0.0029               | 0.1230 | 0.1259 |
| 1.00| 0.0015               | 0.1685 | 0.1700 |
| 1.50| 0.0003               | 0.3228 | 0.3231 |

For the total probability of an error of more than 1.96σ, the bias has little effect provided that it is less than one tenth of the standard deviation. At this point the total probability is 0.0511 instead of the 0.05 that we think it is. As the bias increases further, the disturbance becomes more serious. At B = σ, the total probability of error is 0.17, more than three times the presumed value.

The two tails are affected differently. With a positive bias, as in this example, the probability of an underestimate by more than 1.96σ shrinks rapidly from the presumed 0.025 to become negligible when B = σ. The probability of the corresponding overestimate mounts steadily. In most applications the total error is the primary interest, but occasionally we are particularly interested in errors in one direction.

As a working rule, the effect of bias on the accuracy of an estimate is negligible if the bias is less than one tenth of the standard deviation of the estimate. If we have a biased method of estimation for which B/σ < 0.1, where B is the absolute value of the bias, it can be claimed that the bias is not an appreciable disadvantage of the method.

---

## 1.9 The Mean Square Error

In order to compare a biased estimator with an unbiased estimator, or two estimators with different amounts of bias, a useful criterion is the mean square error (MSE) of the estimate, measured from the population value that is being estimated. Formally,

\[ \text{MSE}(\hat{a}) = E(\hat{a} - \mu)^2 = E[(\hat{a} - m) + (m - \mu)]^2 \]

\[ = E(\hat{a} - m)^2 + 2(m - \mu)E(\hat{a} - m) + (m - \mu)^2 \]

\[ = (\text{variance of } \hat{a}) + (\text{bias})^2 \]

the cross-product term vanishing since \( E(\hat{a} - m) = 0 \).

Use of the MSE as a criterion of the accuracy of an estimator amounts to regarding two estimates that have the same MSE as equivalent. This is not strictly correct because the frequency distributions of errors \((\hat{a} - \mu)\) of different sizes will not be the same for the two estimates if they have different amounts of bias. It has been shown, however, by Hansen, Hurwitz, and Madow (1953) that if \( B/\sigma \) is less than about one half, the two frequency distributions are almost identical in regard to absolute errors \(|\hat{a} - \mu|\) of different sizes. Table 1.2 illustrates this result.

### Table 1.2

**Probability of an Absolute Error ≥ \( \frac{1}{\sqrt{\text{MSE}}} \), 1.96 \( \sqrt{\text{MSE}} \) and 2.576 \( \sqrt{\text{MSE}} \)**

| \( B/\sigma \) | \( 1/\sqrt{\text{MSE}} \) | 1.96 \( \sqrt{\text{MSE}} \) | 2.576 \( \sqrt{\text{MSE}} \) |
|---------------|---------------------------|-----------------------------|-----------------------------|
| 0.0           | 0.317                     | 0.0500                      | 0.0100                      |
| 0.1           | 0.320                     | 0.0509                      | 0.0102                      |
| 0.2           | 0.324                     | 0.0520                      | 0.0105                      |
| 0.3           | 0.342                     | 0.0573                      | 0.0120                      |
| 0.4           | 0.374                     | 0.0679                      | 0.0148                      |

---

## EXERCISES

1.1 Suppose that you were using sampling to estimate the total number of words in a book that contains illustrations.
   - (a) Is there any problem of definition of the population? (b) What are the pros and cons of (1) the page, (2) the line, as a sampling unit?

1.2 A sample is to be taken from a list of names that are on cards (one name to a card) numbered consecutively in a file. Each name is to have an equal chance of being drawn in the sample. What problems arise in the following common situations? 
   - (a) Some of the names do not belong to the target population, although this fact cannot be verified for any name until it has been drawn.
   - (b) Some names appear on more than one card. All cards with the same name appear consecutively in the file.
   - (c) Some names appear on more than one card, but cards bearing the same name may be scattered anywhere about the file.

1.3 The problem of finding a frame that is complete and enables the sample to be drawn is often an obstacle. What kinds of frames might be tried for the following surveys? Have the frames any serious weaknesses?
   - (a) A survey of stores that sell luggage in a large city.
   - (b) A survey of the kinds of articles left behind in subways or buses.
   - (c) A survey of persons present by family members in watching television.

1.4 A city directory, A, lists its addresses in order along each street, and gives the names of the persons living at each address. For a current interview survey of the people in the city, what are the deficiencies of this frame? Can they be remedied by the interviewer during the course of the field work? In using the directory, would you draw a list of addresses (dwelling places) or a list of persons?

1.5 In estimating the average retail value of the small items in the inventory of a large firm, a sample of the book value was recorded for each item in the sample. For the total sample, the ratio of the actual to book value was 1.021, this estimate being approximately normally distributed with a standard error of 0.0082. If the book value of the inventory is $8,600,000, construct a 95% confidence limit for the actual value.

1.6 Frequently the estimates made for a sample, although at first sight they appear to be complete, require emendation. A proprietor in a market finds that business is poor on Sunday morning. At the end of Sunday's operation, his average receipts per Sunday morning are $10. The standard error of this figure, computed from week-to-week variations, is $1.52. The estimates of future profit is $5 per Sunday morning. What is the confidence limit about the long-term profit rate will be at least $5? What assumption must be made in order to answer this question?

---

## INTRODUCTION

### 1.7
In Table 1.2, what happens to the probability of exceeding 1√MSE, 1.96√MSE, and 2.576√MSE when B/σ tends to infinity, that is, when the MSE is due entirely to bias? Do your results agree with the directions of the changes noted in Table 1.2 as B/σ moves from 0 to 0.6?

### 1.8
When it is necessary to compare two estimates that have different frequency distributions of errors (μ̂ - μ), it is occasionally possible, in specialized problems, to compute the cost or loss that will result from an error (μ̂ - μ) of any given size. The estimate that gives the smaller expected loss is preferred, other things being equal. Show that if the loss is a quadratic function A(μ̂ - μ)² of the error, we should choose the estimate with the smaller mean square error.