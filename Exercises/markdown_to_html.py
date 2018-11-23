#!/usr/bin/env python

import argparse
import sys
import inspect
import jinja2
import markdown

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i&amp;subset=cyrillic,cyrillic-ext,latin-ext,vietnamese" rel="stylesheet">    
    <style>
        body {
            font-family: 'Lora', serif;
            font-size: 9;
            font-weight: 100;
            font-size: inherit;
        }
        code, pre {
            font-family: monospace;
        }
        h1 code,
        h2 code,
        h3 code,
        h4 code,
        h5 code,
        h6 code {
            font-size: inherit;
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""


def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    md = args.mdfile.read()
    extensionlist = ['extra', 'smarty']
    html = markdown.markdown(md, extensions=extensionlist)
    doc = jinja2.Template(TEMPLATE).render(content=html)
    args.out.write(doc)


if __name__ == '__main__':
    sys.exit(main())
