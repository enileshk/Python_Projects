import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math


#path=r"C:\Users\inile\PyCharmMiscProject\medical_examination.csv.txt"
path=r"medical_examination.csv"

# 1
df = pd.read_csv(path)
# 2
df['overweight'] = ((df.weight/(df.height/100)**2) > 25).astype(int)
# 3

df.cholesterol = np.where(df.cholesterol<=1,0,1)
df.gluc = np.where(df.gluc<=1,0,1)
# 4
def draw_cat_plot():
    # 5
    columns_to_plot = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']
    df_cat = df[columns_to_plot]
    # 6
    df_cat = df_cat.melt(id_vars='cardio',
                            value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio'],
                            var_name='variable', value_name='value')
    # 8
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
    sns.countplot(data=df_cat[df_cat['cardio'] == 0],
                  x='variable', hue='value', ax=axes[0],legend=False)
    axes[0].set_title('Cardio = 0')
    axes[0].set_ylabel('total')
    axes[0].set_xlabel('variable')

    # cardio = 1
    sns.countplot(data=df_cat[df_cat['cardio'] == 1],
                  x='variable', hue='value', ax=axes[1])
    axes[1].set_title('Cardio = 1')
    axes[1].set_xlabel('variable')
    legend = axes[1].legend(loc='center right')
    #plt.tight_layout()
    # 9
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # 11

    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    h1=df_heat['height'].quantile(0.025)
    h2=df_heat['height'].quantile(0.975)
    w1=df_heat['weight'].quantile(0.025)
    w2=df_heat['weight'].quantile(0.975)

    df_heat = df_heat[df_heat['height'] >= h1]
    df_heat = df_heat[df_heat['height'] <= h2]
    df_heat = df_heat[df_heat['weight'] >= w1]
    df_heat = df_heat[df_heat['weight'] <= w2]
    # 12
    corr_tmp = df_heat.corr()
    #The test suite has some issue - the heatmap values are not matching due to rounding. The CORR matrix value between ap_lo and Cholesterol is not matching. 
    corr=np.round(corr_tmp,1)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, axes = plt.subplots(figsize=(12, 10))
    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='Reds', square=True, linewidths=0.5, ax=axes)

    axes.set_title("Correlation Matrix (Lower Triangle)", fontsize=16)
    plt.tight_layout()
    # 16
    fig.savefig('heatmap.png')
    return fig



