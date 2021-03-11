from collections import deque:
search_queue = deque()
search_queue += graph['you']

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person+ ' is a mango seller!')
        return True
    else:
        search_queue += graph[person]
return False
