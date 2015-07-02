#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from argument import Argument
from generator import Generator


def main():
    args = Argument().args
    print(args)
    generator = Generator(args.length, args.types.split(','), args.count, prefix=args.prefix, suffix=args.suffix)


if __name__ == "__main__":
    main()