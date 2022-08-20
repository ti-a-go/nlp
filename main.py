from utils.txt_to_csv import txt_to_csv


def main():
    text_name = 'variasHistorias'
    genero = 'conto'
    dataset_name = 'machado_de_assis'
    file_path = f"datalake/{dataset_name}/{genero}/{text_name}.txt"
    lang = "pt"
    csv_file_name = f"data_warehouse/{dataset_name}/{genero}/{text_name}.csv"
    txt_to_csv(file_path, csv_file_name, lang)


if __name__ == '__main__':
    main()
