## Inspiration
Looking at people getting rich with stocks, we too wanted to get rich with stocks. But we had no clue how to do that! So, we decided to build a program that can help us figure out which stocks will have the best return in the future!

## What it does
This project takes the past 10 years of a stock and analyzes it to make predictions about the future value of the stock.

## How we built it
We started off using python and the framework streamlit. We used the yahoo finance api to get the history of the stock inputted from the last 10 years. Using that, we then plot it using the plotly module and predict the next n (1-365) days of the stock depending on what the user chose using prophet.  We would also plot that using the plotting inside prophet and plotly. We then ran the calculations to figure out how much the price will change.                                                                                                                                                                                                                                                                                                                                                                                   
## Challenges we ran into
Our biggest challenge was making sure the input given by the user was valid. This was at first done using while loops but we realized that it was making our application extremely slow. We then combatted this using conditionals and try/except which made sure the input was valid and the program ran smoothly!

## Accomplishments that we're proud of
We were proud of how we were able to effectively use the frameworks and api's to allow this project to work. Coming into this hackathon, we had no previous experience with any api or framework, but that didn't stop up from finding the best stocks!

## What we learned
We learned to use the streamlit framework properly, which we ran into many troubles with to properly download and use. Also working with the yahoo finance api which looks at all of stocks value within the past decades and using prophet to predict stocks, which was originally made to predict the forecast.

## What's next for Stockfest
We plan on making Stockfest a proper website with a better front-end design that is user friendly and bug-free. We also plan to make the graphs easier to read and have more calculations that are given out to the user.

## Made by Rushabh Shah and Fayez Mohammed

## Video Link
https://youtu.be/YhEbFuNYiJ4

## Instructions
If you need help running this file, make sure to run with streamlit and prophet downloaded through the terminal (pip install streamlit/prophet) and also run the program in the terminal.
