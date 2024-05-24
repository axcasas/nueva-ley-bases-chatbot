# Chat With Nueva Ley Bases (and other PDFs)

About This Project
==

This repository is dedicated to my project focused on improving access to information within the "Nueva Ley Bases" (New Foundations Law) proposed by the Argentinian government under Javier Milei's leadership. 

The project aims to achieve this by developing a specialized chatbot for interacting with PDF documents and creating a user-friendly graphical interface (GUI). 

Its primary goal is to democratize access to legal information by enabling direct querying of the document's content. 

## Objectives

- To create a chatbot for PDFs, particularly with the New Laws proposed by the Argentinian government. 
- To build a graphic user interface (GUI) to allow users to chat easily. 
- Make information about the "Nueva Ley Bases" more affordable to people by directly asking the document questions about its content. 

## About This Repository

```
├── README.md
├── app.py <- Streamlit app for the chatbot 
|
└── chatbot
     ├── chatbot.py <- class for conversational chat
     ├── embedding.py <- embedder class for pdf documents
├── data
   ├── nueva_ley_bases <- Data from the new laws proposed by the current Argentian goverment of Javier Milei.
|
└── gui
|   ├── history.py <- chat history to generate messages
|   ├── layout.py <- app's layout
|   ├── sidebar.py <- app's sidebar
```

Requirements 
===

Python version > 3.10

- langchain==0.0.294
- streamlit==1.29.0
- streamlit_chat_media==0.0.4
- pypdf==3.16.1
- openai==0.27.8

Run the app 
===
streamlit run app.py