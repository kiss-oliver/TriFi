import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    with open('../../ularger.csv','w') as ul:
        with open('../../vlarger.csv','w') as vl:
            for line in f:
                u, v = line.replace('\n','').split(',')
                if u>v:
                    ul.write(line)
                else:
                    vl.write(line)
