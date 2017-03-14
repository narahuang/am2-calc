package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	s, err := strconv.ParseFloat(os.Args[1], 32)
	e, err := strconv.ParseFloat(os.Args[2], 32)
	b, err := strconv.ParseFloat(os.Args[3], 32)
	if err != nil {
		err = nil
	}
	fmt.Println("Economy: ", s*e/100)
	fmt.Println("Business: ", s*b/200)
	fmt.Println("First: ", s*(100-e-b)/400)
}
