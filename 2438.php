<?php
$n = trim(fgets(STDIN));
$y=1;
while($n+1!=$y)
{
    $x=$y;
    while($x>1)
    {
        print("*");
        $x=$x-1;
    }
    $y=$y+1;
    print("\n");
}
while($y>1)
{
    print("*");
    $y=$y-1;
}
//echo $y;
?>