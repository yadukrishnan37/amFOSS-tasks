
package main

import "fmt"

func prime(x int) int {
	var count int = 0
	for i := 1; i <= x; i++ {
		if x%i == 0 {
			count++
		}
	}
	if count == 2 {
		return 1
	} else {
		return 0
	}
}

func main() {
	var num int
	fmt.Println("Enter the limit: ")
	fmt.Scan(&num)

	for i := 2; i <= num; i++ {
		if prime(i) == 1 {
			fmt.Println(i)
		}
	}
}
