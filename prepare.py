import requests
import argparse
import sys
import os

def PrepareDay(day, path):
    # Create folder
    folder = os.path.abspath(path)
    if os.path.exists(folder):
        newDayFolder = os.path.join(folder, "day%d"%day)
        if not os.path.exists(newDayFolder):
            os.mkdir(newDayFolder)
        file = open(os.path.join(newDayFolder, "input"), 'w')
        # Fetch input
        for tryCounts in range(0, 1):
            print("Attempt %s reading input" % tryCounts)
            try:
                testURL = "https://adventofcode.com/2022/day/%d/input"%day
                httpRequest = requests.get(testURL, cookies={'session':"53616c7465645f5fcc7fdd37ea785c66c06b22d1aef68e512da5923db5f2fbd0f24aa3eeb5384d358a333bfb4abf4c702c8c0c553ed72f2619336326cadcff3f"})
                file.writelines(httpRequest.text)
                break
            except Exception as e:
                print("Encountered : %s" % str(e))

parser = argparse.ArgumentParser(description='Prepare folders with input.')
parser.add_argument('day', metavar='N', type=int, help='day to prepare')
parser.add_argument('path', type=str)
args = parser.parse_args()
PrepareDay(args.day, args.path)