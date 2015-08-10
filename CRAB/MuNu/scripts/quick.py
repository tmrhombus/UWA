import sys
import argparse

parser = argparse.ArgumentParser(description="Submit analyzer to condor")

parser.add_argument('jobName', type=str, help='Job name for submission')

def parse_command_line(argv):
    parser = argparse.ArgumentParser(description="Submit analyzer to condor")

    parser.add_argument('jobName', type=str, help='Job name for submission')
    parser.add_argument('tomName', type=str, help='Tom name for submission')
    args = parser.parse_args(argv)

    return args

argv = sys.argv[1:]
args = parse_command_line(argv)

print args.jobName
print args.tomName
