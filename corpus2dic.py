import sys

kaz_dict_lower_path = sys.argv[1] 
unique_words_path = sys.argv[2]
dict_path = sys.argv[3]

kaz_dict_lower = {}
with open(kaz_dict_lower_path, 'r') as f:
	for line in f:
		char, sound = line.split()
		print(char, sound)
		kaz_dict_lower[char] = sound

full_transcripts = ""
with open(unique_words_path, 'r') as f:
	for word in f:
		word_transcript = word.strip()
		for char in word.strip():
			word_transcript += " " + kaz_dict_lower[char]
		full_transcripts += word_transcript + "\n"

with open(dict_path, 'w') as f:
	f.write(full_transcripts)
