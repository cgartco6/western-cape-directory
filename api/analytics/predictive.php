// api/analytics/predictive.php
$stmt = $conn->prepare("
    SELECT 
        DATE(payment_date) AS day,
        SUM(amount) AS revenue
    FROM payments
    GROUP BY day
    ORDER BY day DESC
    LIMIT 90
");
// Uses 3 months data for ML predictions
