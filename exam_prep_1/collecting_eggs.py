from collections import deque

eggs = deque(int(x) for x in input().split(', '))
paper_sheets = [int(x) for x in input().split(', ')]
boxes_filled = 0
box_size = 50
while eggs and paper_sheets:
    if eggs[0] <= 0:
        eggs.popleft()
        continue
    elif eggs[0] == 13:
        eggs.popleft()
        paper_sheets[-1], paper_sheets[0] = paper_sheets[0], paper_sheets[-1]
        continue
    current_egg = eggs.popleft()
    current_paper = paper_sheets.pop()
    if current_egg + current_paper <= box_size:
        boxes_filled += 1
if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if paper_sheets:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sheets)}")

