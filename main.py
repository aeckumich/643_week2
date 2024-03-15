"""
This is the main script.
"""


if __name__ == "__main__":
    import argparse
    from data_loader import load_player
    from data_manipulation import manipulate_data
    from graph_builder import build_graph

    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", help="The name of the output file. ")
    parser.add_argument(
        "--values", nargs="+", help="Player names to plot. ", required=True
    )
    args = parser.parse_args()

    dfs = [load_player(name) for name in args.values]
    dfs = [manipulate_data(df) for df in dfs]

    build_graph(dfs, (20, 10), args.output_file)
