import click
from cli import create_pipeline, execute_pipeline

@click.command()
def cli():
    """Main entry point for the CLI."""
    click.echo("Hello user, please choose what you want to do:")
    click.echo("1. Create a pipeline")
    click.echo("2. Run an existing pipeline")
    choice = click.prompt("Enter your choice as number (1/2)", type=int)

    if choice == 1:
        create_pipeline()
    elif choice == 2:
        execute_pipeline()
    else:
        click.echo("Invalid choice. Please enter 1 or 2.")

# Register the commands with the CLI group
def create_pipeline():
        """Commad to create a new pipeline."""
        click.echo("Creating a pipeline...")

def execute_pipeline():
    """Command to execute a pipeline."""
    click.echo("Executing a pipeline...")

if __name__ == "__main__":
    cli()