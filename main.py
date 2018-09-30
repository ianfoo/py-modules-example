#! /usr/bin/env python

from bar import dishroom, huh, sports
from foo import Foo
from residents import luca

def main():
    foo = [ Foo(luca.status()),
            Foo(dishroom()),
            Foo(huh()),
            Foo(sports()) ]
    for f in foo:
        print(f.say())


if __name__ == "__main__":
    main()
