import click
import cli.api_client as api_client

@click.command()
def cli():
    """Main entry point for the CLI."""
    click.echo("Hello user, please choose what you want to do:")
    click.echo("1. Create a pipeline")
    click.echo("2. Get the details of existing pipeline")
    click.echo("3. Get all pipelines")
    click.echo("4. test the communication to the server")
    choice = click.prompt("Enter your choice as number (1/2/3)", type=int)

    if choice == 1:
        name = click.prompt("Enter the pipeline name")
        description = click.prompt("Enter the pipeline description")
        result = api_client.create_pipeline(name, description)
        click.echo(f"{result["message"]} with id: {result["data"]}")
    elif choice == 2:
        pipeline_id = click.prompt("Enter the pipeline ID", type=int)
        result = api_client.get_pipeline(pipeline_id)
        click.echo(f"Success: {result["data"]}")
    elif choice == 3:
        result = api_client.get_pipelines()
        click.echo(f"Success: {result["data"]}")
    elif choice == 4:
         result = api_client.test_connection()
         click.echo(f"Success: {result["message"]}")
    else:
        click.echo("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    cli()