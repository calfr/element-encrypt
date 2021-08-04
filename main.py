import argparse, elementencrypt

parser = argparse.ArgumentParser(description='Create an static page with one or more encrypted elements.')
parser.add_argument("file", action='store', type=argparse.FileType('r'))
parser.add_argument('--version', action='version', version='0.1.0')
parser.add_argument('-t', '--template-file', action='store', type=argparse.FileType('r'))
parser.add_argument('-o', '--output-file', action='store', type=argparse.FileType('w'))

args = parser.parse_args()

if args.file:
    input_text = args.file.read()
    if args.template_file:
        result = elementencrypt.process_file(input_text, args.template_file.read())
    else:
        result = elementencrypt.process_file(input_text)

    if args.output_file:
        args.output_file.write(result)
        args.output_file.close()
    else:
        print(result)
