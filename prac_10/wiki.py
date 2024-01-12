import wikipedia


def search():
    keyword = input("Please input the search keyword: ")
    while keyword != "":
        try:
            page_results = wikipedia.page(keyword)
            print(page_results.title)
            print(page_results.sumary)
            print(page_results.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        keyword = input("Please input the search keyword: ")
    print("Thank you")


search()
