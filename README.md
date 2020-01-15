# Kickstarter Campaign Classification [Machine Learning]

[![Build Status](https://travis-ci.com/mishaberrien/kickstarter_campaign_classification.svg?branch=master)](https://travis-ci.com/mishaberrien/kickstarter_campaign_classification)

#### -- Project Status: [Active]

## Project Intro/Objective
Kickstarter is a US based global crowd funding platform focused on bringing funding to creative projects. Since the platform’s launch in 2009, the site has hosted over 159,000 successfully funded projects with over 15 million unique backers. Kickstarter uses an “all-or-nothing” funding system. This means that funds are only dispersed for projects that meet the original funding goal set by the creator.

Kickstarter earns 5% commission on projects that are successfully funded. Currently, less than 40% of projects on the platform succeed. The objective is to predict which projects are likely to succeed so that these projects can be highlighted on the site either through 'staff picks' or 'featured product' lists.

### Collaborators
|Name     |  Github Page   |  Personal Website  |
|---------|-----------------|--------------------|
|Nateé Johnson| [nateej1](https://github.com/nateej1) | --- |
|Misha Berrien | [mishaberrien](https://github.com/mishaberrien)| [www.mishaberrien.com](https://mishaberrien.com/)  |

### Methods Used
* Machine Learning
* Data Visualization
* Predictive Modeling

### Technologies
* Python
* Pandas, jupyter

## Project Description
In order to increase the number of successful campaigns, we propose two related solutions:
* Predict Successful Campaigns and promote those with the lowest predicted probability of being successful.
* Contact creators from those campaigns that are just below the “success” margin and give them insights that will help them succeed.
Locations of campaigns included in the dataset, as of July 2019, were visualized in an [interactive map](https://nateej1.github.io/kickstarter-campaign-classification/). Marker icons/colors indicate the campaign status at the time of creation, and selecting a marker provides more details about the project it represents. 

## Getting Started

1. Clone this repo.
2. A sample of the the deduplicated dataset can be found in the data_sample folder [here](https://github.com/mishaberrien/kickstarter-campaign-classification/tree/master/data_sample).
3. In order to reproduce results first open the "results" file located in the results folder [here](https://github.com/mishaberrien/kickstarter-campaign-classification/tree/master/results). Then change the two file paths at the beginning of the document

_from:_

```
kick_deduped = pd.read_csv('../../data/02_intermediate/kick_deduped.csv.zip')
cluster_features_df =  pd.read_csv('../../data/03_processed/KNN_cluster_features_.csv'))
```
_to:_

```
kick_deduped = pd.read_csv('../../data_sample/kick_deduped_sample.csv.zip')
cluster_features_df =  pd.read_csv('../../data_sample/KNN_cluster_features_.csv'))
```
then run the results file.

4. The data processing/transformation scripts are being kept in the src folder [here](https://github.com/mishaberrien/kickstarter_campaign_classification/tree/master/src)

5. A data dictionary can be found in the references folder [here](https://github.com/mishaberrien/kickstarter_campaign_classification/tree/master/references)


## Featured Notebooks/Analysis/Deliverables
* [Technical Results Notebook](https://mishaberrien.com/kickstarter_campaign_classification/)
* [Executive Summary](https://github.com/nateej1/kickstarter-campaign-classification/blob/master/results/Executive_summary-Kickstarter_campaign_classification.pdf)
* [Geographic Mapping of Kickstarter Projects](https://nateej1.github.io/kickstarter-campaign-classification/)

---

This file structure is based on the [DSSG machine learning pipeline](https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/0_before_you_start/pipelines-and-project-workflow).
