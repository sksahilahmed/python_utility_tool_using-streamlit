# Dashboard Application Flow & Architecture

## 📊 Application Flow

```
START
  │
  ├─→ app.py (Main Entry Point)
  │     │
  │     └─→ st.session_state initialization
  │         - df_uploaded (data storage)
  │         - file_name (current file)
  │         - processed (status flag)
  │
  ├─→ Sidebar Navigation
  │     │
  │     ├─→ Home (01_Home.py)
  │     │     │
  │     │     ├─ Upload Excel File
  │     │     │   └─ File validation
  │     │     │
  │     │     ├─ Preview Data
  │     │     │   └─ Multi-sheet display
  │     │     │
  │     │     └─ Process Button
  │     │         └─ Store in session_state
  │     │
  │     └─→ Dashboard (02_Dashboard.py)
  │           │
  │           ├─ Check session_state
  │           │   └─ If no data: warn & stop
  │           │
  │           └─ Render 5 Sections:
  │               ├─ Utilization Graphs
  │               ├─ Overall RL
  │               ├─ Optimization Summary
  │               ├─ Other Recommended Tools
  │               └─ GradeWise MnM RL
  │
  └─→ END
```

## 🏗️ Directory Structure

```
python_automation_utility/
│
├── app.py                          ← Main entry point
│   └── Renders welcome page
│       Initializes session state
│       Navigation menu
│
├── pages/                          ← Streamlit auto-discovered
│   │
│   ├── 01_Home.py                 ← Home page
│   │   ├── File upload widget
│   │   ├── Data preview (multi-sheet)
│   │   ├── Process button
│   │   └── Session state storage
│   │
│   └── 02_Dashboard.py            ← Dashboard page
│       ├── Data validation
│       ├── 5 dashboard sections
│       ├── Styling & formatting
│       └── Chart rendering
│
├── dashboard.py                    ← Legacy (deprecated)
│
├── create_sample.py                ← Sample data generator
│
├── verify_setup.py                 ← Setup verification
│
├── sample_dashboard_data.xlsx      ← Sample Excel file
│
├── README.md                       ← Full documentation
│
└── QUICKSTART.md                   ← Quick reference
```

## 🔄 Data Flow

```
Excel File Upload
      │
      ▼
File Validation
      │
      ▼
Read with pandas.ExcelFile
      │
      ├─→ Extract all sheet names
      └─→ Read each sheet into DataFrame
      
      ▼
Store in st.session_state['df_uploaded']
      │
      ├─ key: sheet_name
      └─ value: DataFrame
      
      ▼
User clicks "Process & Go to Dashboard"
      │
      ▼
Set st.session_state['processed'] = True
      │
      ▼
Navigate to Dashboard page
      │
      ▼
Dashboard retrieves data from session_state
      │
      ├─→ Extract values for sections
      └─→ Render visualizations
      
      ▼
Display Analytics Dashboard
```

## 📱 Page Components

### Home Page (01_Home.py)

**Header Section:**
- Title: "📊 Automation Dashboard"
- Subheader: "Home - Upload & Preview"

**Upload Section:**
- File uploader widget (accepts .xlsx, .xls)
- Drag-and-drop support
- File validation

**Preview Section:**
- Multiple tabs (one per sheet)
- DataFrames displayed with columns
- Row and column count info

**Action Section:**
- Process button (enabled when file loaded)
- Status messages
- Instructions expander

### Dashboard Page (02_Dashboard.py)

**Header Section:**
- Title with file name display
- Navigation info

**Section 1: Utilization Graphs**
- 3-column layout
- Donut charts: Triaging (7%), Non-Ticketed (54%), Ticketed (39%)
- Teal/Light-Teal colors
- Centered labels

**Section 2: Overall RL**
- 3-column table
- Columns: Period, RL, Remarks
- Teal header bar
- Left-aligned remarks

**Section 3: Optimization Summary**
- 3-column table
- Columns: Lever, # of Usecases, FTE
- Bold lever names
- Light gray borders

**Section 4: Other Recommended Tools**
- 2-column table
- Criteria to Tool mapping
- ServiceNow Performance Analytics

**Section 5: GradeWise MnM RL**
- Full-width grid table
- 7 rows × 19 columns
- Empty cells for data entry
- Centered headers

## 🎨 Styling Architecture

