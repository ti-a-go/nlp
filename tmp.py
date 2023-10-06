# import requests
# from bs4 import BeautifulSoup

# url = "http://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm"
# html = requests.get(url)
# print(html)

# soup = BeautifulSoup(html, features="html.parser")

# # kill all script and style elements
# for script in soup(["script", "style"]):
#     script.extract()    # rip it out

# # get text
# text = soup.get_text()

# # break into lines and remove leading and trailing space on each
# lines = (line.strip() for line in text.splitlines())
# # break multi-headlines into a line each
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # drop blank lines
# text = '\n'.join(chunk for chunk in chunks if chunk)

# file = open("temp_text.txt", "w+")
# file.write(text)
# file.close()


# print(text)

if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.html"
    # print(url)
    html = requests.get(url)
    print(html)