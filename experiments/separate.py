import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open(args.filename, 'r') as f:
    with open('../../ordered.csv','w') as ord:
        for line in f:
            u, v = line.replace('\n','').split(',')
            if u>v:
                ord.write('{},{}\n'.format(v, u))
            else:
                ord.write(line)
