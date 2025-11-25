# Quick Start Guide

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install streamlit pandas openpyxl matplotlib numpy
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

### Step 3: Upload & Analyze
1. Click **Home** in the sidebar
2. Upload your Excel file (or use `sample_dashboard_data.xlsx`)
3. Click **"Process & Go to Dashboard"**
4. View your analytics!

---

## 📁 File Requirements

Your Excel file should have these columns:

**Sheet 1: Overall RL**
| Period | RL | Remarks/information icon |
|--------|----|----|
| H1Y1 | | 140 Tickets productivity No automation |
| H2Y1 | | 160 Tickets productivity 50% automation |

**Sheet 2: Optimization Summary**
| Lever | # of Usecases | FTE |
|-------|---------------|-----|
| Elimination | | |
| Automation | | |

**Sheet 3: Recommended Tools**
| Criteria/Recommendation | Tool/Action |
|------------------------|-------------|
| P1/P2 >= 10 | CRTSIT Assist |

---

## 💡 Tips

- **Sample File**: Run `python create_sample.py` to generate example data
- **Multiple Sheets**: Upload files with multiple sheets - all will be displayed
- **Data Refresh**: Return to Home page to upload new data
- **Browser Issues**: Clear cache if charts don't display
- **Large Files**: May take a few seconds to upload and process

---

## 🎯 Dashboard Sections

| Section | Purpose | Content |
|---------|---------|---------|
| **Utilization Graphs** | Visual metrics | 3 donut charts |
| **Overall RL** | Performance data | Period-based table |
| **Optimization Summary** | Lever analysis | Lever types & counts |
| **Other Recommended Tools** | Recommendations | Tool mappings |
| **GradeWise MnM RL** | Grid reference | 7×19 empty grid |

---

## ⚙️ Configuration

**No configuration needed!** The app works out of the box.

Optional: Customize colors in `pages/02_Dashboard.py`:
```python
TEAL_START = "#2E8CA8"      # Primary color
TEAL_END = "#1F6C86"        # Gradient end
LIGHT_TEAL = "#BFE2EA"      # Accent color
```

---

## ❓ Troubleshooting

**"No data uploaded yet" warning?**
→ Go to Home page and upload an Excel file

**Charts not showing?**
→ Refresh browser (F5) and re-upload the file

**File upload fails?**
→ Ensure file is .xlsx or .xls format with headers

**App crashes on startup?**
→ Check that all packages are installed: `pip list | grep -E "streamlit|pandas|openpyxl"`

---

## 📞 Need Help?

1. Read the full README.md
2. Check terminal for error messages
3. Verify Excel file format
4. Try the sample file first

---

**Version**: 1.0 | **Last Updated**: November 26, 2025
