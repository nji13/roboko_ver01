# コマンドラインからオプションを設定して、プログラムを実行することができる。スクリプトに引数を渡してプログラム内で使える

from optparse import OptionParser
from optparse import OptionGroup


def main():

    usage = 'usage: %prog [options] argv1 argv2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string', dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='int', dest='num')
    parser.set_defaults(verbose=True)
    parser.add_option('-v', action='store_true', dest='verbose')
    # parser.add_option('-v', action='store_false', dest='verbose', default=True)
    parser.add_option('-q', action='store_false', dest='verbose')

    parser.add_option('-r', action='store_const', const='root', dest='user_name')

    parser.add_option('-e', dest='env')

    def is_relase(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't relase")
        setattr(parser.values, option.dest, True)
    
    parser.add_option('--release', action='callback', callback=is_relase, dest='release')

    group = OptionGroup(parser, 'Dangerous options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)

    options, args = parser.parse_args()
    print(options)
    print(args)

if __name__ == '__main__':
    main()