### Color Scheme
```
Primary:      #2E8CA8 (Teal)
Secondary:    #1F6C86 (Dark Teal - gradient end)
Accent:       #BFE2EA (Light Teal)
Grid Lines:   #D9D9D9 (Light Gray)
Text:         Black (regular), White (on headers)
Background:   White
```

### Typography
```
Header Bars:  14pt, Bold, White, Centered
Subheaders:   11pt, Bold
Body Text:    10pt, Regular
Font Family:  Segoe UI, Calibri, sans-serif
```

### Spacing
```
Page Margins:     0.5 inch all sides
Section Spacing:  12-16px
Cell Padding:     8-12px
```

### Layout
```
Sections 1-4:   2-column grid (left | right)
Section 5:      Full-width
Column Gap:     Large (visual separation)
```

## 🔐 Session State Management

```python
st.session_state = {
    'df_uploaded': {
        'sheet_name_1': DataFrame,
        'sheet_name_2': DataFrame,
        ...
    },
    'file_name': str,
    'processed': bool
}
```

### Lifecycle
1. **Initialization**: Each page initializes missing keys
2. **Upload**: Home page populates df_uploaded
3. **Processing**: Process button sets processed = True
4. **Persistence**: Data available until session ends
5. **Reset**: Return to home and upload new file

## 🧩 Key Functions

### Home Page Functions
```python
# Main function flow
1. Initialize session_state
2. Create upload widget
3. If file uploaded:
   - Read Excel file
   - Display preview in tabs
   - Store in session_state
4. If processed:
   - Show success message
   - Navigation hint
```

### Dashboard Functions
```python
gradient_header(title)
  └─ Renders teal gradient header bar

donut_chart(label, value, alt_text)
  └─ Creates and displays donut chart

render_donut_section(data=None)
  └─ Renders 3-chart Utilization section

render_overall_rl_section(data=None)
  └─ Renders Overall RL table

render_optimization_summary_section(data=None)
  └─ Renders Optimization Summary table

render_other_tools_section(data=None)
  └─ Renders Recommended Tools table

render_gradewise_mnm_rl_section(data=None)
  └─ Renders GradeWise grid

styled_table(df, col_widths, remark_align, row_heights)
  └─ Applies consistent table styling
```

## 🔄 User Workflow

```
1. User launches app
   └─ streamlit run app.py

2. Browser opens to main page
   └─ Sees welcome message
   └─ Sidebar has "Home" and "Dashboard"

3. User clicks "Home"
   └─ Sees file upload widget

4. User uploads Excel file
   └─ File is read
   └─ Sheets displayed in tabs
   └─ Preview shown

5. User clicks "Process & Go to Dashboard"
   └─ Data stored in session_state
   └─ Success message displayed

6. User clicks "Dashboard" in sidebar
   └─ Dashboard page checks session_state
   └─ Renders all 5 sections
   └─ Shows uploaded data

7. User can explore and analyze
   └─ View tables
   └─ See charts
   └─ Read recommendations

8. User wants new data
   └─ Clicks "Home" again
   └─ Uploads new Excel file
   └─ Process repeats
```

## 📊 Excel Sheet Requirements

### For full functionality, Excel should have sheets:

**Sheet 1: Overall RL**
```
| Period | RL | Remarks/information icon |
|--------|----|----|
| H1Y1   | 0  | Description |
```

**Sheet 2: Optimization Summary**
```
| Lever | # of Usecases | FTE |
|-------|---------------|-----|
| Name  | 0             | 0   |
```

**Sheet 3: Recommended Tools**
```
| Criteria/Recommendation | Tool/Action |
|------------------------|-------------|
| Criteria Name          | Tool Name   |
```

## 🚀 Performance Considerations

- File size limit: ~10MB recommended
- Charts: Generated in-memory, rendered immediately
- Tables: Streamed as DataFrames
- Session data: Cleared on session end
- No database required: Fully in-memory operation

## 🛡️ Error Handling

```
Home Page:
  └─ Invalid file format → Show error message
  └─ Missing sheets → Display available sheets
  └─ Empty data → Warn user

Dashboard Page:
  └─ No session data → Show warning, stop rendering
  └─ Chart error → Fall back to static values
  └─ Display error → Show error message
```

---

**Last Updated**: November 26, 2025
**Version**: 1.0
