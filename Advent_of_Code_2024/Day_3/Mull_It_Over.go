package main

import (
	"fmt"
	"regexp"
	"os"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

var print = fmt.Println

func main(){
	// Part 1
	dat, err := os.ReadFile("D3.txt")
	check(err)
	var data string = string(dat)
	r := regexp.MustCompile(`mul\(([0-9]+),([0-9]+)\)`)
	matches := r.FindAllStringSubmatch(data, -1)
	sum := 0
	for _, lis := range matches{
		a, b := 0, 0
		fmt.Sscanf(lis[1], "%d", &a)
		fmt.Sscanf(lis[2], "%d", &b)
		sum += a*b
	}
	print(sum)

	// Part 2
	r1 := regexp.MustCompile(`mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)`)
	matches1 := r1.FindAllString(data, -1)
	// print(matches1)
	t := 0
	sum1 := 0
	patt := regexp.MustCompile(`mul\(([0-9]+),([0-9]+)\)`)
	for _, lis:=range matches1{
		if lis == "don't()"{
			t=1
			continue
		} else if lis == "do()"{
			t=0
			continue
		} else {
			if t==0{
				temp := patt.FindAllStringSubmatch(lis, -1)
				a, b := 0, 0
				fmt.Sscanf(temp[0][1], "%d", &a)
				fmt.Sscanf(temp[0][2], "%d", &b)
				sum1 += a*b
			}
		}
	}
	print(sum1)
}