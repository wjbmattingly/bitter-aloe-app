import streamlit as st
from top2vec import Top2Vec
import pandas as pd

@st.cache(allow_output_mutation=True)
def cache_df():
    df = pd.read_json("data/vol7.json")
    names = df.names.tolist()
    return df, names

@st.cache(allow_output_mutation=True)
def load_model():
    model = Top2Vec.load("data/top2vec-model")
    num_topics = model.get_num_topics()
    topic_sizes, topic_nums = model.get_topic_sizes()
    topic_words, word_scores, topic_nums = model.get_topics(num_topics)
    return Top2Vec.load("data/top2vec-model"), num_topics, topic_sizes, topic_nums, topic_words, word_scores, topic_nums

df, names = cache_df()


model, num_topics, topic_sizes, topic_nums, topic_words, word_scores, topic_nums = load_model()

st.markdown("# Sentence Embedding Analysis with Top2Vec(New)")

st.write(f"There are {num_topics} across all Volume 7 Data")

topic_num = st.number_input("Which Topic Number would you like to search?", 0, max_value=num_topics)
num_docs = st.number_input("How many documents do you want to see from this topic?", 5, max_value=topic_sizes[topic_num])
documents, document_scores, document_ids = model.search_documents_by_topic(topic_num=topic_num, num_docs=num_docs)


st.header(f"Topic {topic_num} Data")
data_expander = st.expander("data")
res = {"Topic Words": topic_words[topic_num], "Similarity to Topic": word_scores[topic_num]}
res_df = pd.DataFrame(res)

data_expander.table(res_df)
st.header("RESULTS")
st.write(f"There are a total of {topic_sizes[topic_num]} available. Currently only displaying the top-{num_docs} results.")
for doc, score, doc_id in zip(documents, document_scores, document_ids):
    st.header(f"Victim: {names[doc_id]}")
    st.write(f"Document: {doc_id}")
    st.write(f"Score: {score}")
    st.write(f"Description: {doc}")
    st.write("-----------")
    st.write()
    st.write()
