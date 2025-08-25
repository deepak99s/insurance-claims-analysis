# claims_etl.py
import pandas as pd
from sqlalchemy import create_engine

# Extract CSV files
claims = pd.read_csv("claims.csv")
policies = pd.read_csv("policies.csv")
customers = pd.read_csv("customers.csv")
assessments = pd.read_csv("assessments.csv")

# Transform: clean dates
claims["date_of_incident"] = pd.to_datetime(claims["date_of_incident"], errors="coerce")
assessments["assessment_date"] = pd.to_datetime(assessments["assessment_date"], errors="coerce")

# Transform: standardize status & handle missing values
claims["claim_status"] = claims["claim_status"].str.strip().str.capitalize()
claims["final_payout_amount"] = claims["final_payout_amount"].fillna(0)
assessments["estimated_repair_cost"] = assessments["estimated_repair_cost"].fillna(0)

# Join all sources
df = claims.merge(policies, on="policy_id", how="left") \
           .merge(customers, on="customer_id", how="left") \
           .merge(assessments, on="claim_id", how="left")

# KPI calculations
df["time_to_assess"] = (df["assessment_date"] - df["date_of_incident"]).dt.days.fillna(0)
df["payout_discrepancy"] = df["final_payout_amount"] - df["estimated_repair_cost"]

# Load to MySQL (update username/password as needed)
engine = create_engine("mysql+mysqlconnector://root:Deepak%233512@localhost:3306/claims_db", echo=False)
df.to_sql("fact_claims_details", con=engine, if_exists="replace", index=False)

df.to_csv("fact_claims_details.csv", index=False)


print("ETL complete: Data loaded to MySQL")
