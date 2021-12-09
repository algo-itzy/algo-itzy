// git commit -m "code: Solve boj 01629 곱셈 (yoonbaek)"
package main

import (
	"fmt"
)

var a, b, c int

func fastPow(x, y int) int {
	if y == 1 {
		return x % c
	}
	fp := fastPow(x, y/2) % c
	if y%2 == 0 {
		return fp * fp % c
	}
	return fp * fp % c * x % c
}

func main() {
	fmt.Scanf("%d %d %d\n", &a, &b, &c)
	fmt.Println(fastPow(a, b))
}
