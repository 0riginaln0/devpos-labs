package one_two_three

import "core:fmt"
import "core:time"

main :: proc() {
	secounds_of_sleep := 1 * time.Second
	for i in 1 ..= 60 {
		fmt.println(i)
		time.sleep(secounds_of_sleep)
	}
}
