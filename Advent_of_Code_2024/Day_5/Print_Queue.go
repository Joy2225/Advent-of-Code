package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func check(e error){
	if e != nil{
		panic(e)
	}
}

var print = fmt.Println

func contains(slice []int, element int) bool {
    for _, v := range slice {
        if v == element {
            return true
        }
    }
    return false
}

func check_pages(line []int, dic map[int][]int) bool{
	for i := 0; i < len(line)-1; i++{
		for j := i+1; j<len(line); j++{
			if _, ok := dic[line[i]]; ok{
				if contains(dic[line[i]], line[j]){
					continue
				}else{
					if contains(dic[line[j]], line[i]){
						return false
					}
				}
			}else{
				if _, ok := dic[line[j]]; ok{
					if contains(dic[line[j]], line[i]){
						return false
					}
				}
			}
			
		}
	}
	return true
}

func find_wrong(wrong []int, dic map[int][]int) []int{
	for i := 0; i < len(wrong)-1; i++{
		for j := i+1; j < len(wrong); j++{
			if _, ok := dic[wrong[i]]; ok{
				if contains(dic[wrong[i]], wrong[j]){
					continue
				}else{
					if contains(dic[wrong[j]], wrong[i]){
						wrong[i], wrong[j] = wrong[j], wrong[i]
						if check_pages(wrong, dic){
							return wrong
						}else{
							return find_wrong(wrong, dic)
						}
					}
				}
			}else{
				if _, ok := dic[wrong[j]]; ok{
					if contains(dic[wrong[j]], wrong[i]){
						wrong[i], wrong[j] = wrong[j], wrong[i]
						if check_pages(wrong, dic){
							return wrong
						}else{
							return find_wrong(wrong, dic)
						}
					}
				}
			}
		}
	}
	return wrong
}

func main(){
	dat, err := os.ReadFile("D5.txt")
	check(err)
	data := strings.Split(strings.ReplaceAll(string(dat), "\r\n", "\n"), "\n\n")
	page_com := strings.Split(data[0], "\n")
	pages := make([][]int, 0)
	for _, val := range strings.Split(data[1], "\n"){
		temp_int := make([]int, 0)
		for _, val := range strings.Split(val, ","){
			a := 0
			fmt.Sscanf(val, "%d", &a)
			temp_int = append(temp_int, a)
		}
		pages = append(pages, temp_int)
	}
	dic := make(map[int][]int)
	for _, val := range page_com{
		key, _ := strconv.Atoi(val[:2])
		content, _ := strconv.Atoi(val[3:])
		dic[key] = append(dic[key], content)

	}
	total := 0
	wrong := make([][]int, 0)
	for _, val := range pages{
		if check_pages(val, dic){
			total+= val[len(val)/2]
		}else{
			wrong = append(wrong, val)
		}
	}
	print(total)

	total = 0
	for _, val := range wrong{
		temp := find_wrong(val, dic)
		total+= temp[len(temp)/2]
	}
	print(total)
}