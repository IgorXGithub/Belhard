def count_letters(inputfile, outputfile):
    with open(inputfile, 'r', encoding='utf-8') as file, open(outputfile, 'w', encoding='utf-8') as resfile:
        line_num = 1
        for line in file:
            number = sum(1 for i in line if i.isalpha())
            result = f"{line_num} строка - {number} букв(ы)\n"
            resfile.write(result)
            line_num += 1


count_letters('text.txt', 'res.txt')
