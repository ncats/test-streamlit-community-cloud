import streamlit as st
import multiprocessing
import os
import pandas as pd


def main():

    st.title('Hello World 2')
    st.write('This is a simple Streamlit app.')

    st.selectbox('Select a number', [1, 2, 3], key='number')

    st.write(f'You selected {st.session_state["number"]}')

    # Write number of processors available
    st.write(f'Number of processors: {multiprocessing.cpu_count()}')

    st.write(pd.DataFrame(os.listdir('.')))

    uploaded_files = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=True
    )
    for uploaded_file in uploaded_files:
        st.write(uploaded_file.name)
        st.write(pd.read_csv(uploaded_file))

    st.write(len(uploaded_files))


if __name__ == '__main__':
    main()
