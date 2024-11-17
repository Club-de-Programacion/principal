import re

def read_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_txt(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def extract_text_from_srt(srt_content):
    # Remove the numbers and timestamps
    text = re.sub(r'\d+\n', '', srt_content)
    text = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', text)
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n+', '\n', text)
    text = text.splitlines()
    for i in range(len(text)):
        text[i] = (text[i])[26::]
    text = '\n'.join(text)
    return text

def main(input_srt, output_txt):
    srt_content = read_srt(input_srt)
    text_content = extract_text_from_srt(srt_content)
    write_txt(text_content, output_txt)

if __name__ == "__main__":
    alpha = input("Enter file name without .srt extension: ")
    input_srt = f"{alpha}.srt"  # Replace with your .srt file path
    output_txt = f'{alpha}.txt'  # Replace with your desired .txt file path
    main(input_srt, output_txt)
