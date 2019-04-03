'''
    File name: arxivLinkParser.py
    Author: Ramin Nabati
    Date created: 3/10/2019
'''

import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import argparse
import os

def parse_args():
    # Parse the input arguments
    parser = argparse.ArgumentParser(description='Parse an Arxiv page and return paper\'s informationa.')

    parser.add_argument('paper_url',
                        help='URL to the paper\'s abstract page on Arxiv')

    parser.add_argument('-m', dest='max_abstract_len',
                        help='Maximum number of characters in the abstract',
                        default=520)
    
    parser.add_argument('-p',
                        help='Where is the paper published.',
                        default='Arxiv')
    
    parser.add_argument('-c', dest='code_url',
                        help='URL to paper\'s implementation code if available.',
                        default=None)

    args = parser.parse_args()
    return args


def arxivParser(url, max_abstract_len=550):
    
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    title = soup.find('h1', attrs={'class': 'title mathjax'})
    title = title.text.strip()[6:]

    authors = soup.find('div', attrs={'class':'authors'})
    authors = authors.text.strip()[8:]

    abstract = soup.find('blockquote', attrs={'class':'abstract mathjax'})
    abstract = abstract.text.strip().replace("\n"," ")
    len_abs = len(abstract)
    if len_abs > max_abstract_len:
        abstract = abstract[9:max_abstract_len] + '...'
    else:
        abstract = abstract[9:]

    return {'url':url, 'title':title, 'authors':authors, 'abstract':abstract}

## -----------------------------------------------------------------------------
def main(args):

    info = arxivParser(args.paper_url, args.max_abstract_len)

    if args.code_url is not None:
        formatted_info = "- **{title}** [{pub}] [[Paper]({paper_url}), [Code]({code_url})]\n" +\
                       "    > **Authors:** {authors} <br>\n" +\
                       "    > **Abstract:** {abstract}"
        formatted_info = formatted_info.format(title=info['title'], pub=args.p,
        paper_url=info['url'], code_url=args.code_url, authors=info['authors'],
        abstract=info['abstract'])
    
    else:
        formatted_info = "- **{title}** [{pub}] [[Paper]({paper_url})]\n" +\
                       "    > **Authors:** {authors} <br>\n" +\
                       "    > **Abstract:** {abstract}"
        formatted_info = formatted_info.format(title=info['title'], pub=args.p,
        paper_url=info['url'], authors=info['authors'],
        abstract=info['abstract'])
    
    print("-----------------------------------------------------------------")
    print(formatted_info)
    print("-----------------------------------------------------------------\n")
    print('Paper info copied to clipboard.')
    os.system('echo "%s" | pbcopy' % formatted_info)


if __name__ == '__main__':
    args = parse_args()
    main(args)
