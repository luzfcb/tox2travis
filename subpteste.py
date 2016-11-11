import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('--bar', nargs='+', help='bar help')
    # parser.print_help()
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands',
                                       help='additional help')

    # The first subparser 'Create'
    parser_toci = subparsers.add_parser('toci')
    # Store the result in which for a conditional check later
    parser_toci.set_defaults(which='toci')

    # Add the first arg to create (First Name)
    parser_toci.add_argument(
        '--travis',
        required=False,
        action='store_true',
        help='Generate test matrix for Travis')

    # Add the second arg to create (Last Name)
    parser_toci.add_argument(
        '--gitlab',
        required=False,
        action='store_true',
        help='Generate test matrix for Gitlab')

    subparsers_of_toci = parser_toci.add_subparsers(title='subcommands',
                                            description='valid subcommands',
                                            help='additional help')

    parser_toci_qqqq = subparsers_of_toci.add_parser('tociaaa')

    parser_toci_qqqq.set_defaults(which='tociaaa')

    args = parser.parse_args()
