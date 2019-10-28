import pandas


def read_file(file_name, field_separator='\n', comment='#'):
    result_list = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line.startswith(comment):
                continue
            elements = line.split(field_separator)
            if len(elements) == 1:
                result_list.append(elements[0].strip())
            else:
                elements = [ el.strip() for el in elements ]
                result_list.append(tuple(elements))
    return result_list
    
    
    

    
#
# Everything below gets only executed when the file is explicitly being run
# and not when imported. This is useful for testing the functions.
#
if __name__ == "__main__":
    
    file_name = "../data/reviews.csv"
    
    print (read_file(file_name, fiel))