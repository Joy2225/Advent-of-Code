if __name__ == '__main__':
    with open('D1.txt', 'r') as file:
        values=file.read().split('\n')
    # part 1:
    sum=0
    for s in values:
        l=list( filter ( str.isdigit,s ) )
        sum=sum + int(l[0]) * 10 + int(l[-1])
    print(sum)

    # part 2:
    sum=0
    digits={
        "zero":"ze0o", "one":"o1e", "two":"t2o", "three":"th3ee", "four":"fo4r", "five":"fi5ve", "six":"s6x", "seven":"se7en", "eight":"ei8ht", "nine":"n9ne"
    }
    for s in values:
        for number, replace in digits.items():
            s=s.replace(number, replace)
        l=list( filter ( str.isdigit,s ) )
        sum=sum + int(l[0] + l[-1])
    print(sum)
