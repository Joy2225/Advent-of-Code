package main

import (
	"fmt"
	// "sort"
	"strings"
	"os"
	// "reflect"
	// "math"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

var print = fmt.Println

// func checkList(l []int) bool {
// 	sorted_as := make([]int, len(l))
// 	sorted_ds := make([]int, len(l))
// 	copy(sorted_as, l)
// 	copy(sorted_ds, l)
// 	sort.Ints(sorted_as)
// 	sort.Sort(sort.Reverse(sort.IntSlice(sorted_ds)))
// 	if reflect.DeepEqual(sorted_as, l) || reflect.DeepEqual(sorted_ds, l){
// 		for i:=1; i<len(l); i++{
// 			t := int64(math.Abs(float64(l[i-1]-l[i])))
// 			if !(t==1 || t==2 || t==3){
// 				return false
// 			}
// 		}
// 		return true
// 	}
// 	return false
// }

func checkList(l []int) bool {
	isAscending, isDescending := true, true

	for i := 1; i < len(l); i++ {
		diff := l[i] - l[i-1]
		if diff < -3 || diff > 3 || diff == 0 {
			return false
		}
		isAscending = isAscending && (diff > 0)
		isDescending = isDescending && (diff < 0)
	}
	return isAscending || isDescending
}

func remove_and_check(l []int) bool {
	for i:=0; i< len(l);i++{
		temp := make([]int, len(l)-1)
		copy(temp[:i], l[:i])
		copy(temp[i:], l[i+1:])
		if checkList(temp){
			return true
		}
	}
	return false
}



func main(){
	// Part 1 and Part 2
	dat, err := os.ReadFile("D2.txt")
	check(err)
	safe := 0
	data := strings.Split(strings.ReplaceAll(string(dat), "\r\n", "\n"), "\n")
	for _, line := range data{
		split_line := strings.Fields(line)
		lis := make([]int, len(split_line))
		for i, item := range(split_line){
			fmt.Sscanf(item, "%d", &lis[i])
		}
		if checkList(lis) || remove_and_check(lis){ // remove the 2nd or condition for part 1 answer
			safe+=1
		}
	}
	print(safe)
}