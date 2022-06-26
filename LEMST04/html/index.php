<?php
   echo "<h1 align='center'>Kittiphum 621998004</h1><br/>";
   $servername = "db";
   $username = "devops";
   $password = "devops101";

   $dbhandle = mysqli_connect($servername, $username, $password);
   $selected = mysqli_select_db($dbhandle, "titanic");

   echo "<h2 align='center'>Connected database server></h2><br/>";
   echo "<h2 align='center'>Selected database</h2><br/>";
   phpinfo();
?>
