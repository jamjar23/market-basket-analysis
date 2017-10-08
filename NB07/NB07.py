# -*- coding: utf-8 -*-
# Created on Sat Oct  7 16:06:13 2017

#7.0.0 (ungraded)
import requests
import os
import hashlib
import io

def download(file, url_suffix=None, checksum=None):
    if url_suffix is None:
        url_suffix = file
        
    if not os.path.exists(file):
        if os.path.exists('.voc'):
            url = 'https://cse6040.gatech.edu/datasets/{}'.format(url_suffix)
        else:
            url = 'https://github.com/cse6040/labs-fa17/raw/master/datasets/{}'.format(url_suffix)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(file, 'w', encoding=r.encoding) as f:
            f.write(r.text)
            
    if checksum is not None:
        with io.open(file, 'r', encoding='utf-8', errors='replace') as f:
            body = f.read()
            body_checksum = hashlib.md5(body.encode('utf-8')).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(file, body_checksum, checksum)
    
    print("'{}' is ready!".format(file))
    
datasets = {'iris.csv': 'd1175c032e1042bec7f974c91e4a65ae',
            'table1.csv': '556ffe73363752488d6b41462f5ff3c9',
            'table2.csv': '16e04efbc7122e515f7a81a3361e6b87',
            'table3.csv': '531d13889f191d6c07c27c3c7ea035ff',
            'table4a.csv': '3c0bbecb40c6958df33a1f9aa5629a80',
            'table4b.csv': '8484bcdf07b50a7e0932099daa72a93d',
            'who.csv': '59fed6bbce66349bf00244b550a93544',
            'who2_soln.csv': 'f6d4875feea9d6fca82ae7f87f760f44',
            'who3_soln.csv': 'fba14f1e088d871e4407f5f737cfbc06'}

#for filename, checksum in datasets.items():
#    download(filename, url_suffix='tidy/{}'.format(filename), checksum=checksum)
#print("\n(All data appears to be ready.)")

# Some modules you'll need in this part
import pandas as pd
from io import StringIO
from IPython.display import display

# Ignore this line. It will be used later.
SAVE_APPLY = getattr(pd.DataFrame, 'apply')

irises = pd.read_csv('iris.csv')
#print("=== Iris data set: {} rows x {} columns. ===".format(irises.shape[0], irises.shape[1]))
#display (irises.head())
#print(irises.index)

#7.0.1 (ungraded)
#irises.describe()
#irises['sepal length'].head()
#irises[['sepal length', "petal width"]].head()
#irises.iloc[5:10]
#irises[irises["sepal length"] > 7.0]
#irises["sepal length"].max()
#irises['species'].unique()
#irises.sort_values(by="sepal length", ascending=False).head(13)
#irises.sort_values(by="sepal length", ascending=False).iloc[5:10]
#irises.sort_values(by="sepal length", ascending=False).loc[5:1]
## iloc works by sequence in sorted list, loc works on assinged index value
#irises['x'] = 3.14
#irises[['sepal length', "petal width"]].tail()
#irises.rename(columns={'species': 'type'})
#del irises['x']

A_csv = """country,year,cases
Afghanistan,1999,745
Brazil,1999,37737
China,1999,212258
Afghanistan,2000,2666
Brazil,2000,80488
China,2000,213766"""
with StringIO(A_csv) as fp:
    A = pd.read_csv(fp)
#print("\n=== A ===")
#display(A)

B_csv = """country,year,population
Afghanistan,1999,19987071
Brazil,1999,172006362
China,1999,1272915272
Afghanistan,2000,20595360
Brazil,2000,174504898
China,2000,1280428583"""
with StringIO(B_csv) as fp:
    B = pd.read_csv(fp)
#print("\n=== B ===")
#display(B)

C = A.merge(B, on=['country', 'year'])
#print("\n=== C = merge(A, B) ===")
#display(C)

with StringIO("""x,y,z
bug,1,d
rug,2,d
lug,3,d
mug,4,d""") as fp:
    D = pd.read_csv(fp)

with StringIO("""x,y,w
hug,-1,'e'
smug,-2,'e'
rug,-3,'e'
tug,-4,'e'
bug,1,'e'""") as fp:
    E = pd.read_csv(fp)

#display(D.merge(E, on=['x', 'y'], how='outer'))
#display(D.merge(E, on=['x', 'y'], how='left'))
#display(D.merge(E, on=['x', 'y'], how='right'))
#display(D.merge(E, on=['x', 'y']))

G = C.copy()
G['year'] = G['year'].apply(lambda x: "'{:02d}".format(x % 100))
#display(G)

