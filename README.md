# Analyze Best Selling Amazon Books

Analysis of the Amazon Top 50 bestselling books (2009-2019) with Python and pandas.

## Tools
Python, pandas, matplotlib

## What I did
- Imported the data from a CSV file (550 rows)
- Cleaned the data (duplicates and missing values)
- Analyzed authors, genres, prices, ratings and reviews
- Created 4 charts

## Key findings
- Jeff Kinney has the most bestsellers (12), followed by Rick Riordan (10).
- Fiction and Non Fiction have almost the same average rating (4.62 vs 4.60), but Fiction books get far more reviews on average.
- The average price dropped from about $15 in 2009 to about $10 in 2019.
- Price, rating and number of reviews are almost unrelated (correlation close to 0).

## How to run
pip install pandas matplotlib
python main.py
