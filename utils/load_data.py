import pandas as pd 
import numpy as np 

def load_data(state: str, start_year, end_year):
    state = state.lower()
    df = pd.read_csv(filepath_or_buffer=f'data_clean/{state}.csv')
    
    df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
    df['opioid_overdose_deaths'] = df['opioid_overdose_deaths'].astype("int64")
    df['Year'] = df['Year'].astype(str)
    df['all_drug_overdose_deaths'] = df['all_drug_overdose_deaths'].astype("int64")
    df['Population'] = pd.to_numeric(df['Population'].str.replace(',', ''), errors='coerce')
    df['Year'] = pd.to_numeric(df['Year'].str.replace(',', ''), errors='coerce')
    # opioid related death 
    df['opioid_death_proportion'] = df['opioid_overdose_deaths'] / df['all_drug_overdose_deaths']
    df['opioid_death_per_100K'] = (df['opioid_overdose_deaths'] / df['Population']) * 100000
    return df 

