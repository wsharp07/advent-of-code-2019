package main

import (
	"bufio"
	"fmt"
	"os"
	"math"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("What is the mass? ")
	input, _ := reader.ReadString('\n')
	input = strings.Replace(input, "\n", "", -1)

	mass, _ := strconv.Atoi(input)

	fuelRequired := getFuelRequired(mass);
	fmt.Println("Fuel Required:", fuelRequired)
}

func getFuelRequired(mass int)  int {
	return int(math.Floor(float64(mass / 3))) - 2
}