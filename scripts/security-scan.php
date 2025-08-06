<?php
// Leverages Imunify360's API
$scan_results = file_get_contents(
    "https://127.0.0.1:4083/imunify/api/scan_results.json",
    false,
    stream_context_create(["ssl" => ["verify_peer" => false]])
);

if (strpos($scan_results, 'malware_detected')) {
    mail('admin@yourdomain.co.za', 'Security Alert', $scan_results);
}
?>
