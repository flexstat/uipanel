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
    shell_exec('cp default_named_conf '.$dir_name);
    shell_exec('cp logic.py '.$dir_name);
    shell_exec('cp addinbind.py '.$dir_name);

    //shell_exec('python3 '.$dir_name.'/logic.py');
     shell_exec('cp start.php '.$dir_name);




    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
        header('Location: '.$dir_name.'/start.php');

    }
}
else {
   die('no post data to process');
}

//header('Location: panel.php');
