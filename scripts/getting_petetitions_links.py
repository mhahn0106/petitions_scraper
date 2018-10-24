import argparse
import os
import sys
sys.path.append('../')

from petitions_scrapper import parse_page
from petitions_scrapper import get_petition_links

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--link_file', type=str, default='links.csv')
    parser.add_argument('--begin_page', type=int, default=1)
    parser.add_argument('--end_page', type=int, default=10)

    args = parser.parse_args()
    path = args.link_file
    begin_page = args.begin_page
    end_page = args.end_page

    dirname = os.path.dirname(os.path.abspath(path))
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    links = get_petition_links(begin_page, end_page)
    with open(path, 'w', encoding='utf-8') as f:
        for link in links:
            link_strf = '\t'.join(link)
            f.write('{}\n'.format(link_strf))

if __name__ == '__main__':
    main()