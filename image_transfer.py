#!/usr/bin/env python3

import argparse
import subprocess

DEFAULT_PULL_SERVER = {
    "source": "registry.cn-shanghai.aliyuncs.com",
    "dest": "gcr.io"
}

DEFAULT_PUSH_SERVER = {
    "dest": "registry.cn-shanghai.aliyuncs.com",
    "source": "gcr.io"
}


def process_images(mode, imagefile, source_server, dest_server, keepsource, keepdest):
    with open(imagefile, "r") as file:
        for line in file.readlines():
            if (len(line) < 5):
                continue
            print("process line", line)
            str = line.strip().split(" ")
            if mode == "pull":
                source = source_server + "/" + str[0]
                dest = dest_server + "/" + str[1]
            else:
                source = source_server + "/" + str[1]
                dest = dest_server + "/" + str[0]

            subprocess.run(["docker pull " + source], shell=True, check=True)
            subprocess.run(["docker tag " + source + " " + dest], shell=True, check=True)
            if keepsource == "default":
                subprocess.run(["docker rmi " + source], shell=True, check=True)

            if mode == "push":
                subprocess.run(["docker push " + dest], shell=True, check=True)
                if keepdest == "default":
                    subprocess.run(["docker rmi " + dest], shell=True, check=True)


parser = argparse.ArgumentParser(description='transfer images between registry servers ')
parser.add_argument("-mode", default="pull", help="image list file")
parser.add_argument("-image", default="image.list", help="image list file")
parser.add_argument("-source", default="default", help="the source registry server")
parser.add_argument("-dest", default="default", help="the dest registry server for tag")
parser.add_argument("-keepsource", default="default", help="remain source image")
parser.add_argument("-keepdest", default="default", help="remain dest image")
args = parser.parse_args()

if args.mode == "pull":
    if args.source == "default":
        args.source = DEFAULT_PULL_SERVER["source"]
    if args.dest == "default":
        args.dest = DEFAULT_PULL_SERVER["dest"]
else:
    if args.source == "default":
        args.source = DEFAULT_PUSH_SERVER["source"]
    if args.dest == "default":
        args.dest = DEFAULT_PUSH_SERVER["dest"]

process_images(args.mode, args.image, args.source, args.dest, args.keepsource, args.keepdest)
