file1 = open("body_normal.css", "r")
file_line_list = file1.readlines()
file1.close
file2 = open("body_minify.css", "a")
x = ' '.join([line.strip() for line in file_line_list]) 
file2.write(x)

