import click

@click.command()
def create_pipeline():
    """Command to create a new pipeline."""
    click.echo("Creating pipeline...")