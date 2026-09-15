# 🍔 Chicago Food Inspection Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-DataFrame-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Under_Development-yellow.svg)

> 🚧 **Under Development** — This project is actively being built. Features and analyses are being added regularly.


## 📋 Description
Chicago Food Inspections Analytics is a data analysis project that explores the City of Chicago's food inspection records to uncover patterns in restaurant compliance, inspection outcomes, and food safety risk. Using publicly available data from the Chicago Department of Public Health, this project transforms raw inspection logs into actionable insights through cleaning, exploratory analysis, and visualization.


## 🎯 Objectives
1. Clean and Prepare the Data — Handle missing values, inconsistent formatting, duplicate records, and data type issues to produce a reliable, analysis-ready dataset.
2. Explore Inspection Outcomes — Analyze the distribution of inspection results (Pass, Fail, Pass w/ Conditions) over time and across facility types.
3. Identify Common Violations — Determine which violations appear most frequently and how they correlate with inspection failures.
4. Analyze Geographic Patterns — Examine how inspection outcomes and violation rates vary across Chicago's wards, ZIP codes, and community areas.
5. Assess Risk Factors — Investigate the relationship between facility risk level, inspection frequency, and outcomes.
6. Visualize Key Findings — Produce clear, informative charts and dashboards that communicate insights to a non-technical audience.
7. Generate Actionable Insights — Provide data-driven recommendations that could help inspectors prioritize high-risk establishments or help restaurants improve compliance.


## 📊 Dataset
- Data owner: [Chicago Department of Public Health](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data)  
- This dataset contains information from inspections of restaurants and other food establishments in Chicago from January 1, 2010 to the present.
- What's in this Dataset? 315K+ rows, 17 columns, each row is a food inspection
- Columns:
    - DBA: ‘Doing business as.’ This is legal name of the establishment. 
    - AKA: ‘Also known as.’ This is the name the public would know the establishment as. 
    - License number: This is a unique number assigned to the establishment for the purposes of licensing.
    - Type of facility: Each establishment is described by one of the following: bakery, banquet hall, candy store, caterer, coffee shop, ...
    - Risk category of facility: Each establishment is categorized as to its risk of adversely affecting the public’s health, with 1 being the highest and 3 the lowest. 
    - Street address, city, state and zip code of facility: This is the complete address where the facility is located. 
    - Inspection date: This is the date the inspection occurred.
    - Inspection type: An inspection can be one of the following types: canvass, performed at a frequency relative to the risk of the establishment; consultation, when the inspection is done at the request of the owner prior to the opening of the establishment; complaint, when the inspection is done in response to a complaint against the establishment; license, when the inspection is done as a requirement for the establishment to receive its license to operate; suspect food poisoning, when the inspection is done in response to one or more persons claiming to have gotten ill as a result of eating at the establishment (a specific type of complaint- based inspection); task-force inspection, when an inspection of a bar or tavern is done. 
    - Results: An inspection can pass, pass with conditions or fail. 
    - Violations: An establishment can receive one or more of 45 distinct violations (violation numbers 1-44 and 70). 


## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **Core:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Quality:** pytest, structured logging, pydantic-typed config
- **Tooling:** pyproject.toml, Git (Conventional Commits)


## 📝 License
This project is licensed under the MIT License.

## 🙌 Acknowledgments
- Chicago Department of Public Health
- The open-source Python community