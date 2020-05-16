#! /bin/bash

echo input_file and output_name, no filename extensions, separated by a space:
read input_file
k2pdfopt $input_file.pdf
echo -ne '\n' | ebook-convert $input_file"_k2opt.pdf" $input_file".mobi"
# echo -ne '\n' | ebook-meta $input_file".mobi" [--title, $input_file]
echo -ne '\n' | rm $input_file"_k2opt.pdf"


