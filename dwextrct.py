import re
import sys
from time import time
import argparse

# part 2: reference extraction
# lookup for the references that start with DBN, DBE or DBW and be followed by alphanumeric characters
# with that character being extracted as well

def extract_references(text, output_file=None):
    pattern = r'\b(DBN|DBE|DBW)(\w+)\b'
    matches = re.findall(pattern, text)

    if output_file == None:
        output_file = 'references.txt'
    
    ret = ''
    with open(output_file, 'w', encoding='utf-8') as f:
        for match in matches:
            f.write(f"{match[0]}{match[1]}\n")
            ret += f"{match[0]}{match[1]}\n"

    print("Reference extraction complete.")
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="references extractor.")
    parser.add_argument("file", help="Path to the TXT file to extract references from")
    parser.add_argument("-o", "--output", help="Optional output text file path")
    args = parser.parse_args()

    text = ''
    with open(args.file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    t1 = time()
    references = extract_references(text, args.output)
    t2 = time()
    print(f"Time taken for reference extraction: {t2 - t1} seconds")
    print(f"Extracted References:\n{references}")
