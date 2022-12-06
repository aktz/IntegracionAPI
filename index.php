<?php
class Database{

private $host = 'basedatos:3306';
private $user = 'root';
private $password = "integracion";
private $database = "integracionapi"; 

public function getConnection(){ 
$conn = new mysqli($this->host, $this->user, $this->password, $this->database);
if($conn->connect_error){
die("Error failed to connect to MySQL: " . $conn->connect_error);
} else {
return $conn;
}
}
}
echo "Conexión lograda para LA API REST DE INTEGRACION CONTINUA";
?>
