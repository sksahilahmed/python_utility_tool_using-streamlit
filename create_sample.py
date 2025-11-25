import pandas as pd

# Create sample data for the dashboard
data_sheet1 = {
    "Period": ["H1Y1", "H2Y1", "H1Y2"],
    "RL": [0, 0, 0],
    "Remarks/information icon": [
        "140 Tickets productivity No automation",
        "160 Tickets productivity 50% automation",
        "160 Tickets productivity, 100% Automation + Left Shift"
    ]
}

data_sheet2 = {
    "Lever": ["Elimination", "Automation", "Standard Automation", "Agentic AI", "Left Shift"],
    "# of Usecases": [0, 0, 0, 0, 0],
    "FTE": [0, 0, 0, 0, 0]
}

data_sheet3 = {
    "Criteria/Recommendation": ["P1/P2 >= 10", "FLR <30%", "Triaging Effort >1 FTE", "Service Improvement Recommendation", "ServiceNow Performance Analytics"],
    "Tool/Action": ["CRTSIT Assist", "SOP Genius Recommended", "Auto Ticket Triaging", "Ticket Quality Audit Tool", ""]
}

# Create Excel file
with pd.ExcelWriter("sample_dashboard_data.xlsx", engine='openpyxl') as writer:
    pd.DataFrame(data_sheet1).to_excel(writer, sheet_name="Overall RL", index=False)
    pd.DataFrame(data_sheet2).to_excel(writer, sheet_name="Optimization Summary", index=False)
    pd.DataFrame(data_sheet3).to_excel(writer, sheet_name="Recommended Tools", index=False)

print("✓ Sample Excel file created: sample_dashboard_data.xlsx")
