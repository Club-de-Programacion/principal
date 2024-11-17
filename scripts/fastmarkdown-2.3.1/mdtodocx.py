# Necesitas tener instalado Pandoc para convertir.

import pypandoc

def markdown_to_word(input_md_file, output_word_file):
    try:
        # Convert markdown to word file
        pypandoc.convert_file(input_md_file, 'docx', outputfile=output_word_file)
        print(f"Conversion successful: {output_word_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    string = input("File name (without file extension): ")
    input_md_file = f'{string}.md'  # Replace with your markdown file path
    output_word_file = f'{string}.docx'  # Replace with desired word output path
    markdown_to_word(input_md_file, output_word_file)
