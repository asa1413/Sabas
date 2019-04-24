def main():
    print("insert file name :")
    file_name = input()
    print("insert char for replacement 4:")
    four_repl = input()

    file_open = open(file_name, 'U')
    for line in file_open:
        l_new_line = line.split("|", 2)

        new_line=l_new_line[0]+"|" + l_new_line[1].replace("4", four_repl,2)+"|"+l_new_line[2]
        print(new_line)
        new_file = open('new2.csv','a')
        new_file.write(new_line)
        new_file.close()
    file_open.close()

    print("Good Job")

main()
