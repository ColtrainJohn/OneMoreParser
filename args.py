import argparse


def parseArguments():
    parser = argparse.ArgumentParser(
        prog = 'www.iminfin.ru parser',
        description = 'Parse incidence data from www.iminfin.ru',
        epilog = 'Selezov S.U.'
    )

    parser.add_argument('-out' , metavar='-O', help='Output path')
    parser.add_argument('-year' , metavar='-Y', help='Distinct year to parse')
    parser.add_argument('-month' , metavar='-M', help='Distinct month to parse')
    parser.add_argument('-region' , metavar='-R', help='Distinct region to parse')
    parser.add_argument('-headless' , metavar='-H', help='headless browser mode', default=True)

    parser.parse_args()

    return parser