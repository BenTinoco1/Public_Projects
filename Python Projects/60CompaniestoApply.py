import pandas as pd

# Data for the Excel sheet
data = {
    "Company": [
        "Google", "Amazon", "Microsoft", "Apple", "Meta (Facebook)",
        "Oracle", "Salesforce", "SAP", "IBM", "Adobe", "Twitter (X)", "Uber", "Tesla", "Airbnb",
        "McKinsey & Company", "Boston Consulting Group (BCG)", "Bain & Company", "Deloitte", "PwC", "EY (Ernst & Young)", "Accenture", "KPMG",
        "Citibank (Banamex)", "BBVA", "Santander", "HSBC", "JPMorgan Chase", "Goldman Sachs", "Morgan Stanley",
        "Workday", "ServiceNow", "Snowflake", "NetSuite", "Informatica",
        "Stripe", "Square", "Atlassian", "Datadog", "HubSpot", "Twilio", "MongoDB", "Cloudflare", "Okta", "Palantir", "Slack",
        "Bank of America", "Wells Fargo", "Capital One", "American Express", "Scotiabank", "BlackRock", "Fidelity",
        "Infosys", "Cognizant", "HCL Technologies", "Capgemini", "Genpact",
        "Mercado Libre", "Rappi", "Bitso", "Kavak", "Clip"
    ],
    "Tier": [
        "GAFAM", "GAFAM", "GAFAM", "GAFAM", "GAFAM",
        "Ex-Employer", "Tier 2 Tech", "Tier 2 Tech", "Tier 2 Tech", "Tier 2 Tech", "Tier 2 Tech", "Tier 2 Tech", "Tier 2 Tech", "Tier 2 Tech",
        "Consulting", "Consulting", "Consulting", "Consulting", "Consulting", "Consulting", "Consulting", "Consulting",
        "Bank", "Bank", "Bank", "Bank", "Bank", "Bank", "Bank",
        "Ex-Employer", "Ex-Employer", "Ex-Employer", "Ex-Employer", "Ex-Employer",
        "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup", "Tech Startup",
        "Bank", "Bank", "Bank", "Bank", "Bank", "Bank", "Bank",
        "Consulting", "Consulting", "Consulting", "Consulting", "Consulting",
        "Regional Tech", "Regional Tech", "Regional Tech", "Regional Tech", "Regional Tech"
    ],
    "Potential Fit (%)": [
        95, 90, 85, 80, 80,
        95, 85, 80, 85, 75, 70, 75, 70, 65,
        80, 80, 75, 90, 90, 90, 85, 85,
        85, 80, 80, 80, 75, 70, 70,
        80, 80, 75, 85, 80,
        80, 75, 75, 70, 70, 70, 70, 65, 65, 60, 60,
        85, 80, 75, 75, 70, 70, 70,
        75, 75, 70, 70, 70,
        75, 70, 65, 65, 60
    ],
    "Success Rate (%)": [
        20, 20, 15, 10, 10,
        30, 15, 10, 15, 10, 10, 10, 10, 5,
        15, 15, 10, 20, 20, 20, 15, 15,
        15, 10, 10, 10, 10, 10, 10,
        15, 10, 10, 15, 10,
        10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        15, 15, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10,
        10, 10, 10, 10, 5
    ],
    "Comments": [
        "Strong BI alignment, referral improves odds.", "Data-driven roles like BI, Data Analyst, or AWS-aligned roles fit well.",
        "Look for Power BI roles or BI Engineering in Azure.", "BI or technical support analytics roles.", "Focus on technical BI roles or global operations.",
        "Returning to Oracle in a different team or senior role is a strong option.", "BI or data engineering roles supporting CRM platforms.",
        "Analytics and BI roles focusing on enterprise resource planning solutions.", "Look for data analytics or cloud roles tied to IBM Cloud.",
        "Business intelligence roles analyzing product or marketing data.", "Focus on operational data analysis roles.", "Strong alignment with BI or market analytics for LATAM.",
        "Target roles in supply chain analytics or operational intelligence.", "Data-related roles in customer experience or operations.",
        "Business Intelligence Analyst or Operations Analytics.", "Target data-driven consulting roles in Mexico.", "Focus on strategy-related analytics roles.",
        "BI and data visualization roles; large Mexico presence.", "Data analytics for financial and operational projects.",
        "Business intelligence within finance or risk consulting teams.", "Cloud and analytics roles in LATAM.", "Business analytics roles; solid presence in Mexico.",
        "BI or risk analytics roles in Mexico.", "Strong focus on BI for LATAM operations.", "BI roles in risk, operations, and finance teams.",
        "Target data analysis or digital transformation teams.", "Opportunities in operations or investment analytics.", "Data-driven roles in compliance or risk analytics.",
        "BI and data analytics for operations or investment insights.", "BI roles supporting HR and financial planning tools.",
        "Focus on operational data visualization.", "Opportunities in cloud data warehousing.", "Transition to cloud-based BI solutions.",
        "Data engineering and BI integration tools.", "Fast-growing startups with strong BI needs.", "Strong BI roles in LATAM market.", "Look for technical and operational data analysis roles.",
        "Target roles in analytics and process automation.", "Opportunities in global tech markets.", "Focus on data visualization and process improvements.",
        "Look for roles in predictive analytics.", "Strong focus on operational analytics.", "Growing interest in BI for LATAM markets.",
        "Opportunities in scalable data platforms.", "Target operational intelligence roles.", "Focus on predictive analytics and cloud-based operations.",
        "Growing focus on BI and operational insights.", "Data analytics or BI-related roles in LATAM.", "Look for opportunities in fintech or financial operations.",
        "Focus on predictive analytics.", "Operational analytics and decision-making roles.", "Growing fintech focus in LATAM.", "Strong analytics focus.",
        "Focus on operations and analytics.", "Growing opportunities in BI for LATAM market.", "Expand comments here if needed for equal length.",
        "", "", "", "", ""
    ]
}

# Ensure all lists in the dictionary are of the same length
max_length = max(len(lst) for lst in data.values())
for key in data:
    if len(data[key]) < max_length:
        data[key].extend([""] * (max_length - len(data[key])))

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
file_path = "Top_100_Companies_Job_Target_List.xlsx"
df.to_excel(file_path, index=False)

print(f"Excel file saved as '{file_path}'.")
