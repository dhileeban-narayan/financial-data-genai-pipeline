import os
import json
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

class DataQualityReport(BaseModel):
    status: str = Field(description="Must be either 'PASS' or 'FAIL'")
    anomalies_detected: bool = Field(description="True if any anomalies were found, otherwise False")
    issues_list: list[str] = Field(description="List of specific anomalies found in the data, empty if none")
    recommended_action: str = Field(description="Suggested next steps (e.g., 'Proceed to downstream BI', 'Halt pipeline and alert on-call')")

def run_dq_agent(metadata: dict) -> DataQualityReport:
    client = genai.Client()
    
    prompt = f"""
    You are an Enterprise Data Governance Agent. Review the following daily data load metadata. 
    Flag any anomalies, such as significant row count drops, high null percentages, 
    or extreme price standard deviations (e.g., drops exceeding 20%).
    
    Data Load Metadata:
    {json.dumps(metadata, indent=2)}
    """
    
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=DataQualityReport,
        ),
    )
    return DataQualityReport.model_validate_json(response.text)

if __name__ == "__main__":
    daily_metadata = {
        "table_name": "fact_daily_price_actions",
        "expected_row_count": 5000,
        "actual_rows_processed": 450,           
        "null_close_price_percentage": 12.5,    
        "max_price_drop_percentage": 22.1,      
    }
    
    print("Agent is reviewing pipeline metadata...")
    try:
        report = run_dq_agent(daily_metadata)
        print("\n--- 🤖 Data Quality Agent Report ---")
        print(f"Status:             {report.status}")
        print(f"Anomalies Detected: {report.anomalies_detected}")
        print(f"Issues Found:       {report.issues_list}")
        print(f"Recommended Action: {report.recommended_action}")
    except Exception as e:
        print(f"\nError running agent: {e}")
        print("Please ensure your GOOGLE_API_KEY environment variable is set.")