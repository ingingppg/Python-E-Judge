"""Ask"""
def main():
    """Function Main"""
    num = int(input())
    element = []
    elements = []
    for i in range(num):
        text = input()
        elements.append(text)
        if text not in element:
            element.append(text)
    freq = []
    for i in element:
        freq.append(elements.count(i))
    if freq.count(max(freq)) > 1:
        print("No.")
    else:
        idx = freq.index(max(freq))
        print(element[idx])
main()
