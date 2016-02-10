<?php

$var = $_GET['var'];
$value = $_GET['value'];

exec(escapeshellcmd("python py-bin/opc_put_values.py ".$var." ".$value." >>/tmp/error_log 2>&1"), $output, $return_var);

?>
