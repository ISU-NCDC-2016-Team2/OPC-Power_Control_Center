<?php

$var = escapeshellarg($_GET['var']);
$value = escapeshellarg($_GET['value']);

exec(escapeshellcmd("python py-bin/opc_put_values.py ".$var." ".$value." 2>&1"), $output, $return_var);

?>
