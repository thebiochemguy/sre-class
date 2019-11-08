import os
import pyperclip
import re


def print_results(comment, results):
    if(len(results)!=0):
        print(f'{comment}')
        for i in results:
            print(f'{i}')
# print(pyperclip.paste())

phones=re.compile(r'(\d{3}-)?(\d{3}-\d{4})+')
emails=re.compile(r'\S+@\S+')
# exp=re.compile(r'(\d{3}-)?(\d{3}-\d{4})+|\S+@\S+', re.VERBOSE)

p_results=phones.findall(pyperclip.paste())
e_results=emails.findall(pyperclip.paste())
# stuff=exp.findall(pyperclip.paste())

# print(f'phones found: {p_results}')
# print(f'emails found: {e_results}')




if(len(p_results)==0 and len(e_results)==0):
    print(f'No email or phones numbers were found')
else:
    print_results("The following numbers were found.", p_results)
    print_results("The following emails were found.",e_results)
    # if(len(p_results)!=0):
    #     print(f'Following numbers were found: ')
    #     for i in p_results:
    #         print(f'{i}')
    # if(len(e_results)!=0):
    #     print(f'Following emails were found: ')
    #     for i in e_results:
    #         print(f'{i}')

    
# print(f'results are {stuff}')
# pyperclip.copy(print(results))
