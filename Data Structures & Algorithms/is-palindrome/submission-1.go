func isPalindrome(s string) bool {

	sr := []rune(strings.ToLower(s))


	for i, j := 0, len(sr)-1; i != j; {
		for i < j && !unicode.IsLetter(sr[i]) && !unicode.IsDigit(sr[i]){
			i++
		}
		for i < j && !unicode.IsLetter(sr[j]) && !unicode.IsDigit(sr[j]){
			j--
		}

		fmt.Println("i, j")
		fmt.Println(i, j, string(sr[i]), string(sr[j]))

		if j-i <= 1 && sr[j] == sr[i]{
			break
		}

		if sr[i] != sr[j]{
			return false
		}
		i++
		j--
	}

	return true

}
