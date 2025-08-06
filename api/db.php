<?php
$host = "localhost";
$user = "afrihost_username";
$pass = "afrihost_password";
$db = "afrihost_dbname";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
