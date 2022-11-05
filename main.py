from lib.txt_to_csv import txt_to_csv




def exemplo_obra_machado_de_assis():
    text_name = 'variasHistorias'
    genero = 'conto'
    dataset_name = 'machado_de_assis'
    file_path = f"datalake/{dataset_name}/{genero}/{text_name}.txt"
    lang = "pt"
    csv_file_name = f"data_warehouse/{dataset_name}/{genero}/{text_name}.csv"
    txt_to_csv(file_path, csv_file_name, lang)

def create_doc(text: str, metadata: dict):
    """
    INPUT:
    text - str (the text data to be processed)
    metadata - dict (name, source, url, genre, autor, date, language)
    
    Use Space models to process a string containing natural language data.
    
    OUTPUT:
    database - save the features and the metadata in the database
    http - return a json that can by an http response body.
    """



def main():
    exemplo_obra_machado_de_assis()


if __name__ == '__main__':
    main()
