# Function for creating the playfair key matrix
def playfairKeyMatrix(key):
	# Remove duplicates and treat 'i' and 'j' as the same letter
	key = key.replace("j", "i")
	# Mark a letter if it has been used in the keyword
	seen = set()
	# Create an array to store the key matrix
	key_matrix = []
	# Add letters in the matrix that are in the keyword
	for char in key:
		if char not in seen and char.isalpha():
			seen.add(char)
			key_matrix.append(char)
	# Add the rest of the alphabet to the matrix
	alphabet = "abcdefghiklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in seen:
			key_matrix.append(char)
	# Convert the key into a 5x5 matrix
	return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

# Function for determining the row and column of a letter in the key matrix
def findPosition(matrix, char):
	# For loop to find the position of the letter in the key matrix
	for row in range(5):
		for col in range(5):
			if matrix[row][col] == char:
				return row, col
	return None

# Function for replacing 'j' with 'i' and add padding characters 'x' or 'q'
def replaceLetters(plaintext):
	# Always output ‘j’, never ‘i’
	plaintext = plaintext.replace("j", "i")
	processed = ""
	i = 0
	while i < len(plaintext):
		# Pad with the character ‘x’
		if i == len(plaintext) - 1:
			processed += plaintext[i] + 'x'
			break
		if plaintext[i] == plaintext[i + 1]:
			# Encrypting “xx”, use the padding character ‘q’.
			processed += plaintext[i] + ('q' if plaintext[i] == 'x' else 'x')
			i += 1
		else:
			processed += plaintext[i] + plaintext[i + 1]
			i += 2
	return processed

# Function for the logic of encrypting with Playfair Cipher
def encryptPair(pair, matrix):
	# Identifies the position of the characters in the key matrix
	row1, col1 = findPosition(matrix, pair[0])
	row2, col2 = findPosition(matrix, pair[1])
	# If same row, move to the right
	if row1 == row2:
		return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
	# If same column, move down
	elif col1 == col2:
		return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
	# If rectangle, swap columns
	else:
		return matrix[row1][col2] + matrix[row2][col1]

# Function for the running all other functions together to create a Playfair Cipher
def playfairEncrypt(key, plaintext):
	matrix = playfairKeyMatrix(key)
	replacedLetters = replaceLetters(plaintext)
	ciphertext = ""
	for i in range(0, len(replacedLetters), 2):
		ciphertext += encryptPair(replacedLetters[i:i + 2], matrix)
	return ciphertext


def main():
	# User input for the number of pairs
	n = int(input())
	print("")
	for i in range(n):
		# User input for the key
		key = input()
		# User input for the key plaintext
		plaintext = input()
		# Call functions to encrypt the plaintext with key
		ciphertext = playfairEncrypt(key, plaintext)
		# Prints the ciphertext for the current pair of the loop
		print(ciphertext)
		print("")

if __name__ == "__main__":
	main()