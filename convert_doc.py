#!/usr/bin/env python3
import sys
import os
from skills.docx_converter import json_to_docx_file, docx_to_json_file

def print_usage():
    print("Deterministic SDLC Document Format Converter")
    print("Usage:")
    print("  python3 convert_doc.py to-docx <input_json_path> <output_docx_path>")
    print("  python3 convert_doc.py to-json <input_docx_path> <output_json_path>")
    print()

def main():
    if len(sys.argv) < 4:
        print_usage()
        sys.exit(1)
        
    command = sys.argv[1].lower()
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    
    if command == "to-docx":
        if not os.path.exists(input_path):
            print(f"❌ Error: Input JSON file '{input_path}' does not exist.")
            sys.exit(1)
        try:
            print(f"🔄 Converting JSON '{input_path}' to DOCX '{output_path}'...")
            json_to_docx_file(input_path, output_path)
            print("✅ Conversion successful!")
        except Exception as e:
            print(f"❌ Error during conversion: {e}")
            sys.exit(1)
            
    elif command == "to-json":
        if not os.path.exists(input_path):
            print(f"❌ Error: Input DOCX file '{input_path}' does not exist.")
            sys.exit(1)
        try:
            print(f"🔄 Converting DOCX '{input_path}' to JSON '{output_path}'...")
            docx_to_json_file(input_path, output_path)
            print("✅ Conversion successful!")
        except Exception as e:
            print(f"❌ Error during conversion: {e}")
            sys.exit(1)
            
    else:
        print(f"❌ Unknown command: {command}")
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
