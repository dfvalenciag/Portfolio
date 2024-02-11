# Data science project about Food inspections

## Description: 
This dataset contains information from inspections of restaurants and other food establishments in Chicago from January 1, 2010 to the present. This information is derived from inspections of restaurants and other food establishments in Chicago from January 1, 2010 to the present. Inspections are performed by staff from the Chicago Department of Public Health’s Food Protection Program. Inspections are done using a standardized procedure. The results of the inspection are inputted into a database, then reviewed and approved by a State of Illinois Licensed Environmental Health Practitioner (LEHP). 

# This is the report for the EDA of the inspections 


Below, a detailed analysis of the graphs obtained through the notebook, as well as the Exploratory Data Analysis (EDA) conducted on the dataset, will be presented.

## EDA Analysis: Exploratory Data Analysis (EDA)


In this analysis, we will examine in detail the graphs generated from the notebook and the exploratory data analysis carried out on the dataset.

* #### The number of inspections per year is reflected in the following figure, showing that the year with the highest number of inspections was 2016 with a gradual decrease until 2023; however, it should be noted that from 2010 to 2016 the number of inspections performed on establishments increased linearly with a low slope.

![Cantidad de inspecciones por cada año](Step3-%20S3_AWS_Exploratory_analysis_EDA/Figures/Fig1.png)

* #### Analysis of Sanitary Inspections: Restaurants and Grocery Stores

A significant aspect of interest in sanitary inspections analysis is the distribution of these assessments among different types of establishments. According to our data, restaurants represent the type of establishment with the highest number of inspections conducted. This is not surprising, given the significant role restaurants play in public food safety. Given the complexity and the plethora of policies and regulations implemented in these establishments, it is understandable that they receive special attention in terms of inspections and audits.

However, it is noteworthy that the second type of establishment with the most inspections are grocery stores. This finding is significant as it underscores the importance of rigorous sanitary control in these establishments. Food stores, like restaurants, are susceptible to risks related to food safety and disease spread if they are not subjected to regular audits and assessments.

In summary, the analysis and the following figure reveal that both restaurants and grocery stores are subject to a considerable number of sanitary inspections. These findings highlight the need to maintain high standards of food safety across a wide range of establishments, in order to protect public health and prevent the spread of diseases.

![Tipos de establecimientos con más inspecciones](Step3-%20S3_AWS_Exploratory_analysis_EDA/Figures/Fig2.png)

* #### Frequency of inspections
The most frequent inspections are related to "canvass" and "license" processes. This trend arises from the fact that a wide range of establishments, including restaurants, grocery stores, bakeries, and children's services facilities, require optimal and up-to-date licenses to operate legally and safely. These licenses are crucial due to the multitude of policies and regulations aimed at reducing various types of offenses and promoting safety within these spaces.

The "canvass" process is also subject to frequent inspections as it is essential to meet the specific requirements set for these types of establishments. These assessments are crucial to ensuring full compliance with regulations related to "canvass" and thus maintaining integrity and safety in the mentioned places.

The high frequency of inspections related to "canvass" and "license" (see next figure) reflects the critical importance of maintaining adequate standards of licensing and regulatory compliance in a variety of establishments. This not only helps prevent offenses and ensure safety but also promotes public confidence and overall well-being in these commercial and service environments.

![5 inspecciones que más se realizan](Step3-%20S3_AWS_Exploratory_analysis_EDA/Figures/Fig3.png)

* #### Percentage of Inspections for the Most Common Inspection Types
The analysis of the percentage of inspections for the most common types reveals significant insights. As shown in the attached figure, it is noteworthy that "canvass" accounts for over 50% of all inspections conducted. Following closely behind is "license," representing approximately 12% of the total inspections. It is important to highlight that among the top five most frequent inspections, "License Re-Inspection" has the lowest percentage. These findings bolster the previously presented arguments regarding the critical importance of maintaining high standards of licensing and regulatory compliance across a variety of establishments.

![Porcentaje top 5 de inspecciones](Step3-%20S3_AWS_Exploratory_analysis_EDA/Figures/Fig4.png)

* #### Percentage of Establishments by Inspection Outcome

The outcomes of the inspections are depicted in the following figure. It's noteworthy how the majority (>50%) of establishments passed the audits, while just under 20% failed. This failure rate could be attributed to policy changes or non-compliance with laws within the establishments. Additionally, a smaller percentage, around 15%, received a conditional pass, indicating they failed to meet some requirements, albeit not of severe gravity. Importantly, there were no establishments deemed "not located," indicating that all audits were conducted as planned. These findings shed light on the overall compliance landscape and underscore the importance of ongoing regulatory adherence and enforcement within establishments.

![Porcentaje establecimientos por tipo de resultado](Step3-%20S3_AWS_Exploratory_analysis_EDA/Figures/Fig5.png)


## Next Steps

+ Improving Inspection Outcomes and Exploring Inspection Trends

+ The prevalence of inspection failures in establishments warrants a closer examination to pinpoint the underlying causes. It's imperative to scrutinize whether these failures stem from systemic issues, regulatory oversights, or lapses in compliance protocols.

+ Implementing diverse analytical approaches can shed light on the recent reduction in inspection frequency. Exploring potential factors such as changes in regulatory frameworks, shifts in enforcement priorities, or improvements in compliance practices could offer valuable insights into this trend.

+ The relatively low number of inspections conducted in bakeries necessitates further investigation. Delving into potential reasons, such as exemptions based on size or production volume, variations in risk assessments, or resource allocation discrepancies, could provide a comprehensive understanding of this phenomenon.

+ To enhance inspection efficiency and effectiveness, developing a machine learning model for predicting inspection outcomes is paramount. Leveraging historical audit data, along with pertinent establishment-specific attributes such as compliance history, location, and establishment type, can empower predictive analytics to forecast whether an establishment will pass, pass with conditions, or fail an audit. Such a model can serve as a proactive tool for regulatory agencies and establishments alike, facilitating targeted interventions and resource allocation strategies.

+ Moreover, conducting cross-validation with different machine learning algorithms is essential to identify the most robust model for such predictions. By rigorously assessing the performance of various algorithms across diverse datasets, stakeholders can ascertain the model's reliability and suitability for real-world applications, thereby enhancing decision-making processes and regulatory efficacy.





