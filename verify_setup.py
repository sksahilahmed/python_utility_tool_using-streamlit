import os
import sys

print("=" * 60)
print("AUTOMATION DASHBOARD - SETUP VERIFICATION")
print("=" * 60)
print()

# Check required files
files_to_check = [
    ("app.py", "Main entry point"),
    ("pages/01_Home.py", "Home page"),
    ("pages/02_Dashboard.py", "Dashboard page"),
    ("sample_dashboard_data.xlsx", "Sample Excel file"),
    ("README.md", "Documentation"),
    ("QUICKSTART.md", "Quick start guide"),
]

print("📁 FILE STRUCTURE:")
all_exist = True
for file, description in files_to_check:
    exists = os.path.exists(file)
    status = "✓" if exists else "✗"
    print(f"  {status} {file:30} | {description}")
    if not exists:
        all_exist = False

print()

# Check required packages
print("📦 REQUIRED PACKAGES:")
packages = [
    ("streamlit", "Streamlit framework"),
    ("pandas", "Data processing"),
    ("openpyxl", "Excel reading"),
    ("matplotlib", "Chart generation"),
    ("numpy", "Numerical computing"),
]

all_installed = True
for package, description in packages:
    try:
        __import__(package)
        print(f"  ✓ {package:15} | {description}")
    except ImportError:
        print(f"  ✗ {package:15} | {description} - NOT INSTALLED")
        all_installed = False

print()
print("=" * 60)
print("DASHBOARD FEATURES:")
print("=" * 60)

features = [
    "Multi-page navigation (Home, Dashboard)",
    "Excel file upload & processing",
    "Real-time data preview",
    "5 dashboard sections with visualizations",
    "Teal gradient styling (#2E8CA8 → #1F6C86)",
    "Session state management",
    "Responsive 2-column + full-width layout",
    "Professional table styling",
    "Donut charts with custom colors",
]

for i, feature in enumerate(features, 1):
    print(f"  {i}. ✓ {feature}")

print()
print("=" * 60)
print("QUICK START:")
print("=" * 60)
print()
print("  1. Run the app:")
print("     streamlit run app.py")
print()
print("  2. Go to Home page (sidebar)")
print("  3. Upload Excel file (or use sample_dashboard_data.xlsx)")
print("  4. Click 'Process & Go to Dashboard'")
print("  5. View analytics in Dashboard page")
print()
print("=" * 60)

if all_exist and all_installed:
    print("✅ ALL CHECKS PASSED - SYSTEM READY!")
else:
    if not all_exist:
        print("⚠️  Some files are missing!")
    if not all_installed:
        print("⚠️  Some packages are not installed!")
        print("   Run: pip install streamlit pandas openpyxl matplotlib numpy")

print("=" * 60)
