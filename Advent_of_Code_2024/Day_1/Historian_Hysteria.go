package main

import (
	"fmt"
    "os"
	"strings"
	"slices"
	"math"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

var print = fmt.Println

func makeDict(data []int) map[int]int {
    c := make(map[int]int)
    for _, item := range data {
        c[item]++
    }
    return c
}


func main() {
	// Part 1
	dat, err := os.ReadFile("D1.txt")
	check(err)
	var data string = string(dat)
	var lines = strings.Split(strings.ReplaceAll(data, "\r\n", "\n"), "\n")
	a := make([]int, len(lines))
	b := make([]int, len(lines))
	for i, line := range lines {
		fmt.Sscanf(strings.Fields(line)[0], "%d", &a[i])
		fmt.Sscanf(strings.Fields(line)[1], "%d", &b[i])
	}
	slices.Sort(a)
	slices.Sort(b)
	var sum int =0
	for i:=0; i<len(a); i++{
		sum += int(math.Abs(float64(a[i]-b[i])))
	}
	print(sum)

	// Part 2
	d1 := makeDict(a)
	d2 := makeDict(b)
	var sum2 int =0
	for i:= range d1{
		if val, exist := d2[i]; exist{
			sum2 += int(val*i*d1[i])
		}
	}
	print(sum2)
}