import streamlit as st
from index_resumes import store
from query import search_resumes

st.title("🔍 AI Resume Search Engine")
job_desc = st.text_area("Enter Job Description:")

if st.button("Search"):
    if job_desc:
        results = search_resumes(store, job_desc)
        for res, score in results:
            percentage = score * 100
            st.write(f"**File**: {res['filename']} | **Match Score**:  {percentage:.1f}%")
            with st.expander("Show Resume Text"):
                st.write(res['text'])
