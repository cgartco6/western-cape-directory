<?php
$conn = new mysqli(
    "localhost", 
    "silver_db_user",  // Dedicated DB user
    "ComplexP@ssw0rd!", // Stronger password
    "wc_business",
    3306,
    "/var/lib/mysql/mysql.sock"  // Unix socket for faster connections
);

// Enable persistent connections
$conn->options(MYSQLI_OPT_CONNECT_TIMEOUT, 10);
$conn->options(MYSQLI_OPT_READ_TIMEOUT, 30);
?>
