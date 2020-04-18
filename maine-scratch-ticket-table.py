
import pandas as pd

# create dataframe from first table at url
dfs = pd.read_html('http://mainelottery.com/players_info/unclaimed_prizes.html', header=0)
df = dfs[0]

# forward fill percent unsold values
df[['Percent Unsold']] = df[['Percent Unsold']].fillna(method='ffill')

# make other nan values blank
df = df.fillna('')

# define function to highlight rows for games where the percent unsold < 1.0
def highlight_lessthan(x):
    if x['Game Name'] == '':
        return ['background-color: white']*len(x)
    elif x['Percent Unsold'] < 1.0:
        return ['background-color: yellow']*len(x)
    else:
        return ['background-color: white']*len(x)
        
# render html from styled df:
html = (df.style.apply(highlight_lessthan, axis=1).render())

#save html as index.html file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close() 