import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("beer_reviews.csv")

# get top 5 beers
beershead = df.groupby(['beer_name']).size().rename('Counts').reset_index().sort_values(['Counts'], ascending=False)
top5beers = []
top5beers2 = []
for i in beershead.head()['beer_name']:
    top5beers.append(i)

for i in top5beers:
    beers2 = df.loc[(df['beer_name'] == i)]
    beer_review = beers2.groupby('review_palate').size().rename('Counts').reset_index()
    i = 0;
    total = 0;
    for w in beer_review['review_palate']:
        total = beer_review['Counts'][i]*w + total
        i+=1
    top5beers2.append(total / beer_review['Counts'].sum())
 

    
print(top5beers)  
print(top5beers2)
    

x = np.array(top5beers)
y = np.array(top5beers2)

plt.bar(x,y)
plt.show()
