import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_financial_data(raw_text):
    prompt = f"""You are a senior real estate accountant. Analyze the following financial report text and extract:
- Document Type (e.g. Actual, Budget)
- Period (e.g. March 2025)
- Rental Income
- Laundry/Vending Income
- Parking Income
- Other Revenue
- Total Revenue
- Repairs & Maintenance
- Utilities
- Property Management Fees
- Property Taxes
- Insurance
- Admin/Office Costs
- Marketing/Advertising
- Total Expenses
- Net Operating Income (NOI)

Text:
""" + raw_text + """

Return this in JSON format.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return {"error": str(e)}
