import streamlit as st
import json
import pandas as pd
import glob

st.title("")

testimony_type = st.selectbox("Select Testimony Type", [
                                        # "Amnesty Decisions",
                                        "Amnesty Hearings",
                                        "Human Rights Violation Hearings",
                                        "Special Hearings"
                                        ])
# if testimony_type == "Amnesty Hearings":
testimony_type_file = testimony_type.lower().replace(" ", "_")
files = glob.glob(f"./data/data_saha/{testimony_type_file}/*/*.json")
places = list(set([x.split("\\")[-2].replace("_", " ").title() for x in files]))
places.sort()
if testimony_type == "Special Hearings":
    location = st.selectbox("Select Testimony Category", places)
else:
    location = st.selectbox("Select Location", places)
file_location = location.lower().replace(" ", "_")
loc_files = glob.glob(f"./data/data_saha/{testimony_type_file}/{file_location}/*.json")
potential_files = [x.split("\\")[-1] for x in loc_files]
testimony_file = st.selectbox("Select Testimony", potential_files)
with open(f"./data/data_saha/{testimony_type_file}/{file_location}/{testimony_file}", "r") as f:
    data = json.load(f)
speakers = ["All"]+data['header']['speakers']
speakers = [x.replace("\n", "") for x in speakers]
narrow_speakers = st.multiselect("Select Speaker(s)", speakers, ["All"])
st.write("-----")
for item in data['header']:
    st.write(f"{item.title()}: {data['header'][item]}")
st.write("-----")
st.write("-----")
for i, segment in enumerate(data["testimony"]):
    if "All" in narrow_speakers or segment[0] in narrow_speakers:
        st.markdown(f"(Index {i}) **{segment[0]}**: {segment[1]}")
        st.write("-----")
