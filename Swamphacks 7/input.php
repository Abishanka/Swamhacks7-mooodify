<?php

    $input ="";
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $input = test_input($_POST['input']);
    }

   // connect to mongodb
   $m = new MongoClient();	
   echo "Connection to database successfully";

   // select a database
   $db = $m->mydb;	
   echo "Database mydb selected";

   $collection = $db->createCollection("mycol");
   echo "Collection created succsessfully"

   $document = array( 
    "title" => "User Input", 
    "input" => $input
 );
  
 $collection->insert($document);
 echo "Document inserted successfully";
?>