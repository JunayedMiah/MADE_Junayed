# Project Plan

## Title
Reveal Crash Severity: A Comprehensive Analysis of Location, Weather, and Time Factors.

## Main Question

What factors contribute to the severity of motor vehicle crashes?

## Description

In this project, I use features like crash location, time weather conditions, and road type to predict the seriousness of crashes (e.g., minor, serious, fatal) and explain how analyzing crash data helps reduce accidents, inform policymakers, and improve public safety.

## Datasources

### Data Source-1: Montgomery County Crash Data Source:
* Metadata URL: https://catalog.data.gov/dataset/crash-reporting-drivers-data
* Data URL: https://data.montgomerycountymd.gov/api/views/mmzv-x632/rows.csv?accessType=DOWNLOAD
* License: Open Data Common Public Domain and License (ODC PDDL)

The dataset provides me with detailed information about motor vehicle crashes in Montgomery County, including crash date, route type, road conditions, weather, and driver at fault. It offers many details about the factors related to crash severity.

### Data Source-2: New York City Vehicle Collision Data Source:
* Metadata URL: https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes
* Data URL: https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD
* License: Available through NYC OpenData, aligning with open-data principles, ensuring it can be used without legal constraints.

Provides detailed records of motor vehicle collisions, including location, time, injuries, and fatalities. There are some major fields like Crash Date, Borough, Number of persons injured, Latitude etc.

## Work Packages

 ### Work Package 1: Data Collection
 #####  Import tertiary education enrollment data from the data source into a pandas DataFrame for analysis.

 ### Work Package 2: Data Cleaning
 #####  Address missing values, remove duplicates, and validate the accuracy of enrollment rates and other relevant fields to ensure data integrity.

 ### Work Package 3: Exploratory Analysis
 ##### To focus on essential data for predictive analysis.

 ### Work Package 4: Data Pipeline Development
 #####  Design a modular data pipeline for efficient data extraction, transformation, and storage, ensuring easy updates and maintenance.

 ### Work Package 5: Reporting and Visualization
 #####  Summarize key findings in a report and create visualizations (charts and graphs) to effectively find out the insights.
