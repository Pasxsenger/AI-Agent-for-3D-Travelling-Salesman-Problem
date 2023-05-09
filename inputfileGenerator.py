import random


def main():
    filename = "inputSmall.txt"
    lines = 10
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(lines) + "\n")
        while lines > 0:
            x = random.randint(1, 1000)
            y = random.randint(1, 1000)
            z = random.randint(1, 1000)
            f.write(str(x) + " " + str(y) + " " + str(z))
            if lines > 1:
                f.write("\n")
            lines -= 1


if __name__ == '__main__':
    main()
