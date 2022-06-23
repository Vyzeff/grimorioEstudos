<?php

$numbers = array();
$x = 0;
$y = 0;
$z = 0;
$limit = 200;
do {

    if ( $x == 0 ) {
        $x = 1;
        echo "<p>We begin with <em>$x</em></p>";
        $numbers[] = $x;
    } elseif ( $y == 0 ) {
        $y = $x;
        echo "<p>The sum of $y and $z is <em>$x</em></p>";
        $numbers[] = $x;
    } else {
        $y = $numbers[(sizeof($numbers) - 1)];
        $z = $numbers[(sizeof($numbers) - 2)];
        $x = $y + $z;
        echo "<p>The sum of $y and $z is <em>$x</em></p>";
        $numbers[] = $x;
    }
} while ( $x <= $limit);

// 1° arquivo que eu consegui fazer rodar no apache com o php sendo lido
?>