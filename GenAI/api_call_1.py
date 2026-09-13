import requests


# for i in range(3):
#     response = requests.get(f"https://jsonplaceholder.typicode.com/users/{i}")
# print(response.status_code)
# print(type(response.text))

# print(response.text)

# var = input("Do you want to proceed")
# # import requests

# def get_book():
#     response = requests.get('https://potterapi-fedeperin.vercel.app/en/books')
#     books = response.json()
#     return books

# # var = get_book()
# # print(type(var))

# # print("\n"*4)
# # print(var)


resp = requests.get("https://api.bigbookapi.com/search-books?query=books+about+wizards")
var = resp.json()

if (resp.status_code == 401) or resp.status_code == "401":
    print(var["message"])
