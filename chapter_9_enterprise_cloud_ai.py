## Automate AI-Powered Follow-Ups ##
def send_followup_email(lead_name, lead_score):
    if lead_score > 80:
        return f"Sending follow-up email to {lead_name} (High Priority Lead)."
    else:
        return f"Lead {lead_name} is low priority. No follow-up needed."


# Test AI Lead Scoring
print(send_followup_email("Sarah Johnson", 85))

## Creating an AI Data Analyst in Snowflake AI ##
import snowflake.connector

conn = snowflake.connector.connect(
    user="your_username", password="your_password", account="your_account"
)
cursor = conn.cursor()
cursor.execute(
    "SELECT product_name, SUM(revenue) FROM sales_data GROUP BY product_name"
)
for row in cursor.fetchall():
    product, sales = row
    if sales > 50000:
        print(f" High Revenue Alert: {product} has exceeded $50K in sales!")
