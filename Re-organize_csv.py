#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[7]:


# We isolate columns that are index-level columns

Nodes = ['cycle.@id', 'impactAssessment.@id',
 'site.@id', 'cycle.site.@id',
 'impactAssessment.cycle.@id', 'site.defaultSource.@id', 'source.bibliography.name']


# we write three functions to take an id, remove the '-' values and return a non-empty dataframe
def return_dataframes(id):
    id_df = input[id]
    return id_df

def prune_df(df):
    clean_df = df.replace('-', np.nan)
    return clean_df

def remove_nan(df):
    df.dropna(inplace=True)
    return df

def process_csv(idA):
    df_ = return_dataframes(idA)
    id_df_prune = prune_df(df_)
    idA = remove_nan(id_df_prune)
    return idA

def merge_dataframes(idA, idB):
    df_id = process_csv(idA)
    id_dfB = process_csv(idB)
    idA_idB_df = pd.merge(df_id, id_dfB, left_on=df_id[0], right_on=id_dfB[0], how='outer') # Merge cyclesiteid and siteid dataframes
    return idA_idB_df

def reorganize_csv(file):
    input = pd.read_csv(file)
    # Then we sort column categories based on how disjointed they were, starting from the first column through the last column preceding the next '-' value on the ro
    cycleid = input.columns[0:5]
    impactAssessmentid = input.columns[5:11]

    siteid = input.columns[11:14]

    sourceid = input.columns[14:16]
    cyclesiteid = input.columns[16:52]
    impactAssessmentcycleid = input.columns[52:58]
    sitedefaultsourceid = input.columns[58:73]
    bibliography = input.columns[73:76]
    
    cycle_site_df = merge_dataframes(cycleid, siteid)
    impact_cycle_df = merge_dataframes(impactAssessmentcycleid, cycleid)
    
    # We create copies of these two dataframes and give them unions since they don't have common joining points
    dff3 = impactAssessmentid_df.copy()
    dff4 = sitedefaultsourceid_df.copy()
    cycle_site_df['id'] = ['1','2','3']
    impact_cycle_df['id'] = ['1','2','3']
    dff3['id'] = ['1','2','3']
    dff4['id'] = ['1','2','3']
    
    # We merge the remaining dataframes
    impact_sitedefault_df = dff3.merge(dff4, on='id', how='inner')
    impact_sitedefault_df.drop(columns = 'id')
    dff6 = impact_sitedefault_df.copy()
    impact_source_df = pd.merge(dff6, sourceid_df, left_on='site.defaultSource.@id', right_on='source.@id', how='outer')
    impact_bib_df = pd.merge(impact_source_df, bibliography_df, left_on='source.name', right_on='source.bibliography.name', how='outer')
    impact_bib_df['id'] = ['1','2','3']
    
    join_cycle_site_impact_dfs = cycle_site_df.merge(impact_cycle_df, on='id', how='inner')
    join_all = join_cycle_site_impact_dfs.merge(impact_bib_df, on='id', how='inner')
    join_all.drop(columns='id', inplace=True)
    final_dataframe = join_all[output.columns]
    
    return final_dataframe


# In[8]:





# In[ ]:




