import argparse
def p(s, v=False):
	return [s[i_j_pair[0]:i_j_pair[1] + 1] for i_j_pair in 
			[
				[ 
					[ 
					item for seeking_palindrome_of_size in 
						range(1, len(s) + 1) 
					for item in 
						[ 
						(i_j_pair[0],i_j_pair[1]) for i_j_pair in 
							[ 
							(i, i + seeking_palindrome_of_size - 1) 
							for i in 
								range(len(s) - 1)
							if i + seeking_palindrome_of_size - 1 < len(s) 
							] 
						if palindrome_loc_holder[i_j_pair[0]][i_j_pair[1]]
						or (palindrome_loc_holder[i_j_pair[0]+1][i_j_pair[1]-1] 
							and s[i_j_pair[0]] == s[i_j_pair[1]] 
							and not palindrome_loc_holder[i_j_pair[0]].__setitem__(i_j_pair[1],True) 
							and (not v or (v and not print('Found "', s[i_j_pair[0]:i_j_pair[1] + 1],'" to be a longer palindrome of length', i_j_pair[1] + 1 - i_j_pair[0]) 
							and not print("Updated Best Palindrome Evaluation Matrix at",(i_j_pair[0],i_j_pair[1]),":") and not print_mat(palindrome_loc_holder, s)))
							) 
						or palindrome_loc_holder[i_j_pair[0]].__setitem__(i_j_pair[1],False)
						]
					] 
				for palindrome_loc_holder in
					[
						[
							[
							True if i == j 
							or (j == i + 1 and s[i] == s[j])
							and (not v or (v and not print('Initializing Palindrome Matrix at coord: ', (i, j))))
							else None 
							for j in range(len(s))
							] 
						for i in range(len(s))
						]
					] 
				if not v or (v and not print('Palindrome Array Initialized:') 
					and not print_mat(palindrome_loc_holder, s))
				][0][-1]
			]
		][0]if len(s)>1 else s



def print_mat(m, s):
	for row in range(len(m)):
		row_str = "[\t"
		for col in range(len(m[0])):
			is_palin = m[row][col]
			if is_palin is True:
				palin_substr = s[row:col + 1]
				row_str += palin_substr + '\t' if col != len(m[0]) - 1 else palin_substr + '\t]'
			elif is_palin is None:
				row_str += '.\t' if col != len(m[0]) - 1 else '.\t]'
			elif is_palin is False:
				row_str += '~\t' if col != len(m[0]) - 1 else '~\t]'
		print(row_str)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Find the longest palindromic substring within the words written into the terminal -- in only one line of code!')
	parser.add_argument('string', metavar='S', type=str, help='The input string with palindromes needing locating')
	parser.add_argument('-v',action='store_true',help='Raise this flag for verbose output')

	args = parser.parse_args()
	s = args.string
	if not s:
		raise Error('Missing argument for string to parse')
	elif args.v:
		print(p(s, True))
	else:
		print(p(s))