import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Automation Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #f0f8ff;
    }
    .main-header {
        text-align: center;
        font-size: 32pt;
        font-weight: bold;
        color: #2E8CA8;
        margin-bottom: 10px;
    }
    .main-subheader {
        text-align: center;
        font-size: 16pt;
        color: #666;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Main page content
if 'df_uploaded' not in st.session_state:
    st.session_state.df_uploaded = None
if 'file_name' not in st.session_state:
    st.session_state.file_name = None
if 'processed' not in st.session_state:
    st.session_state.processed = False

# Display main page
st.markdown('<div class="main-header">📊 Automation Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subheader">Excel Data Processing & Analytics</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    ### Welcome to the Automation Dashboard! 🎯
    
    This application helps you:
    - 📁 **Upload** your Excel data
    - 📊 **Process** the information
    - 📈 **Visualize** through interactive dashboards
    - 📋 **Analyze** utilization metrics and performance data
    
    ### Quick Start:
    1. Navigate to **Home** in the sidebar
    2. Upload your Excel file
    3. Preview and verify your data
    4. Click **Process & Go to Dashboard**
    5. View your analytics in the **Dashboard** page
    
    """)

st.markdown("---")

# Status section
if st.session_state.df_uploaded is not None:
    st.success("✅ Data is ready! Navigate to Dashboard to view analytics.")
else:
    st.info("👉 Get started by clicking **Home** in the sidebar to upload your data.")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #999; font-size: 12pt; margin-top: 30px;">
    <p>Dashboard v1.0 | Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)
