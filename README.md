# SalaryPrediction
## Goal: To predict Salary based on different job qualifications/ employee metadata from the HR department.
### Useful for **both** parties in the hiring process:
- *Employees*: Useful for job hunters and candidates to negotiate their proper salary based on qualifications like: years of Experience and Industry worked in.
- *Employers*: Informative for companies hiring to make sure they're paying future employees the appropriate amount; furthermore, helps reduce costs while hiring the most qualified.

### 1 Main Notebooks:
  1. Salary_Prediction.ipynb( contains EDA , Baseline model, select the best model)
  2. model.ipynb (contains final model for project) 


### The Languages and Technologies used in this project are:
- Visualization: Seaborn, Matplotlib
- Data Manipulation: Pandas, Numpy
- Machine Learning - models included are:
  - Scikit-Learn
    - Linear Regression
    - Random Forest Regressor
    - Gradient Boosting Regressor
  
  
## Outline the 4D Process:
  1. **Define** the Problem
    
      - **Problem**: Employees and Employers often have a hard time determining the optimal salary for individuals based on their qualifications. 
      - **Goal**: Studying this HR dataset and creating a Regression algorithm to predict salaries based on these features.
  2. **Discover** Inights and Trends
    
      - Understand the Numerical and Categorical data:
        1. **Numerical**
            - **Salary**: Target Feature & pay of each employee
            - **yearsExperience**: Amount of experience the employee has
            - **milesFromMetropolis**: Distance from metropolis of the employee
        2. **Categorical**
            - **CompanyId**: Id of the company the employee works for
            - **jobType**: Level on the Corporate ladder
            - **degree**: Level of education
            - **major**: Type of major
            - **industry**: Industry the employee works in
      - Identify outliers, missing, and duplicate data
        - **Remove Salaries of 0** for individuals with high qualifications since it also offers low predictive signal
      - Locate trends and correlations for features vs. salary:
        - *Salary increases* as:
          - **jobType** on the Corporate ladder gets better
          - **degree** of education is more advanced
        - *Salary increases* for individuals that:
          - Are Math, Business, or Engineering **majors**
          - Are working in Finance, Oil, or Web **industries**
          - Have more **YearsExperience**
        - *Salary decreases* as **milesFromMetropolis** increases -- *negatively correlated*
      - Understand Distributions of each of the features:
        - Salary has a Gaussian or *Normal* Distribution
        - All other features ahve a *Uniform* Distribution
      - Create and Pickle: Train, Validation, and Test data
  3. **Develop** Feature Engineering , create the model , select the best model
    
      
        - Random Forest Regressor: 389.68
        - Linear Regression: 921.97
        - Gradient Boosting Regressor: 359.23
     
      - ***Summary:*** The **Gradient Boosting Regressors** - performed **best** when **max_depth=6** and **n_estimators=160**
  
     
  4. **Deploy** Solutions
      - The optimal model will be the **Gradient Boosting Regressors** as it provides the **lowest MSE**

