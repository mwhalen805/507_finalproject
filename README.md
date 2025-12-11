# SI 507 Final Project
## 2024 Trade Data Interface

This project allows users to interact with trade data from 2024. The base is a python program that reads json data from [comtrade](https://comtradeplus.un.org) and constructs a graph with countries as nodes and trade relationships as edges. The comtrade data can be accessed in this [Google folder](https://drive.google.com/drive/folders/1cGpCeNdZDeHQLQaLpxNOuKgubnINmEJ0?usp=sharing). Users can:
- Find the trade partners of a given country
- Find the shortest trade route between two countries
- Show the top countries by number of trade partners
- View the total number of trade clusters
- Find the bottleneck countries

I also developed a web app to display this information in a more visual way. I used Flask for the back end and React for the front end. The web app is still in development at this time, so the only feature currently allows users to select a country (highlighted in blue) and show its trade partners (highlighted in green), as well as displaying a list of the top countries by number of trade partners on the left side of the page. 

In the future, I hope to group countries into clusters based on their GDP per capita, global militarization index, and global diplomacy index, then have check boxes to show different tiers on the map for each category. 

