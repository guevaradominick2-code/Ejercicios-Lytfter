def text_writer(path1, path2):
    with open(path1, 'r', encoding="UTF-8") as file:
        lines = [line.strip() for line in file.readlines()]      
        text = ' '.join(lines) 
        
    with open(path2, 'w', encoding="UTF-8") as file2: 
        file2.write(text)

text_writer("Ejercicio1.txt", "solucion_ejercicio.txt")
#-------------------------------------------------------------------------------------
def sentence_counter(path3):
    with open(path3, 'r', encoding="UTF-8") as file:
        text_data = file.read()
    
    words = text_data.split()
    counter = len(words) 
    
    return counter


result = sentence_counter("sentences_counter.txt")
print(f"El texto contiene {result} palabras")     
#-------------------------------------------------------------------------------------

def lower_case_conversion(path4,new_file):
    with open(path4, 'r', encoding = "UTF-8") as file:
        lower_text= file.read()
    with open (new_file, "w", encoding = "UTF-8") as new_text:
        new_text.write(lower_text.upper())


lower_case_conversion("lower_cases.txt", "upper_cases.txt")
#-------------------------------------------------------------------------------------
def text_append(path5):

    new_text = input("Inserte el texto que desea agregar al documento: ")
    try:
        with open(path5,"a", encoding = "UTF-8") as append_text:
            append_text.write("\n"+ new_text)
    except:
        with open(path5,"w", encoding = "UTF-8") as append_text:
            append_text.write(new_text)

text_append("text_includer.txt")