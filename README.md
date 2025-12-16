# The Unrivaled Basketball League 2026 Season Ranking Predictions

# Project Overview
This project aims to predict the ranking of the eight teams in the Unrivaled Basketball League for the upcoming 2026 season.

# Team Members
Mengxiang Xiao & Zike Zeng

# Creating a virtual environemnt
python3 -m venv venv
source venv/bin/activate

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
1) To identify the key metrics for generating the player scoring model, raw data is cleaned and prepared using the following notebook:
  jupyter notebook src/clean_key_metrics.ipynb
2) To filter the key metrics, raw data of the player-level statistics for all players who appeared in the 2025 WNBA regular season is cleaned and processed using the following notebook:
  jupyter notebook src/clean_wnba.ipynb

# Data Analysis
1) To calculate the weight of each key metrics and generate the custom weighted scoring model, the following notebook is used:
  jupyter notebook src/run_analysis_weight.ipynb
2) Player performance scores are calculated using the following notebook:
  jupyter notebook src/run_analysis_wnba_2025_player_scores.ipynb
3) Each team's score (averaged) and the final ranking are calculated using the following notebook:
  jupyter notebook src/run_analysis_team_score.ipynb

# Data Visualization
1) Performance differences by each metric are visualized using:
  jupyter notebook jupyter notebook src/visualize_performance_difference_by_each_metric.ipynb
2) The weight of each key metric is visualized using:
   jupyter notebook jupyter notebook src/src/visualize_weight_of_each_key_metric.ipynb
3) Final team scores results are visualized using:
  jupyter notebook jupyter notebook src/visualize_team_results.ipynb
