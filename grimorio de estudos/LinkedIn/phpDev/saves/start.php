<?php
class Person {
    var $first_name;
    var $last_name;

    function __construct( $fn, $ln ) {
        $this->first_name = $fn;
        $this->last_name = $ln;
    }

    public function get_first_name() {
        return $this->first_name;
    }

    public function get_last_name() {
        return $this->last_name;
    }
}

// Challenge: Sort this array of Person objects by last, then first name! 

$rob = new Person( 'Rob', 'Casabona' );
$joe = new Person( 'Joe', 'Casabona' );
$erin = new Person( 'Erin', 'Casabona' );
$steve = new Person( 'Steve', 'Wozniack' );
$bill = new Person( 'Bill', 'Gates' );
$walt = new Person( 'Walt', 'Disney' );
$bob = new Person( 'Bob', 'Iger' );

$people = array( $rob, $joe, $erin, $steve, $bill, $walt, $bob );

function sortPeople($array) {
    $lastArray = array();
    $firstArray = array();
    foreach ($array as $val) {
        $lastArray[] = $val->get_last_name();
        $firstArray[] = $val->get_first_name();
    };
    asort($lastArray);
    asort($firstArray);
    foreach ($lastArray as $name) {
        echo "$name <br>";
    };
    
};

sortPeople($people)
?>