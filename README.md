# The application :

This project is a flask app which allows to recommend 5 movies which are close to a chosen one.
The original datasets are in the "original_files" folder. A feature engineering has been by usig the data in their columns.
The recommendation is mostly based on the movies genders :
- A dimensionality reduction has been done with t-SNE


- After a satisfying embeding were found :
--> The 5 closest movies to each movies have been computed
--> The result of this computation were stored in json fields
--> The final files for the recommendation maps movies to their neighbors in a ".csv" file : "recommandation_system_light.csv" . Below is the structure of this file :
![alt text](https://github.com/E-tanok/Recommandation_movie_recommendation-system/blob/master/project_instructions/final_file_structure.png)

- Finally, a flask application reads the final file in order to make the recommendation.



## How to use it

### First steps

Here are the instructions which allows to launch the application :
![alt text](https://github.com/E-tanok/Recommandation_movie_recommendation-system/blob/master/project_instructions/first_steps.png)


### Once the application is launched

Select the movie of your choice in the html list and press "ENTER":
![alt text](https://github.com/E-tanok/Recommandation_movie_recommendation-system/blob/master/project_instructions/selecting_movie.png)


### The recommendation results

The application query the file (or the database) and shows you the 5 closest movies from your selection (Below is an example of the result with the "Independance Day" recommendation ):
![alt text](https://github.com/E-tanok/Recommandation_movie_recommendation-system/blob/master/project_instructions/results.png)
