def run_report(report_name: str) -> None:
    """Generate a report using the local shell."""
    # Use a list of arguments and disable shell execution to prevent command injection
    subprocess.run(
        ["echo", f"Generating report {report_name}"],
        shell=False,
        check=False,
    )