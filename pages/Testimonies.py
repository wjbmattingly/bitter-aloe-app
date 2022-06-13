import streamlit as st
import json
import pandas as pd
import glob
import pathlib

@st.cache(allow_output_mutation=True)
def cache_speakers():
    with open ("./data/all_speakers.json", "r") as f:
        speakers = json.load(f)
    return speakers

st.title("")
style = st.sidebar.selectbox("Select Testimony Analysis Method", [
                                                            "By Testimony",
                                                            "By Person"

                                                                ])
if style == "By Testimony":
    st.title("Testimony Analysis by Testimony")
    testimony_type = st.selectbox("Select Testimony Type", [
                                            # "Amnesty Decisions",
                                            "Amnesty Hearings",
                                            "Human Rights Violation Hearings",
                                            "Special Hearings"
                                            ])

    testimony_type_file = testimony_type.lower().replace(" ", "_")
    files = glob.glob(f"./data/data_saha/{testimony_type_file}/*/*.json")
    places = list(set([x.replace("\\", "/").split("/")[-2].replace("_", " ").title() for x in files]))
    places.sort()
    if testimony_type == "Special Hearings":
        location = st.selectbox("Select Testimony Category", places)
    else:
        location = st.selectbox("Select Location", places)
    file_location = location.lower().replace(" ", "_")
    loc_files = glob.glob(f"./data/data_saha/{testimony_type_file}/{file_location}/*.json")
    potential_files = [x.replace("\\", "/").split("/")[-1] for x in loc_files]
    testimony_file = st.selectbox("Select Testimony", potential_files)
    with open(f"./data/data_saha/{testimony_type_file}/{file_location}/{testimony_file}", "r") as f:
        data = json.load(f)
    speakers = ["All"]+data['header']['speakers']
    speakers = [x.replace("\n", "") for x in speakers]
    narrow_speakers = st.multiselect("Select Speaker(s)", speakers, ["All"])
    st.write("-----")
    st.header("Header Metadata")
    for item in data['header']:
        st.write(f"{item.title()}: {data['header'][item]}")
    st.write("-----")
    st.header("Testimony")
    st.write("-----")
    for i, segment in enumerate(data["testimony"]):
        if "All" in narrow_speakers or segment[0] in narrow_speakers:
            st.markdown(f"(Index {i}) **{segment[0]}**: {segment[1]}")
            st.write("-----")
elif style == "By Person":
    st.markdown("**This is in Development**")
    st.title("Testimony Analysis by Person")
    all_speakers = cache_speakers()
    speaker_names = list(all_speakers.keys())
    speaker_names.sort()
    people = st.multiselect("Select People", speaker_names)
    corrected_people = [p.replace("\n", "") for p in people]
    for person in people:
        st.header(f"Displaying the Data for {person}")
        for filename in all_speakers[person]:
            filename = filename.replace("\\", "/").replace("..", ".")
            st.markdown(f"**Displaying Dialogue Found in**: {filename}")
            with open (filename, "r") as f:
                testimony = json.load(f)["testimony"]
            for i, segment in enumerate(testimony):
                if segment[0] in corrected_people:
                    st.markdown(f"(Index {i}) **{segment[0]}**: {segment[1]}")
            st.write("-----")
