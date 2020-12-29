# Covid-19

Step 1: Download jenkins (via docker is the easiest way)  
Step 2: Create a pipeline that will connect to this repo / clone this repo, and push it to your repo. This way you can connetק with jenkins to your private repo.
Step 3: Build for the first time.  
Step 4: You will see a new button in the job called 'Build with parameters' - it will open you 3 parametrs you could define - each will give you info accordingly this description.  

You will see in the pipeline 6 stages:  
a. Declarative Checkout SCM  
b. Build - this will connect to the repo and clone the files  
c. deathPeak - Returns the date (and value) of the highest peak of death Covid-19 cases in the last 30 days for a required country.  
d. newCasesPeak - Returns the date (and value) of the highest peak of new Covid-19 cases in the last 30 days for a required country.  
e. recoveredPeak - Returns the date (and value) of the highest peak of recovered Covid-19 cases in the last 30 days for the required country. 
f. Status - Returns a value of success / fail to contact the backend API  
