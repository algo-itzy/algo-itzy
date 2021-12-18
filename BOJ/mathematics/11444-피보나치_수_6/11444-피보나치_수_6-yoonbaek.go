// git commit -m "code: Solve boj 11444 피보나치 수 6 (yoonbaek)"
package main

import "fmt"

const (
	size int = 2
	div  int = 1000000007
)

var (
	unit = [size][size]int{
		{1, 1},
		{1, 0},
	}
)

func main() {
	n := 0
	fmt.Scanf("%d", &n)
	fmt.Println(fastFib(n)[1][0])
}

func fastFib(n int) [size][size]int {
	if n == 1 {
		return unit
	}
	ff := fastFib(n / 2)
	if n%2 == 0 {
		return matSquare(ff, ff)
	}
	return matSquare(matSquare(ff, ff), unit)
}

func matSquare(a, b [size][size]int) [size][size]int {
	res := [size][size]int{}
	for row := range a {
		for col := range a {
			for k := range a {
				res[row][col] += (a[row][k] * b[k][col])
			}
			res[row][col] %= div
		}
	}
	return res
}
