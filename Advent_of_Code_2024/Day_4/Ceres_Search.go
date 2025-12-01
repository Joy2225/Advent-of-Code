package main

import (
	"fmt"
	"os"
	"strings"
	"regexp"
)

// Part 1
func check(e error){
	if e != nil {
		panic(e)
	}
}

var print = fmt.Println
var r1 = regexp.MustCompile("XMAS")
var r2 = regexp.MustCompile("SAMX")

func check_xmas(a string) int{
	return len(append(r1.FindAllString(a, -1), r2.FindAllString(a, -1)...))
}

func check_x_mas(data []string, i int, j int) bool{
	return ((data[i-1][j-1]=='M' && data[i+1][j+1]=='S') || (data[i-1][j-1]=='S' && data[i+1][j+1]=='M')) && ((data[i-1][j+1]=='M' && data[i+1][j-1]=='S') || (data[i-1][j+1]=='S' && data[i+1][j-1]=='M'))
}

func main() {
	// Part 1
	total := 0
	dat, err := os.ReadFile("D4.txt")
	check(err)
	data := strings.Split(strings.ReplaceAll(string(dat), "\r\n", "\n"), "\n")
	for _, val:= range data {
		total += check_xmas(val)
	}
	top_down := make([]string, len(data[0]))
	for j:=0; j<len(data[0]); j++{
		for i:=0; i<len(data); i++{
			top_down[j] += string(data[i][j])
		}
	}
	for _, val:= range top_down {
		total += check_xmas(val)
	}
	tl_br := make([]string, 0)
	for i:=0; i<len(data)-3; i++{
		for j:=0; j<len(data[i])-3; j++{
			temp := ""
			for k:=0; k<4; k++{
				temp += string(data[i+k][j+k])
			}
			tl_br = append(tl_br, temp)
		}
	}
	for _, val:= range tl_br {
		total += check_xmas(val)
	}
	tr_bl := make([]string, 0)
	for i:=0; i<len(data)-3; i++{
		for j:=len(data[i])-1; j>=3; j--{
			temp := ""
			for k:=0; k<4; k++{
				temp += string(data[i+k][j-k])
			}
			tr_bl = append(tr_bl, temp)
		}
	}
	for _, val:= range tr_bl {
		total += check_xmas(val)
	}
	print(total)

	// Part 2
	total = 0
	for i:=1; i<len(data)-1; i++{
		for j:=1; j<len(data[i])-1; j++{
			if data[i][j] == 'A' && check_x_mas(data, i, j){
				total++
			}
		}
	}
	print(total)
}