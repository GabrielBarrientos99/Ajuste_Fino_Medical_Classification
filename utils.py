def print_description_register(index, df, indent=4):
    indent_str = " " * indent
    print("{")
    print(indent_str + "Registro " + str(index) + ":")
    print(indent_str + "-" * 40)  # Separador para mayor claridad
    
    # Iteramos por las columnas de interés para hacer el formato
    for col in ['Title', 'Description', 'Sintomas', 'FactoresRiesgo', 'Complicaciones', 'Diagnostico']:
        print(indent_str + col + ":")
        print(indent_str + indent_str + str(df[col][index]))
        print()
    
    print(indent_str + "-" * 40)  # Separador final
    print("}")



def print_text_label(index, df, indent=4):
    indent_str = " " * indent
    print("{")
    print(indent_str + "Texto:")
    print(indent_str + "-" * 40)  # Separador para mayor claridad
    print(indent_str + indent_str + str(df['Text'][index]))
    print()
    print(indent_str + "Etiqueta:")
    print(indent_str + indent_str + str(df['Label'][index]))
    print(indent_str + "-" * 40)  # Separador final
    print("}")