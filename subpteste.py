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
    parser_create = subparsers.add_parser('create')
    # Store the result in which for a conditional check later
    parser_create.set_defaults(which='create')

    # Add the first arg to create (First Name)
    parser_create.add_argument(
        '--first_name',
        required=True,
        help='First Name')

    # Add the second arg to create (Last Name)
    parser_create.add_argument(
        '--last_name',
        required=True,
        help='Last Name')

    # The Second subparser 'Delete'
    parser_delete = subparsers.add_parser('delete')
    parser_delete.set_defaults(which='delete')

    parser_delete.add_argument(
        'id', help='Database ID')

    args = parser.parse_args()
