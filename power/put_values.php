<?php

$var = $_GET['var'];
$value = $_GET['value'];

exec(escapeshellcmd("python py-bin/opc_put_values.py ".$var." ".$value." 2>>../error_log"), $output, $return_var);

?>
