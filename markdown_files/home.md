This is the Bitter Aloe Project's application. It is designend in Streamlit and is a work in progress. On this application, you will be able to use some of the tools we are developing for analysis of documents related to South Africa's Truth and Reconciliation Commission (TRC). You can navigate to different tools through the portal on the left.

### Volume 7 Database
The Volume 7 Database allows you to interrogate the data from Volume 7 of the TRC's final report. Here, you will be able to narrow your searches based on parameters, such as victim's name and a search across all descriptions.

### Sentence Embedding Analysis (Old)
Like the Volume 7 Database, the Sentence Embedding Analysis tool allows you to examine and study the Volume 7 data. In this tool, however, you are able to leverage the power of machine learning to dynamically search across all documents based on a document's similarity. The older version of this app will be replaced in June with the newer version based on the Top2Vec library.

This part of the app is still live, but we are using the Top2Vec app to do similar analysis with quicker and better results.

### Top2Vec Analysis
At the core of this tool is a model trained through the Top2Vec library. The model was finetuned on the Volume 7 Data. Like the Sentennce Embedding Analysis tool, this allows you to dynamically search across documents by vector similarity. It is a bit more robust than the Sentence Embedding Analaysis tool because of the Top2Vec library's built-in functions for analyzing document similarity in a myraid of ways.
