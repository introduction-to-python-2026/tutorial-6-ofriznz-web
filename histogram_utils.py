def read_file(file_path):
  file_content = open(file_path)
  lines = file_content.readlines()
  file_content.close()
  long_string = ""
  for line in lines:
    long_string += line.strip()
  return long_string
