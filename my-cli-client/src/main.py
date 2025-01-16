import click
import cli.api_client as api_client
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@click.command()
def cli():
    """Main entry point for the CLI."""

    api_key = os.getenv("GOOGLE_GENAI_API_KEY")
    if not api_key:
        click.echo("API key not found. Please set the GOOGLE_GENAI_API_KEY environment variable.")
        return
    
    genai.configure(api_key=api_key)
    
    
    while True:
        click.echo("Hello user, please choose what you want to do:")
        click.echo("1. Create a pipeline")
        click.echo("2. Get the details of existing pipeline")
        click.echo("3. Get all pipelines")
        click.echo("4. test the communication to the server")
        click.echo("5. Test Gemini AI")
        click.echo("6. To exit")


        
        choice = click.prompt("Enter your choice as number (1/2/3/4/5/6)", type=int)

        if choice == 1:
            model = genai.GenerativeModel("gemini-1.5-flash",system_instruction="You should test the syntax of a given yaml file. If it's valid please return valid, otherwise return the mistakes and recommendations")
            name = click.prompt("Enter the pipeline name")
            description = click.prompt("Enter the pipeline description")
            # data = click.prompt("Enter the data of the pipeline in yaml format")
            click.echo("Enter a pipeline in a valid yaml format (press Enter to open editor, then paste your yaml file, save it and close it):")
            data = click.edit()
            if data is None:
                click.echo("No data entered.")
            else:
                response = model.generate_content(data)
            if response.text == 'valid\n': 
                click.echo("Great! creating your pipline")
                # result = api_client.create_pipeline(name, description, data)
                # click.echo(f"{result["message"]} with id: {result["data"]}")
            else:
                print(response.text)
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
        elif choice == 5:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = click.prompt("Enter your prompt for Gemini AI")
            response = model.generate_content(prompt, stream = True)
            for chunk in response:
                    print(chunk.text, end=" ")
            # response = model.generate_content("Explain how AI works")
            # print(response.text)
        elif choice == 6:
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid choice. Please choose a number from the valid options")


if __name__ == "__main__":
    cli()



# A valid pipline

# pipeline:
#   name: "Example Pipeline"
#   description: "This is a sample pipeline configuration."
#   steps:
#     - name: "Step 1"
#       action: "load_data"
#       parameters:
#         source: "data/source.csv"
#     - name: "Step 2"
#       action: "process_data"
#       parameters:
#         method: "standardize"
#     - name: "Step 3"
#       action: "save_data"
#       parameters:
#         destination: "data/processed.csv"