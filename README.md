####VHCreator

KeyJen created to generate some keys or passwords quickly. You can define your char types to use,

    $ keyjen -l 12 -c 5 --types upper,lower --prefix pre_ --suffix _suf

####Installation

```
$ [sudo] pip install keyjen
```


####Options

- -h HELP

- -l, --length You can define length of your key with this option.

- -c, --count Number of keys.

- -t, --types It defines char types. For example you can use uppercase and lowercase letters. There is four choices as all,upper,lower,digit

- -p, --prefix You can define a prefix for your keys.

- -s, --suffix You can define a suffix four your keys.

- -v, --version It shows version of keyjen.
