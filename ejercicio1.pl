#!/usr/bin/perl

#Ejercicio1.pl
#citlalli Limpens

$A = "A";
$T = "T";
$C = "C";
$G = "G";
@dna = ("A", "A", "A", "A",);
$n = 1;

sub pos1 {
    if ($dna[3] == $A) {
        print "$n\t@dna\n";
        $n++;
        $dna[3] = $T;
        print "$n\t@dna\n";
    }
    if ($dna[3] == $T) {
        print "$n\t@dna\n";
        $n++;
        $dna[3] = $C;
        print "$n\t@dna\n";
    }
    if ($dna[3] == $C) {
        print "$n\t@dna\n";
        $n++;
        $dna[3] = $G;
        print "$n\t@dna\n";
    }
    $n++
}

sub pos2 {
    pos1;
    if ($dna[0] == $A, $dna[1] == $A, $dna[2] == $A, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $C;
        pos1;
    }
    if ($dna[0] == $A, $dna[1] == $A, $dna[2] == $A, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $G;
        pos1;
    }
    if ($dna[0] == $A, $dna[1] == $A, $dna[2] == $A, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $T;
        pos1;
    }
}

sub pos3 {
    pos2;
    if ($dna[0] == $A, $dna[1] == $A, $dna[2] == $T, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $A;
        $dna[1] = $C;
        pos2;
    }
    if ($dna[0] == $A, $dna[1] == $C, $dna[2] == $T, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $A;
        $dna[1] = $G;
        pos2;
    }
    if ($dna[0] == $A, $dna[1] == $G, $dna[2] == $T, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $A;
        $dna[1] = $T;
        pos2;
    }
}

sub pos4 {
    pos3;
    if ($dna[0] == $A, $dna[1] == $T, $dna[2] == $T, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $A;
        $dna[1] = $A;
        $dna[0] = $C;
        pos3;
    }
    if ($dna[0] == $C, $dna[1] == $T, $dna[2] == $T, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $A;
        $dna[1] = $A;
        $dna[0] = $G;
        pos3;
    }
    if ($dna[0] == $G, $dna[1] == $T, $dna[2] == $T, $dna[3] == $T) {
        $dna[3] = $A;
        $dna[2] = $A;
        $dna[1] = $A;
        $dna[0] = $T;
        pos3;
    }

    
