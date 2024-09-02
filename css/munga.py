import random

def main():
    # Single server queue simulation
    run = 10
    mean = 10.0
    sd = 1.5
    mue = 9.5
    sigma = 1.0

    sb = 0.0
    se = 0.0
    cat = 0.0
    cwt = 0.0
    cit = 0.0

    outfile = open("output.txt", "w")
    outfile.write("\n i r' IAT CAT SB r' ST SE WT IT\n")

    for j in range(1, run + 1):
        # Generate inter-arrival time
        sum = 0
        for i in range(1, 13):
            x = random.random()
            sum += x
        x1 = mean + sd * (sum - 6)
        iat = x1
        cat += iat

        if cat <= se:
            sb = se
            wt = se - cat
            cwt += wt
        else:
            sb = cat
            it = sb - se
            cit += it

        # Generate service time
        sum = 0
        for i in range(1, 13):
            x = random.random()
            sum += x
        x2 = mue + sigma * (sum - 6)
        st = x2
        se = sb + st

        outfile.write(f"{j}\t{x1:.4f}\t{iat:.4f}\t{cat:.4f}\t{sb:.4f}\t{x2:.4f}\t{st:.4f}\t{se:.4f}\t{wt:.4f}\t{it:.4f}\n")

    awt = cwt / run
    pcu = (cat - cit) * 100 / cat

    outfile.write(f"Average waiting time: {awt}\n")
    outfile.write(f"Percentage capacity utilization: {pcu}\n")

    outfile.close()

if __name__ == "__main__":
    main()