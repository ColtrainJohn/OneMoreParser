import argparse



def parseArguments():
    parser = argparse.ArgumentParser(
        prog = 'www.iminfin.ru parser',
        description = 'Parse incidence data from www.iminfin.ru',
        epilog = 'Selezov S.U.'
    )

    parser.add_argument('-out', metavar='-O')
    parser.add_argument('-year', metavar='-Y', help='Distinct year to parse', default=False)
    parser.add_argument('-month', metavar='-M', help='Distinct month to parse', default=False)
    parser.add_argument('-region', metavar='-R', help='Distinct region to parse', default=False)
    parser.add_argument('-headless', metavar='-H', help='headless browser mode', default=True)
    return parser


if __name__ == '__main__':
    parser = parseArguments()
    args = parser.parse_args()
    print(args)
    
