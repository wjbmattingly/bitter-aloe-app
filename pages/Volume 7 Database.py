import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

@st.cache(allow_output_mutation=True)
def cache_df():
    return (pd.read_json("data/vol7.json"))

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.header("Volume 7 Database")

database_directions = read_markdown_file("markdown_files/database.md")
directions = st.expander("Directions")
directions.markdown(database_directions, unsafe_allow_html=True)

df = cache_df()
df = df.fillna(" ")
descs = list(df["descriptions"])
people = list(df["names"])

form_options = st.form("Query Form")
strict_box = form_options.checkbox("Strict Search On")
description_search = form_options.text_input(f"Descriptions ({len(descs)})")
people_select = form_options.multiselect(f"People ({len(people)})", people)
if form_options.form_submit_button():
    if strict_box == True:
        description_search = description_search.split("|")
        cond1 = df['descriptions'].str.findall('|'.join(description_search)).map(lambda x: len(set(x)) == len(description_search))

        new_df = df.loc[cond1, :]
        st.write(len(new_df))
        st.table(new_df)
    else:
        if len(description_search) > 0:
            main_cond = df['descriptions'].str.fullmatch(description_search)
            if len(people_select) > 0:
                cond2  = [x for x in df['names'].str.contains("|".join(people_select))]
                i=0
                for c in cond2:
                    if c == True:
                        main_cond[i] = True
                    i=i+1
        else:
            if len(people_select) > 0:
                main_cond = [x for x in df['names'].str.contains("|".join(people_select))]


        new_df = df.loc[main_cond, :]
        st.write(f"The Total Number of Results is {len(new_df)}")
        st.table(new_df)
# if strict_box == False:
#     cond1  = [any(y in mss_select for y in x ) for x in df['valid_mss'].str.split(", ")]
#     main_cond = cond1
#     if len(people_select) > 0:
#         cond2  = [x for x in df['pase_refs'].str.contains("|".join(people_select))]
#         main_cond = cond1
#         i=0
#         for c in cond2:
#             if c == True:
#                 main_cond[i] = True
#             i=i+1
#
#     new_df = df.loc[main_cond, :]
# else:
#     #https://stackoverflow.com/questions/60932036/check-if-pandas-column-contains-all-elements-from-a-list
#     mss_select = set(mss_select)
#     cond1 = [x for x in df['valid_mss'].str.split(", ").apply(lambda x: set(mss_select).issubset(x))]
#     cond2 = [x for x in df['pase_refs'].apply(lambda x: np.all([*map(lambda l: l in x, people_select)]))]
#
#
#     main_cond = []
#     i=0
#     for c in cond2:
#         if c == True and cond1[i] == True:
#             main_cond.append(True)
#         else:
#             main_cond.append(False)
#         i=i+1
#     new_df = df.loc[main_cond, :]
#
# st.table(new_df)
