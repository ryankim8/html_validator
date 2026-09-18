#!/bin/python3

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    try:
        tags_list = _extract_tags(html)
    except ValueError:
        return False
    stack = []
    for tag in tags_list:
        if tag[1] != "/":
            stack.append(tag)
        else:
            if tag[0] + tag[2:] in stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0
    
    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the stack.py file.
    # The main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags.


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags_list = []
    i = 0
    while i < len(html):
        if html[i] == "<":
            end_tag = html.find(">", i)
            if end_tag == -1:
                raise ValueError("found < without matching >")
            start_tag = html[i:end_tag+1]
            start_tag_items = start_tag.split()
            if len(start_tag_items) > 1:
                tags_list.append(start_tag_items[0] + ">")
            else:
                tags_list.append(start_tag_items[0])
            i = end_tag + 1
        else:
            i += 1
    return tags_list
