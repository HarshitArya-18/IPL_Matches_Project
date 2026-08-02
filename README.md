# IPL Matches Analysis

A match-level data analysis project on IPL (Indian Premier League) cricket matches, built as part of a Data Analyst portfolio.

## Overview
This project analyzes 592 synthetic IPL matches spanning the 2018–2025 seasons across 10 teams. It covers team performance, toss impact, venues, win margins, and Player of the Match awards — demonstrating an end-to-end analyst workflow from database design to visualization.

## Tools Used
- **MySQL** — schema design and SQL analysis queries
- **Python** — scripting and data generation
- **Pandas** — data loading, cleaning, grouping, aggregation
- **NumPy** — numerical/statistical calculations
- **Matplotlib** — data visualization

## Project Structure
```
ipl_matches_project/
├── data/
│   └── ipl_matches.csv          # Match-level dataset (592 rows, 13 columns)
├── sql/
│   └── ipl_matches.sql          # Table schema + 8 analysis queries
├── charts/
│   ├── 01_wins_per_team.png
│   ├── 02_win_percentage.png
│   ├── 03_matches_per_season.png
│   ├── 04_toss_decision.png
│   ├── 05_toss_impact.png
│   ├── 06_win_margins.png
│   ├── 07_matches_per_city.png
│   └── 08_top_player_of_match.png
├── generate_data.py             # Synthetic dataset generator
├── analysis.py                  # Main analysis + chart generation script
└── README.md
```

## Dataset Columns
| Column | Description |
|---|---|
| match_id | Unique match identifier |
| season | IPL season year |
| match_date | Date of the match |
| team1 / team2 | Competing teams |
| venue / city | Match location |
| toss_winner | Team that won the toss |
| toss_decision | "bat" or "field" |
| winner | Match winner |
| win_by_runs / win_by_wickets | Victory margin |
| player_of_match | Award winner |

## Key Insights
- **Most successful team**: Rajasthan Royals led with 78 total wins and the highest win percentage (56.52%) across the dataset.
- **Toss decision**: Teams chose to field first far more often than to bat first after winning the toss.
- **Win margins**: Matches won by runs averaged ~47.5 runs; matches won by wickets averaged ~5 wickets — both consistent with typical T20 chase patterns.
- **Season trends**: No single team dominated every season — champions varied year to year (e.g., Rajasthan Royals in 2018/2021/2022, Gujarat Titans in 2020/2023, Chennai Super Kings in 2025).
- **Venue distribution**: Matches were spread fairly evenly across each team's home venue, with a mild bias toward more frequently used stadiums.

## How to Run
1. Load `data/ipl_matches.csv` into MySQL using the schema in `sql/ipl_matches.sql` (or query the CSV directly with Pandas).
2. Run the analysis script:
   ```bash
   pip install pandas numpy matplotlib
   python analysis.py
   ```
3. Generated charts will appear in the `charts/` folder, and summary statistics will print to the console.

## Note on Data
This dataset is **synthetically generated** (see `generate_data.py`) to resemble real IPL match data for portfolio and learning purposes. Team names, venues, and player names are real, but exact match outcomes are simulated and do not reflect actual historical results.

## Author
Built by a BCA student (CCSU, Meerut) as part of a Data Analyst fresher portfolio project.
