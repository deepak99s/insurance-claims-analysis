-- 1. Processing Efficiency: Average time_to_assess by state
SELECT 
    state,
    AVG(time_to_assess) AS avg_time_to_assess
FROM fact_claims_details
GROUP BY state
ORDER BY avg_time_to_assess;

-- 2. High-Discrepancy Claims: Top 10 with highest positive discrepancy
SELECT 
    claim_id,
    payout_discrepancy,
    customer_name,
    state
FROM fact_claims_details
WHERE payout_discrepancy > 0
ORDER BY payout_discrepancy DESC
LIMIT 10;

-- 3. Claim Status Overview: Count by status
SELECT 
    claim_status,
    COUNT(*) AS claim_count
FROM fact_claims_details
GROUP BY claim_status
ORDER BY claim_count DESC;

-- 4. Top 3 Customers by payout in each state (including ties)
WITH ranked_customers AS (
    SELECT 
        state,
        customer_name,
        SUM(final_payout_amount) AS total_payout,
        RANK() OVER (
            PARTITION BY state 
            ORDER BY SUM(final_payout_amount) DESC
        ) AS rnk
    FROM fact_claims_details
    GROUP BY state, customer_name
)
SELECT state, customer_name, total_payout
FROM ranked_customers
WHERE rnk <= 3
ORDER BY state, total_payout DESC;
