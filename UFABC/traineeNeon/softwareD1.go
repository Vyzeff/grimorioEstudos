// feito como o 1 desafio dos trainees da UFABC NEON em 2023
// me baseei nas seguintes fontes:
// https://www.geeksforgeeks.org/8-queen-problem/
// https://iq.opengenus.org/8-queens-problem-backtracking/
// https://stackoverflow.com/questions/2894443/8-queens-algorithm-example

package main

import (
	"fmt"
	"strings"
)

var isQueen [8][8] bool
var canAttack [8][8] int
var solNo int

// tries to place queen on both the queen and attack board
func tryQueen(i, j int) {
	isQueen[i][j] = true
	// change attack board acordingly
	// row
	for x := 0; x < 8; x++ {
		canAttack[i][x]++
	}
	// col
	for y := 0; y < 8; y++ {
		canAttack[y][j]++
	}
	// since the pos[i][j] is + twice, remove 2
	canAttack[i][j] -= 2  

	// diagonals
	for x := 0; x < 8; x++ {
		for y := 0; y < 8; y++ {
			// if on top of the place queen is placed, ++
			if x == i && y == j {
				canAttack[x][y]++
				continue
			}
			// diagonal calc
			if x-i == y-j || x-i == -(y-j) {
				canAttack[x][y]++
			}
		}
	}
}

// same stuff as above, just subtract instead of adding
func deleteQueen(i, j int) {
	isQueen[i][j] = false
	// change attack board acordingly
	// row
	for x := 0; x < 8; x++ {
		canAttack[i][x]--
	}
	// col
	for y := 0; y < 8; y++ {
		canAttack[y][j]--
	}
	// since the pos[i][j] is - twice, add 2
	canAttack[i][j] += 2 

	// diagonals
	for x := 0; x < 8; x++ {
		for y := 0; y < 8; y++ {
			// if on top of the place queen is placed, --
			if x == i && y == j {
				canAttack[x][y]--
				continue
			}
			// diagonal calc
			if x-i == y-j || x-i == -(y-j) {
				canAttack[x][y]--
			}
		}
	}
}


func queenqueenSolver(x int) {
	if x == 7 {
		// last row, check if can place wheen anywhere
		for y, cnt := range canAttack[7] {
			if cnt == 0 {
				tryQueen(x, y)
				solNo++
				fmt.Println("Solution No.", solNo)
				printAll(isQueen)
				deleteQueen(x, y)
			}
		}

	} else {
		for y, cnt := range canAttack[x] {
			if cnt == 0 {
				tryQueen(x, y)
				// continue to solve until 7th row
				queenqueenSolver(x + 1)
				// remove this and all queens, backtrack
				deleteQueen(x, y)
			}
		}
	}
}

// just prints the board
func printAll(data [8][8]bool) {
fmt.Println("    A B C D E F G H")
fmt.Println("  -----------------")
for i := 0; i < 8; i++ {
	row := make([]string, 8)
	for j := 0; j < 8; j++ {
		if data[i][j] {
			row[j] = "Q"
		} else {
			row[j] = "+"
		
		}
	}
	fmt.Print((i+1), " | ")
	fmt.Println(strings.Join(row, " "))
}
}

func main() {
	queenqueenSolver(0)
}