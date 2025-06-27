import argparse
from playbookgen.main import main as run_interactive_main


def main():
    parser = argparse.ArgumentParser(
        prog="playbookgen",
        description="""
        PlaybookGen: An interactive CLI tool to generate structured playbooks.

        You'll be prompted to enter instructions or questions. The tool maintains state
        and builds a YAML playbook interactively based on your input. When you're done,
        it saves the final result to a file if specified.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Optional path to save the generated playbook YAML (e.g., './playbook.yml')"
    )

    args = parser.parse_args()
    run_interactive_main(output_file=args.output)
