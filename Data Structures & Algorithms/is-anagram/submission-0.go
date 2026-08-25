func isAnagram(s string, t string) bool {
	// counter on both incrementing and then check counters

	counter1 := make(map[string]int)
	counter2 := make(map[string]int)

	if len(s) != len(t)	{return false}

	for i:=0; i < len(s); i++ {
		counter1[string(s[i])]++
		counter2[string(t[i])]++
	}

	for k, v := range counter1{
		if counter2[k] != v {return false}
	}

	return true
}
