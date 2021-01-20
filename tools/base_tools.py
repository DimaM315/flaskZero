import time


def string_normalize(string):
	# удаляем non_symb с начала и конца,
	# меняем все заглавные буквы на строчные
	
	non_symb = '.,/?!$%;'
	ex = ''
	
	while string[0] in non_symb+" ":
		string = string[1:]
	while string[-1] in non_symb+" ":
		string = string[:-1]
	# очищаем от мусорных символов
	for i in range(len(string)):
		if (string[i] == ' ' and string[i+1] == ' ') or string[i] in non_symb:
			continue
		ex += string[i]

	return ex.lower()


def levenstein(A, B):
	F = [[(i+j) if i*j==0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]
	
	for i in range(1, len(A)+1):
		for j in range(1, len(B)+1):
			if A[i-1]==B[j-1]:
				F[i][j] = F[i-1][j-1]
			else:
				F[i][j] = 1+min(F[i-1][j], F[i][j-1], F[i-1][j-1])
	return F[len(A)][len(B)]


def valid_data_reg(args):
    for i in args:
        if len(i) < 3:
            return False
    return True


def slugify(title):
    # title has checked on len
    assert len(title) >= 6 
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', title)
    

if __name__ == '__main__':
	print(len(extract_comments(-1)))
	