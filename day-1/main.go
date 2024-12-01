package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func calculateTotalDistance(leftList, rightList []int) int {
	// Sort both lists
	sort.Ints(leftList)
	sort.Ints(rightList)

	// Calculate the total distance
	totalDistance := 0
	for i := range leftList {
		totalDistance += abs(leftList[i] - rightList[i])
	}

	return totalDistance
}

func calculateSimilarityScore(leftList, rightList []int) int {
	// Count the occurrences of each number in the right list
	rightCount := make(map[int]int)
	for _, num := range rightList {
		rightCount[num]++
	}

	// Calculate the similarity score
	similarityScore := 0
	for _, num := range leftList {
		similarityScore += num * rightCount[num]
	}

	return similarityScore
}

func readInputFile(filePath string) ([]int, []int, error) {
	leftList := []int{}
	rightList := []int{}

	file, err := os.Open(filePath)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		left, err := strconv.Atoi(parts[0])
		if err != nil {
			return nil, nil, err
		}
		right, err := strconv.Atoi(parts[1])
		if err != nil {
			return nil, nil, err
		}
		leftList = append(leftList, left)
		rightList = append(rightList, right)
	}

	if err := scanner.Err(); err != nil {
		return nil, nil, err
	}

	return leftList, rightList, nil
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	// Read the input file
	leftList, rightList, err := readInputFile("input.txt")
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	// Calculate the total distance
	totalDistance := calculateTotalDistance(leftList, rightList)
	fmt.Printf("Total distance: %d\n", totalDistance)

	// Calculate the similarity score
	similarityScore := calculateSimilarityScore(leftList, rightList)
	fmt.Printf("Similarity score: %d\n", similarityScore)
}
