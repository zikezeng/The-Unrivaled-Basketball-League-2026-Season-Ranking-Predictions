# The Unrivaled Basketball League 2026 Season Ranking Predictions

# Project Overview
This project aims to predict the ranking of the eight teams in the Unrivaled Basketball League for the upcoming 2026 season.

# Team Memebers
Mengxiang Xiao & Zike Zeng

# Creating a virtual environemnt
python -m venv venv
venv\Scripts\activate

# Installing the required libraries
pip install -r requirements.txt

# Data collection
1) The following notebooks is used to collect the raw data of the Unrivaled League team statistics for 2025 season:
  jupyter notebook src/get_Unrivaled_2025_team_data.ipynb
2) The following notebooks is used to collect the raw data of the player-level statistics for all players who appeared in the 2025 WNBA regular season:
  jupyter notebook src/get_wnba_data_per_game.ipynb
3) The following notebooks is used to collect the raw data of the Unrivaled League 2026 season club rosters:
  jupyter notebook src/get_team_members.ipynb

# Data Cleaning 
1) To identify the key meterics for generating the player scoring model, raw data are cleaned and prepared using the following notebook:
  jupyter notebook src/Data Cleaning-Identify Key Metrics.ipynb
2) To filtered the key metrics, raw data of the player-level statistics for all players who appeared in the 2025 WNBA regular season are cleaned and processed using the follwing notebook:
  jupyter notebook src/clean_wnba.ipynb

# Data Analysis
1) To calculate the weights of each key metrics and generate the custom weighted scoring model, the following notebook is used:
  jupyter notebook src/caculate weight & weight formula.ipynb
2) Player performance scores are calculated using the following notebook:
  jupyter notebook src/run_analysis_wnba_2025_player_scores.ipynb
3) Each team's score (averaged) and the fonal ranking are calculated using the follwing notebook:
  jupyter notebook src/run_analysis_team_score.ipynb

# Data Visualization
Final team scores results are visualized using:
jupyter notebook visualize_team_results.ipynb
