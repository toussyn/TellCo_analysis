# TellCo_Analysis

---

**Table of Contents**

- [TellCo Analysis](#TellCo_Analysis)
  - [Overview](#overview)
  - [Business Need - The Scenario](#Business-Need---The-Scenario)
  - [The Approach](#theapproach)
  - [Repo Structure](#project-structure)
    - [.github](#.github)
    - [dashboard](#dashboard)
    - [data](#data)
    - [models](#models)
    - [notebooks](#notebooks)
    - [screenshots](#screenshots)
    - [scripts](#scripts)
    - [root folder](#root-folder)
  - [Installation guide](#installation-guide)

***

## Overview
In this repository contains detailed analytics and modeling of telecomunications dataset of a company called TellCo. This project is part of 10 academy's training week 1 challenge. The project's objective is to analyze opportunities for growth and make a recommendation on whether TellCo is worth buying or not.

## Business Need - The Scenario
You are working for a wealthy investor that specializes in purchasing assets that are undervalued. The investor is interested in purchasing TellCo, an existing mobile service provider in the Republic of Pefkakia. You will analyze a telecommunication dataset that contains useful information about the customers & their activities on the network. Your job is to perform detailed analysis to understand the fundamentals of the business and especially to identify opportunities to drive profitability by changing the focus of which products or services are being offered.

## The Approach
The project is divided and implemented by the following sections
1. User Overview analysis
2. User Engagement analysis
3. User Experience analysis
4. User Satisfaction analysis
5. Serving results of the analyses on a web dashboard

## Repo Structure
The repository has a number of files and folders that houses python scripts, jupyter notebooks, raw and cleaned data, and text files. The following is their structure with a brief explanation.

### Folders

#### .github
- a configuration file for github actions and workflow
- `workflows/CI.yml` continous integration configuration

#### dashboard
- the folder where all the multiple dashboard pages belong
- `UserEngagement.py` dashboard page for presenting the findings in `User Engagement Analysis.ipynb`
- `UserExperience.py` dashboard page for presenting the findings in `User Experience analysis.ipynb`
- `UserOverview.py` dashboard page for presenting the findings in `User Overview analysis.ipynb`
- `UserSatisfaction.py` dashboard page for presenting the findings in `User Engagement Analysis.ipynb`

#### data
- the folder where the raw, and cleaned datasets' csv files are stored

#### models
- the folder where models' pickle files are stored

#### notebooks
- `Data Cleaning, Transforming and Extraction.ipynb`: a jupyter notebook that handles data cleaning tranformation and extraction
- `User Overview analysis.ipynb`: a jupyter notebook that analyzes general users' behaviours
- `User Engagement analysis.ipynb`: a jupyter notebook that analyzes the engagement of users
- `User Experience analysis.ipynb`: a jupyter notebook that analyzes users' network experience
- `User Satisfaction analysis.ipynb`: a jupyter notebook that analyzes the satisfaction of users

#### scripts
- `clean_dataframe.py`: a python script for cleaning pandas dataframes
- `plot_dataframe.py`: a python script for plotting selected data
- `utils.py`: a python script for cleaning outliers in a pandas dataframe
- `logger.py`: a python script used for writing logs to corresponding log files

### Files
- `requirements.txt`: a text file lsiting the projet's dependancies
- `.gitignore`: a text file listing files and folders to be ignored
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

## Installation guide
Option 1
```
git clone https://github.com/natyrix/Telecommunication-Industry-User-Analytics
cd Telecommunication-Industry-User-Analytics
pip install -r requirements.txt 
```
Option 2
```
git clone https://github.com/natyrix/Telecommunication-Industry-User-Analytics
cd Telecommunication-Industry-User-Analytics
pip install .
```

