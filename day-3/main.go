package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
)

func parseInput(inputText string, part int) int {
	// Regular expression to find valid mul instructions
	mulPattern := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	// Regular expression to find do and don't instructions
	controlPattern := regexp.MustCompile(`\b(do|don't)\(\)`)

	// Split the input text into tokens
	tokens := regexp.MustCompile(`(\bdo\(\)|\bdon't\(\)|mul\(\d+,\d+\))`).FindAllString(inputText, -1)

	enabled := true
	totalSum := 0

	for _, token := range tokens {
		if part == 2 && controlPattern.MatchString(token) {
			if token == "do()" {
				enabled = true
				fmt.Println("do() found, enabling mul instructions")
			} else if token == "don't()" {
				enabled = false
				fmt.Println("don't() found, disabling mul instructions")
			}
		} else if mulPattern.MatchString(token) {
			matches := mulPattern.FindStringSubmatch(token)
			x, _ := strconv.Atoi(matches[1])
			y, _ := strconv.Atoi(matches[2])
			if part == 1 || (part == 2 && enabled) {
				totalSum += x * y
				fmt.Printf("mul(%d,%d) found, current sum: %d\n", x, y, totalSum)
			} else {
				fmt.Printf("mul(%d,%d) found but ignored due to don't()\n", x, y)
			}
		}
	}

	return totalSum
}

func main() {
	// Read the input file
	inputBytes, err := ioutil.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}
	inputText := string(inputBytes)

	// Calculate the result for part 1
	fmt.Println("Executing Part 1")
	resultPart1 := parseInput(inputText, 1)
	fmt.Printf("Part 1 result: %d\n", resultPart1)

	// Calculate the result for part 2
	fmt.Println("\nExecuting Part 2")
	resultPart2 := parseInput(inputText, 2)
	fmt.Printf("Part 2 result: %d\n", resultPart2)
}
