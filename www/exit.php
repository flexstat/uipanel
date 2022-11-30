<?php 
session_start();
unset($_SESSION['user_id']);
//setcookie('user', $user['name'], time() - 3600, "/");
header('Location: /');

 ?>
