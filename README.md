# Covid-19

Step 1: Download jenkins (via docker is the easiest way)  
Step 2: Create a pipeline that will connect to this repo.  
Step 3: Build for the first time without param's.  
Step 4: At the second time, you will see a new button in the job called 'Build with parameters' - it will open up 3 parametrs you could pass to the build for testing.  

You will see in the pipeline 6 stages:  
a. Declarative Checkout SCM  
b. Build - for install requirements.  
c. deathPeak - Returns the date (and value) of the highest peak of death Covid-19 cases in the last 30 days for a required country.  
d. newCasesPeak - Returns the date (and value) of the highest peak of new Covid-19 cases in the last 30 days for a required country.  
e. recoveredPeak - Returns the date (and value) of the highest peak of recovered Covid-19 cases in the last 30 days for the required country.  
f. Status - Returns a value of success / fail to contact the backend API

