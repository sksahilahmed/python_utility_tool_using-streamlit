import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="Dashboard - Home",
    layout="wide",
)

st.markdown("""
<style>
    .header-title {
        text-align: center;
        font-size: 28pt;
        font-weight: bold;
        color: #2E8CA8;
        margin-bottom: 20px;
    }
    .upload-section {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 5px;
        border: 2px solid #2E8CA8;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-left: 4px solid #2E8CA8;
        margin-bottom: 15px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header-title">📊 Automation Dashboard</div>', unsafe_allow_html=True)

st.markdown("---")

# Initialize session state
if 'df_uploaded' not in st.session_state:
    st.session_state.df_uploaded = None
if 'file_name' not in st.session_state:
    st.session_state.file_name = None

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.subheader("📁 Upload Excel File")
    
    uploaded_file = st.file_uploader(
        "Choose an Excel file (.xlsx, .xls)",
        type=["xlsx", "xls"],
        help="Upload your data in Excel format. The file should contain data for the dashboard."
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("**📋 File Requirements:**")
    st.markdown("- Excel format (.xlsx or .xls)")
    st.markdown("- Structured data with headers")
    st.markdown("- Compatible with dashboard fields")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# File preview section
if uploaded_file is not None:
    st.subheader("📋 File Preview")
    
    try:
        # Read the Excel file
        excel_file = pd.ExcelFile(uploaded_file)
        
        # Show sheet names
        st.write(f"**Sheet Names:** {', '.join(excel_file.sheet_names)}")
        
        # Create tabs for each sheet
        sheet_tabs = st.tabs(excel_file.sheet_names)
        
        sheet_data = {}
        for idx, sheet_name in enumerate(excel_file.sheet_names):
            with sheet_tabs[idx]:
                df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
                sheet_data[sheet_name] = df
                st.dataframe(df, use_container_width=True)
                st.write(f"**Rows:** {len(df)} | **Columns:** {len(df.columns)}")
        
        # Store in session state
        st.session_state.df_uploaded = sheet_data
        st.session_state.file_name = uploaded_file.name
        
    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
        st.session_state.df_uploaded = None

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("")

with col2:
    if uploaded_file is not None and st.session_state.df_uploaded is not None:
        if st.button("✅ Process & Go to Dashboard", key="process_btn", use_container_width=True):
            st.session_state.processed = True
            st.success("✓ File processed successfully!")
            st.info("👉 Navigate to 'Dashboard' page to view your data")
            st.balloons()
    else:
        st.button("✅ Process & Go to Dashboard", disabled=True, use_container_width=True, 
                 help="Please upload a file first")

with col3:
    st.markdown("")

# Display status
if uploaded_file is not None:
    st.markdown("---")
    st.success(f"✓ File loaded: **{uploaded_file.name}**")
    if 'processed' in st.session_state and st.session_state.processed:
        st.info("✓ Ready to view dashboard. Use the sidebar to navigate to Dashboard page.")

# Instructions section
st.markdown("---")
st.subheader("📖 Instructions")

with st.expander("How to Use", expanded=False):
    st.markdown("""
    1. **Upload File**: Click the upload button above and select your Excel file
    2. **Preview Data**: Review the data in the preview section to ensure it's correct
    3. **Process**: Click the "Process & Go to Dashboard" button
    4. **View Dashboard**: Navigate to the Dashboard page using the sidebar
    5. **Analyze**: Review all dashboard sections with your data
    
    ### Expected Excel Format:
    - Sheet 1: Main data with columns matching dashboard fields
    - Ensure headers are in the first row
    - Data should be structured and clean
    """)
