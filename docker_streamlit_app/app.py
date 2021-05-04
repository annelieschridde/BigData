import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns 


st.title('Interactive Bubble Chart')
st.sidebar.markdown("## Controls")
st.sidebar.markdown("Add year:")
slider = st.sidebar.slider('Year', min_value = 1800, max_value=2100, step = 1)

@st.cache
def load_data():
    data = pd.read_csv(r"tidy_data.csv")
    #data = pd.read_csv(r"C:\Users\Annelie Schridde\Documents\Uni - HWR\2. Semester HWR\Big Data\Hausaufgaben\Streamlit Data\docker\tidy_data.csv")
    return data

df = load_data()


st.sidebar.markdown("Add countries:")
countries = st.sidebar.multiselect(
    "Select Countries",
    df['country'].unique()
)



### Plotting countries ###

max_gni = df['GNI'].apply(lambda x: math.log(x)).max()
subset_df = df.loc[lambda d: d['country'].isin(countries)]

fig, ax = plt.subplots()
for name in countries:
    plotset = subset_df.loc[lambda d: d['year'] == slider].loc[lambda d: d['country'] == name]
    ax.scatter(plotset['GNI'].apply(lambda x: math.log(x)),
    plotset['life_expectancy'],
    s = plotset['population']*0.001,
    label=name,
    alpha = 0.3)
plt.xlim([0,max_gni])
plt.ylim([0,100])
plt.legend(loc="lower left", markerscale=0.1, handlelength = 1, title = "Country")
plt.xlabel("Logarithmic GNI")
plt.ylabel("Life Expectancy")
plt.title("")
st.pyplot(fig)

