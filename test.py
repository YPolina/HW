from collections import deque

graph = {}

graph['you'] = ['Alice', 'Bob', 'Claire']
graph['Bob'] = ['Anuj', 'Peggi']
graph['Alice'] = ['Peggi']
graph['Claire'] = ['Thoe', 'Jhonnym']
graph['Peggi'] = []
graph['Anuj'] = []
graph['Thoe'] = []
graph['Jhonnym'] = []


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + 'is mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search('you')
