<?php
require '../api/db.php';

// Get weekly revenue
$result = $conn->query("SELECT SUM(amount) AS total FROM payments 
                       WHERE payment_date >= DATE_SUB(NOW(), INTERVAL 7 DAY)");
$revenue = $result->fetch_assoc()['total'];

// Transfer 70% to owner (mock FNB API)
$owner_amount = $revenue * 0.7;
$conn->query("INSERT INTO transfers (amount, account) 
             VALUES ($owner_amount, 'OWNER_FNB_ACCOUNT')");

// Log payout
file_put_contents('payout.log', date('Y-m-d')." - Paid R$owner_amount\n", FILE_APPEND);
?>
