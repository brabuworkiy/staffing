import base64
import pandas as pd
import streamlit as st


# Function to compare two dataframes and find new data
def find_new_data(df1, df2):
    comparison_df = df1.merge(df2, indicator=True, how='outer')
    new_data = comparison_df[comparison_df['_merge'] == 'right_only'].drop(columns='_merge')
    return new_data


def main():
    st.title('WORKIY INDIA STAFFING')
    st.subheader("[Compare Both Excel to Get The New Data]")
    st.sidebar.title('Compare both excel to get the new data ')
    uploaded_file1 = st.sidebar.file_uploader("Upload Previous Download Excel file", type=["xlsx"])
    uploaded_file2 = st.sidebar.file_uploader("Upload Current Download Excel file", type=["xlsx"])

    if uploaded_file1 and uploaded_file2:
        st.sidebar.success('Files uploaded successfully.')

        # Load Excel files
        df1 = pd.read_excel(uploaded_file1)
        df2 = pd.read_excel(uploaded_file2)

        # Display all data
        st.subheader('Data from File 1:')
        st.write(df1)

        st.subheader('Data from File 2:')
        st.write(df2)

        # Compare dataframes
        new_data = find_new_data(df1, df2)

        st.write("Length of DataFrame 1:", len(df1))
        st.write("Length of DataFrame 2:", len(df2))
        st.write("Length of New Data:", len(new_data))

        if not new_data.empty:
            st.subheader('New Data Found:')
            st.write(new_data)

            # Download new data
            csv_data = new_data.to_csv(index=False, encoding='utf-8-sig')
            b64 = base64.b64encode(csv_data.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="new_data.csv">Download New Data</a>'
            st.markdown(href, unsafe_allow_html=True)

        else:
            st.subheader('No New Data Found.')


if __name__ == "__main__":
    main()
