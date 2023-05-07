def list_line_length_of_file(filename):
    """Return a list of line lengths for a file."""
    with open(filename, "r") as f:
        return [len(line) for line in f.readlines()]
