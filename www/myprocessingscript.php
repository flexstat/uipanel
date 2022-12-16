<?php
session_start();

$dir_name = $_SESSION['user_id'];


$root = $_SERVER["DOCUMENT_ROOT"];
$dir = $root . '/'. $dir_name .'/';

if( !file_exists($dir) ) {
    mkdir($dir, 0777, true);
}

if(isset($_POST['field1']) && isset($_POST['field2'])) {
    $data = $_POST['field1'] . ';' . $_POST['field2'] . ';' . $dir_name . "\r\n";
    $ret = file_put_contents($dir . '/userdata', $data,  LOCK_EX);
    shell_exec('cp conf_default '.$dir_name);
    shell_exec('cp default_named_conf_zone_ru '.$dir_name);
    shell_exec('cp default_named_conf_zone_de '.$dir_name);
    shell_exec('cp logic.py '.$dir_name);
    shell_exec('cp addinbind.py '.$dir_name);
    shell_exec('cp ddos_confg '.$dir_name);
    shell_exec('cp addinddos.py '.$dir_name);


    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
        //header('Location: '.$dir_name.'/start.php');
        // shell_exec('php '.$dir_name.'/start.php');
         shell_exec('/usr/bin/python3.5 super/logic.py');
         echo $dir_name;

    }
}
else {
   die('no post data to process');
}

//header('Location: panel.php');
