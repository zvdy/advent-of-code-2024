package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isSafeReport(report string) bool {
	levels := parseLevels(report)
	increasing := true
	decreasing := true

	for i := 0; i < len(levels)-1; i++ {
		diff := levels[i+1] - levels[i]
		if diff < 1 || diff > 3 {
			increasing = false
		}
		if diff > -1 || diff < -3 {
			decreasing = false
		}
	}

	return increasing || decreasing
}

func canBeSafeWithRemoval(levels []int) bool {
	for i := range levels {
		modifiedLevels := append([]int{}, levels[:i]...)
		modifiedLevels = append(modifiedLevels, levels[i+1:]...)
		if isSafeReport(joinLevels(modifiedLevels)) {
			return true
		}
	}
	return false
}

func countSafeReportsPart1(data string) int {
	reports := strings.Split(strings.TrimSpace(data), "\n")
	safeCount := 0
	for _, report := range reports {
		if isSafeReport(report) {
			safeCount++
		}
	}
	return safeCount
}

func countSafeReportsPart2(data string) int {
	reports := strings.Split(strings.TrimSpace(data), "\n")
	safeCount := 0
	for _, report := range reports {
		levels := parseLevels(report)
		if isSafeReport(report) {
			safeCount++
		} else if canBeSafeWithRemoval(levels) {
			safeCount++
		}
	}
	return safeCount
}

func parseLevels(report string) []int {
	parts := strings.Fields(report)
	levels := make([]int, len(parts))
	for i, part := range parts {
		levels[i], _ = strconv.Atoi(part)
	}
	return levels
}

func joinLevels(levels []int) string {
	strLevels := make([]string, len(levels))
	for i, level := range levels {
		strLevels[i] = strconv.Itoa(level)
	}
	return strings.Join(strLevels, " ")
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var inputData string
	for scanner.Scan() {
		inputData += scanner.Text() + "\n"
	}

	part1SafeCount := countSafeReportsPart1(inputData)
	part2SafeCount := countSafeReportsPart2(inputData)

	fmt.Printf("Part 1: %d safe reports\n", part1SafeCount)
	fmt.Printf("Part 2: %d safe reports\n", part2SafeCount)
}
