# Election_Analysis

## Project Overview
A Colorado Borad of Elections employee has given you the following tasks to complete the elction audit of a recent local congressional election.

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 total votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana Degette, who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
The Colorado Board of Elections requested some additional data in regard to the election audit done previously for information on voter turnout in participating counties.

1.  The voter turnout for each county
2.  The percentage of votes from each county out of the total count
3.  The county with the highest turnout

## Election-Audit Results
The analysis of the election results show that:
- A total of 369,711 votes were case in the election
  -  ![Total_votes](https://user-images.githubusercontent.com/88444529/133843404-aeae865a-cb1e-44b1-a427-3aad658f2a6d.PNG)
  - Jefferson county contributed 10.5% of the vote and 38,855 number of votes.
  - Denver county contributed 82.8% of the vote and 306,055 number of votes.
  - Araphoe county contributed 6.7% of the vote and 24,801 number of votes.
    - ![Candidate_County_Options](https://user-images.githubusercontent.com/88444529/133844171-d864e24c-34c6-44a3-89be-7b1721521e28.PNG)
    - ![Retrieving_County_Name](https://user-images.githubusercontent.com/88444529/133844229-3edac714-9933-4ab7-80d5-6ab6ca7f779b.PNG)
    - ![County_Vote_Count](https://user-images.githubusercontent.com/88444529/133844214-d3c1485b-6023-46be-861d-20c3a5fc7cd7.PNG)
    - ![County_Calculations](https://user-images.githubusercontent.com/88444529/133844200-ea56f193-4b86-45c2-ba55-2caab3982864.PNG)
- The county with the largest number of votes:
  - Denver county, who contributed 82.8% of the vote and 306,055 number of votes.
## Election-Audit Summary
The code that has been used to complete the analysis of this election can be used in subsequent elections with only slight modification necessary.  Depending on the data that is being gathered, a dictionary can be created that holds values and can be iterated through to get the relevant data like votes per county or votes per candidate.  This could be done to further analyze election data with other variables if available in the dataset.  It could be broken down further into geographical area of votes per zipcode.  This is a dynamic script and it could be in your best interest to adopt this script for all future elections.
