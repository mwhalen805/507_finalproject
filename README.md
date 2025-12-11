# SI 507 Final Project
## 2024 Trade Data Interface

This project allows users to interact with trade data from 2024. The base is a python program that reads json data from [comtrade](https://comtradeplus.un.org) and constructs a graph with countries as nodes and trade relationships as edges. The comtrade data can be accessed in this [Google Drive folder](https://drive.google.com/drive/folders/1cGpCeNdZDeHQLQaLpxNOuKgubnINmEJ0?usp=sharing), as it could not be uploaded to the repo due to its size. This data was originally downloaded from [comtrade](https://comtradeplus.un.org)'s premium institutional api, as U-M has a license. I also downloaded a countries csv from the site to map countries to their 3 digit codes in order to be able to display country names to the user. This file was converted to a json and can be found in flask_backend/country_name_to_code.json. 

Comtrade data summary: This is a very large file containing data on all trades conducted between countries in the year 2024. For this project I used "reporterCode" (the country reporting the trade) and "partnerCode" (the country being traded with) fields to find the countries with a trade relationship. In a next phase of the project, I would also like to use "cmdCode" (commodity code) to see what goods are being traded. 

Country data summary: This is a file containing country names mapped to codes. Since the Comtrade data only has codes for countries, I used this information to display country names to the user so as to be more readable. 

Users can interact with the base program by running trade_graph.py and responding to prompts in the terminal. Options include:
- Find the trade partners of a given country
- Find the shortest trade route between two countries
- Show the top countries by number of trade partners
- View the total number of trade clusters
- Find the bottleneck countries

Note that trade_graph.py is quite slow due to the large volume of data it must pull, so it may take 30 seconds to a minute to load. 

I also developed a web app to display this information in a more visual way. I used Flask for the back end and React for the front end. To access the web app:
1. Open a terminal, cd into the flask_backend folder, and run "python app.py"
2. Open a second terminal, cd into the react_frontend folder, and run "npm run dev"
3. Paste the web address from the react_frontend terminal into a browswer

Note that app.py is quite slow due the large volume of data trade_graph.py must pull, so it may take 30 seconds to a minute to load. Wait until it is loaded before accessing the web app.

The web app is still in development at this time, so the only feature currently allows users to select a country (highlighted in blue) and show its trade partners (highlighted in green), as well as displaying a list of the top countries by number of trade partners on the left side of the page. 

In the future, I hope to group countries into clusters based on their GDP per capita, global militarization index, and global diplomacy index, then have check boxes to show different tiers on the map for each category. I may also add a feature to show the goods being traded between countries. 

