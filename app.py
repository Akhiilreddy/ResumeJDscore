import streamlit as st
from index_resumes import store
from query import search_resumes

st.title("🔍 AI Resume Search Engine")
job_desc = st.text_area("Enter Job Description:")

if st.button("Search"):
    if job_desc:
        results = search_resumes(store, job_desc)
        for res, score in results:
            st.write(f"**File**: {res['filename']} | **Similarity Score**: {round(score, 2)}")
            with st.expander("Show Resume Text"):
                st.write(res['text'])
