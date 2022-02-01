#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pandas.testing as pd_testing


# In[ ]:


def test_return_dataframes(id):
    df = pd.DataFrame({"a": [True, True, False, False], "b": [None, None, False, False], "c": [None, False, True, None]})
    expected = df['a']
    result = return_dataframes['a']
    assert expected ==  result
    
    
def test_prune_df(df):
    df = pd.DataFrame({"a": ['-', None, None], "b": [None, None, False], "c": [None, False, True]})
    expected = pd.DataFrame({"a": [nan , None, None], "b": [None, None, False], "c": [None, False, True]})
    result = prune_df(df)
    pd_testing.assert_frame_equal(expected, result)

def test_remove_nan(df):
    df = pd.DataFrame({"a": ['-', None, None], "b": ['-', None, False], "c": ['-', False, True]})
    expected = pd.DataFrame({"a": [None, None], "b": [None, False], "c": [False, True]})
    result = remove_nan(df)
    pd_testing.assert_frame_equal(expected, result)

def test_process_csv(idA):
    df = pd.DataFrame({"a": ['-', None, None], "b": ['-', None, False], "c": ['-', False, True]})
    expected = pd.DataFrame({"a": [None, None], "b": [None, False], "c": [False, True]})
    result = process_csv(df)
    pd_testing.assert_frame_equal(expected, result)
    
    
def test_merge_dataframes(idA, idB):
    df_a = pd.DataFrame({"b@id": ["a"], "b": ["c"]})
    df_b = pd.DataFrame({"a@id": ["a"], "d": ["e"]})
    expected = pd.DataFrame({"b@id": ['a'], "b": ['c'], "d": [e]})
    result = merge_dataframes(df_a, df_b)
    
def test_reorganize_csv(file):
    expected = pd.read_csv('output.csv')
    result = reorganize_csv('input.csv')
    pd_testing.assert_frame_equal(expected, result)

