# Automation Dashboard with Excel Data Processing

A comprehensive Streamlit-based dashboard application that allows users to upload Excel files and visualize dashboard analytics including utilization graphs, optimization summaries, and performance metrics.

## Features

✨ **Multi-page Application**
- Home page for file upload and data preview
- Dashboard page for analytics visualization
- Easy navigation between sections

📁 **Excel Upload & Processing**
- Drag-and-drop file upload
- Multi-sheet support
- Real-time data preview
- Data validation

📊 **Interactive Dashboard**
- Utilization donut charts (Triaging, Non-Ticketed, Ticketed)
- Overall RL summary table
- Optimization Summary with lever analysis
- Recommended Tools mapping
- GradeWise MnM RL grid

🎨 **Professional Styling**
- Teal gradient headers (#2E8CA8 → #1F6C86)
- Responsive layout (2-column for sections 1-4, full-width section 5)
- Consistent color scheme and typography
- 0.5-inch page margins

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd "e:\Automation tech\python_automation_utility"
```

2. Install required packages:
```bash
pip install streamlit pandas openpyxl matplotlib numpy
```

3. Verify installation:
```bash
python -m py_compile app.py pages/01_Home.py pages/02_Dashboard.py
```

## Usage

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Workflow

1. **Home Page** (Default landing page)
   - Upload your Excel file (.xlsx or .xls)
   - Preview data from all sheets
   - Click "Process & Go to Dashboard" button

2. **Dashboard Page**
   - View all visualizations and tables
   - Analyze data with interactive charts
   - Review metrics and recommendations

3. **Update Data**
   - Return to Home page
   - Upload a new Excel file
   - Process and view updated dashboard

## Excel File Format

### Expected Structure

Your Excel file should contain one or more sheets with structured data:

**Sheet 1: Overall RL** (Optional)
- Columns: `Period`, `RL`, `Remarks/information icon`
- Example: H1Y1, (blank), "140 Tickets productivity No automation"

**Sheet 2: Optimization Summary** (Optional)
- Columns: `Lever`, `# of Usecases`, `FTE`
- Example: Elimination, (number), (number)

**Sheet 3: Recommended Tools** (Optional)
- Columns: `Criteria/Recommendation`, `Tool/Action`
- Example: "P1/P2 >= 10", "CRTSIT Assist"

### Sample File

A sample file is provided: `sample_dashboard_data.xlsx`

To regenerate it:
```bash
python create_sample.py
```

## Dashboard Sections

### 1. Utilization Graphs
- Three donut charts displaying utilization percentages
- Triaging, Non-Ticketed, Ticketed metrics
- Customizable values via Excel upload

### 2. Overall RL (Response Level)
- Period-based analysis table
- Performance metrics and remarks
- Left-aligned remarks column

### 3. Optimization Summary
- Lever categorization (Elimination, Automation, etc.)
- Use case and FTE tracking
- Bold lever labels for emphasis

### 4. Other Recommended Tools
- Criteria-to-tool mapping
- Service improvement recommendations
- ServiceNow Performance Analytics reference

### 5. GradeWise MnM RL
- 7-row (Grade, PAT/PT, PA/P, A, SA, M, SM) × 19-column (M1-M18) grid
- Empty cells for data entry
- Centered headers with teal gradient

## Architecture

```
python_automation_utility/
├── app.py                    # Main entry point
├── pages/
│   ├── 01_Home.py           # Upload & preview page
│   └── 02_Dashboard.py       # Analytics visualization page
├── dashboard.py             # Legacy dashboard (deprecated)
├── create_sample.py         # Sample file generator
└── sample_dashboard_data.xlsx # Sample Excel file
```

## Session State Management

The app uses Streamlit's session state to:
- Store uploaded file data (`df_uploaded`)
- Track file name (`file_name`)
- Manage processing status (`processed`)
- Maintain data across page navigation

## Styling & Colors

- **Primary Color**: Teal (#2E8CA8)
- **Secondary Color**: Dark Teal (#1F6C86)
- **Accent Color**: Light Teal (#BFE2EA)
- **Grid Lines**: Light Gray (#D9D9D9)
- **Font**: Segoe UI, Calibri, sans-serif
- **Header Font Size**: 14pt bold
- **Body Font Size**: 10pt regular

## Troubleshooting

### File Upload Issues
- Ensure file is in .xlsx or .xls format
- Check that data has headers in first row
- Verify sheet names don't have special characters

### Display Issues
- Clear browser cache (Ctrl+Shift+Delete)
- Restart Streamlit app (Ctrl+C, then `streamlit run app.py`)
- Check terminal for error messages

### Data Not Showing
- Return to Home page
- Verify data is displayed in preview
- Check that "Process" button was clicked
- Navigate to Dashboard page again

## Performance Notes

- Large Excel files (>10MB) may take longer to upload
- Charts are generated in-memory for better performance
- Session data persists during the current session only

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Customization

### Modifying Dashboard Layout
Edit `pages/02_Dashboard.py`:
- Adjust column layouts in `main()` function
- Modify colors using TEAL_START, TEAL_END constants
- Update header bar styling

### Adding New Sections
Add new functions in `pages/02_Dashboard.py`:
```python
def render_custom_section(data=None):
    gradient_header("Section Title")
    # Add your content here
    st.dataframe(your_data)
```

### Changing Donut Chart Values
Edit `render_donut_section()` to accept different data:
```python
donut_data = [
    ("Label", value_percentage, "alt_text"),
    # Add more tuples as needed
]
```

## Known Limitations

1. Donut charts display fixed values (7%, 54%, 39%) - configure via Excel in future version
2. GradeWise grid is for reference/entry only - data not persisted
3. Table styling may vary slightly across browsers
4. Export functionality not yet implemented

## Future Enhancements

- [ ] Excel data binding for chart values
- [ ] Export dashboard as PDF or PowerPoint
- [ ] Data persistence with database backend
- [ ] Advanced filtering and drill-down capabilities
- [ ] Real-time data synchronization
- [ ] User authentication and role-based access
- [ ] Dashboard templates

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review error messages in browser console and terminal
3. Verify Excel file format and content
4. Ensure all dependencies are installed

## Version

**Dashboard v1.0** | Powered by Streamlit

---

**Created**: November 26, 2025
**Last Updated**: November 26, 2025
