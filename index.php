<?php

// comita ou não comita... de novo!
function generateHash($password) {
    if (defined("CRYPT_BLOWFISH") && CRYPT_BLOWFISH) {
        $salt = '$2y$11$' . substr(md5(uniqid(rand(), true)), 0, 22);
        return crypt($password, $salt);
    }
}

function verify($password, $hashedPassword) {
    return crypt($password, $hashedPassword) == $hashedPassword;
}

$password = "Aa1@aa";
$hashpass = generateHash($password);

//echo $hashpass."<br>";

function pass_check($pass){
	$pattern = '/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/';
	return preg_match($pattern, $pass);
}


if(pass_check("@#$%&6rP"))
	echo "incredible... it works!";
else 
    echo "something goes wrong...";