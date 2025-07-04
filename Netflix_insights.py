import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('netflix_titles.csv.zip')
df=pd.DataFrame(data)


plt, ax= plt.subplots(3,2, figsize=(18,20))
plt.suptitle("Netflix Data Analysis", fontsize=20, fontweight='bold')

country=df['country'].value_counts().sort_values(ascending=False).head(10)
sns.barplot(country, orient='h',ax=ax[0][0])
ax[0][0].set_xlabel('Production')
ax[0][0].set_title('Top Contribution of Countries', fontsize=18, fontweight='bold', fontfamily='Arial')


type=df['type'].value_counts().sort_values(ascending=False)
ax[0][1].pie(type,labels=type.index,autopct='%1.1f%%',colors = ['#4c72b0', '#d3d3d3'],startangle=90)
ax[0][1].set_title('Content types ', fontsize=18, fontweight='bold', fontfamily='Arial')


year = df['release_year'].value_counts().sort_index().tail(15)
sns.lineplot(year, marker='o',ax=ax[1][0],palette='crest')
ax[1][0].grid(color='grey',linestyle=':')
ax[1][0].set_xlabel('Year')
ax[1][0].set_ylabel('Number of publishes')
ax[1][0].set_title('Trend of publishing content (from 2006 to 2021)', fontsize=18, fontweight='bold', fontfamily='Arial')


description=df['listed_in'].astype(str).str.split(',').str[0]
description=description.value_counts().head(5)
ax[1][1].pie(description, labels=description.index,autopct='%1.1f%%',startangle=90,colors = ['#dadaeb', '#bcbddc', '#9e9ac8', '#756bb1', '#54278f'])
ax[1][1].set_title('Top 5 Description(Tag)', fontsize=18, fontweight='bold', fontfamily='Arial')


directors=df['director'].value_counts().sort_values(ascending=False).head(10)
colors = ['#23004d', '#360080', '#4b00b5', '#6200ea', '#7a29ff',
          '#914dff', '#a974ff', '#c299ff', '#dabfff', '#f2e5ff']
sns.barplot(directors,orient='h',ax=ax[2][0], palette=colors)
ax[2][0].set_xlabel('Number of Directed movie and series')
ax[2][0].set_ylabel('Top Directors')
ax[2][0].set_title('Top 10 Netflix Directors', fontsize=18, fontweight='bold', fontfamily='Arial')


rating=df['rating'].value_counts().sort_values(ascending=False).head(5)
ax[2][1].pie(rating, labels=rating.index, autopct='%1.1f%%',startangle=90,colors = ['#ccd9ff', '#b3c6ff', '#99b3ff', '#809fff', '#668cff'])
ax[2][1].set_title('Top 5 rating', fontsize=18, fontweight='bold', fontfamily='Arial')

sns.despine()
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('Figure.png',dpi=350,bbox_inches='tight')
plt.show()
