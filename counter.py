def countEmail():
    # This first line is provided for you
    name = input("Enter file: ")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    counts = {}
    for line in handle:
        if line.startswith("From "):
            split_line = line.split()
            sender = split_line[1]
            counts[sender] = counts.get(sender, 0) + 1
    
    max_sender = 0
    max_sent = 0
    for email, number in counts.items():
        if number > max_sent:
            max_sender = email
            max_sent = number
    print(max_sender, max_sent)




            
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