#7.0.2 (2 points)
def calc_prevalence(G):
    H = G.copy()
    H['prevalence'] = H.apply(lambda row: row['cases'] / row['population'], axis=1)
    return H
#SAVE_APPLY = getattr(pd.DataFrame, 'apply')

#7.0.3
def canonicalize_tibble(X):
    # Enforce Property 1:
    var_names = sorted(X.columns)
    Y = X[var_names].copy()
    # 2 sort by rows
    Y.sort_values(by=var_names, inplace=True)
    # 3 index 0 to n-1
    a=list(range(0,len(Y)))
    Y.set_index( [a] , inplace=True)

    return Y

#display(canonicalize_tibble(G))
#var_names = sorted(G.columns)
#Y = G[var_names].copy()
#display(Y)
#Y.sort_values(by=var_names, inplace=True)
#display(Y)
##Y.set_index( ['country','year'], inplace=True)
#a=[i for i in range(0,len(H))]
#H.set_index( [a], inplace=True)

#7.0.4
def tibbles_are_equivalent(A, B):
    # Given two tidy tables ('tibbles'), returns True iff they are equivalent.
    Ac = canonicalize_tibble(A)
    Bc = canonicalize_tibble(B)
#    return Ac.equals(Bc)
    return pd.DataFrame.all(Ac==Bc).all()

#tibbles_are_equivalent(C, G)

#7.0.5
def melt(df, col_vals, key, value):
    assert type(df) is pd.DataFrame

    varM=[i for i in list(df.columns) if i not in col_vals] 
    ndf = None
    for i in col_vals:
        varT = varM + [i]
        tdf=df[varT].copy()
        tdf.rename(columns={i: value}, inplace=1)  #e.g. rename year to cases
        tdf[key]=i    # add column for key (e.g. year) with value i (e.g. 1999)
        if ndf is None:
            ndf = tdf
        else:
            ndf = ndf.merge(tdf, how='outer')
    return ndf

df=pd.read_csv('table4a.csv')
col_vals=['1999','2000']
key='year'
value='cases'
#display(melt(df, col_vals, key, value))

#7.0.6a
def cast(df, key, value, join_how='outer'):
    # Casts the input data frame into a tibble, given the key column and value column.
    assert type(df) is pd.DataFrame
    assert key in df.columns and value in df.columns
    assert join_how in ['outer', 'inner']
    
    fixed_vars = list(df.columns.difference([key, value]))
    tibble = pd.DataFrame(columns=fixed_vars) # empty frame
    
    new_vars=list(set(df[key]))
    for i in new_vars:
        tdf=df[df[key]==i]    #return subset where key==i e.g. key==cases or population
        tdf = tdf[fixed_vars+[value]]   # extract data for that key e.g. from value 'count'
        tdf.rename(columns={value: i}, inplace=1)  # rename to key
        tibble=tibble.merge(tdf, on=fixed_vars, how=join_how)  
    return tibble

df=pd.read_csv('table2.csv')
key='type'
value='count'
fixed_vars = list(df.columns.difference([key, value]))
fixed_vars
#display(cast(df,key,value))

#7.0.6b
table3 = pd.read_csv('table3.csv')

import re

def default_splitter(text):
    """Searches the given spring for all integer and floating-point
    values, returning them as a list _of strings_.
    E.g., the call
      default_splitter('Give me $10.52 in exchange for 91 kitten stickers.')
    will return ['10.52', '91'].
    """
    fields = re.findall('(\d+\.?\d+)', text)
    return fields
    
def separate(df, key, into, splitter=default_splitter):
    # Given a data frame, separates one of its columns, the key, into new variables.
    assert type(df) is pd.DataFrame
    assert key in df.columns
    # Hint: http://stackoverflow.com/questions/16236684/apply-pandas-function-to-column-to-create-multiple-new-columns

    def apply_splitter(text):
        fields = splitter(text)
        return pd.Series({into[i]:f for i, f in enumerate(fields)})

    ndf = df['rate'].apply(apply_splitter)
    ndf = pd.concat([df,ndf], axis=1)
    del ndf[key]
    return ndf
    
key='rate'
into=['cases','population']
df=table3
i='cases'
display(separate(df, key, into))

#7.0.7
who_raw = pd.read_csv('who.csv')
print("=== WHO TB data set: {} rows x {} columns ===".format(who_raw.shape[0],
                                                              who_raw.shape[1]))
print("Column names:", who_raw.columns)
print("\n=== A few randomly selected rows ===")
import random
row_sample = sorted(random.sample(range(len(who_raw)), 5))
display(who_raw.iloc[row_sample])
