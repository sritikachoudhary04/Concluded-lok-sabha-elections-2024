# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:39:58 2024

@author: vruti
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  Results of Lok Sabha Elections                   ") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Find tables with election results
tables = soup.find_all('table')

#Extract headers
headers = soup.find_all('th')[0:4]
headers = [ele.text.strip() for ele in headers]


# Extract data into a DataFrame
data = []
for table in tables:
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
df = pd.DataFrame(data, columns=headers)
df.to_csv('E:\projects\kalvium task\lok_sabha_results.csv', index=False)

df = pd.read_csv('E:\projects\kalvium task\lok_sabha_results.csv')
df.dropna(inplace=True)
df.columns = df.columns.str.strip()

# Plot pie chart of party-wise vote share
plt.figure(figsize=(10, 8))
plt.pie(df['Won'], startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Party-wise Vote Share')
plt.show()


# Define a color palette
colors = plt.cm.tab20.colors
# Plot pie chart of party-wise vote share
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(df['Won'], autopct='%1.1f%%', startangle=140, colors=colors)

# Add a legend with party names and corresponding colors
plt.legend(wedges, df['Party'], title="Parties", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Party-wise Vote Share')
plt.savefig('party_wise_vote_share.png')
plt.show()




while True:
    print()
    print("10 Key Insights:-")
    print()
    print("1.Total Seats")
    print("2.Winning Party")
    print("3.Top 5 Parties by Seats Won")
    print("4.Total Seats Won")
    print("5.Total Seats Leading")
    print("6.Party with Most Leading Seats")
    print("7.Top 5 Parties by Leading Seats")
    print("8.Winning Party Percentage of Total Seats")
    print("9.Number of Parties with At Least One Seat")
    print("10.Total Number of Parties Participated")
    print("Enter 0 for exit")

    choice=int(input("Enter your choice: "))
    
    if choice == 1:
        total_seats = df['Total'].astype(int).sum()
        print(total_seats)
        
    elif choice == 2:
        winning_party = df.loc[df['Won'].astype(int).idxmax()]['Party']
        print(winning_party)
        
    elif choice == 3:
        top_5_parties = df[['Party', 'Won']].sort_values(by='Won', ascending=False).head(5)
        print(top_5_parties)
        
    elif choice == 4:
        total_won_seats = df['Won'].astype(int).sum()
        print(total_won_seats)
        
    elif choice == 5:
        total_leading_seats = df['Leading'].astype(int).sum()
        print(total_leading_seats)
        
    elif choice == 6:
        leading_party = df.loc[df['Leading'].astype(int).idxmax()]['Party']
        print(leading_party)
        
    elif choice == 7:
        top_5_leading_parties = df[['Party', 'Leading']].sort_values(by='Leading', ascending=False).head(5)
        print(top_5_leading_parties)
        
    elif choice == 8:
        winning_party_seats = df[df['Party'] == winning_party]['Won'].astype(int).sum()
        winning_party_percentage = (winning_party_seats / total_seats) * 100
        print(winning_party_percentage)
        
    elif choice == 9:
        parties_with_seats = df[df['Won'].astype(int) > 0]['Party'].nunique()
        print(parties_with_seats)
        
    elif choice == 10:
        total_parties = df['Party'].nunique()
        print(total_parties)
        
    elif choice==0:
        print()
        print()
        print("***************THANK YOU***************")
        break

    else:
        print("ENTER A VALID NUMBER!!!")
        print()
        print()
        print()


