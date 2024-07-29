import click
import requests
import json

token = None

@click.group()
def cli():
    pass

@cli.command()
@click.option('--first_name', prompt='First Name', help='Your first name')
@click.option('--last_name', prompt='Last Name', help='Your last name')
@click.option('--email', prompt='Your email', help='The email you use to login to exydata')
@click.option('--password', prompt='Your password', help='The password you use to login to exydata')
def register(first_name, last_name, email, password):
    """Sign up to exydata platform"""
    print('Registering...')
    url = 'https://api.exydata.com/v1/accounts/register'
    data = json.dumps({"first_name": first_name, "last_name": last_name, "email": email, "password": password})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--email', prompt='Your email', help='The email you use to login to exydata')
@click.option('--code', prompt='Your confirmation code', help='The confirmation code you received in your email')
def confirm(email, code):
    """Confirm your account"""
    print('Confirming your account...')
    url = 'https://api.exydata.com/v1/accounts/confirm'
    data = json.dumps({"email": email, "code": code})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--email', prompt='Your email', help='The email you use to login to exydata')
@click.option('--password', prompt='Your password', help='The password you use to login to exydata')
def login(email, password):
    """Login to exydata platform"""
    print('Logging in...')
    url = 'https://api.exydata.com/v1/accounts/login'
    data = json.dumps({"email": email, "password": password})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--cloud', prompt='Where you want to deploy', help='You can deploy to AWS and DigitalOcean')
@click.option('--database', prompt='Your database', help='The database you want to deploy')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to exydata')
@click.option('--token', prompt='Your token', help='The token you use to login to exydata')
@click.option('--plan', prompt='Your plan', help='The plan you want to deploy')
@click.option('--region', prompt='Your region', help='The region you want to deploy')
def deploy(cloud, database, org_id, token, plan, region):
    """Deploy a new resource to ExyData platform"""
    print('Deploying a new resource, sit tight...')
    url = 'https://api.exydata.com/v1/services/deploy'
    data = json.dumps({"cloud": cloud, "database": database, "org_id": org_id, "token": token, "plan": plan, "region": region})
    r = requests.post(url, data=data)
    try:
        response_data = r.json()
        print(json.dumps(response_data, indent=4, sort_keys=True))
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON response: {e}")

@cli.command()
@click.option('--cloud', prompt='Where your resource id is running', help='Specify the cloud provider, AWS or DigitalOcean')
@click.option('--region', prompt='Your region', help='The where your instance/resource is running')
@click.option('--resource_id', prompt='Your resource_id', help='The resource_id you want to replan')
@click.option('--plan', prompt='Your plan', help='The plan you want to replan')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to exydata')
@click.option('--token', prompt='Your token', help='The token you use to login to exydata')
def replan(cloud, region, resource_id, plan, org_id, token):
    """Resize a resource in ExyData platform"""
    print('Resizing a resource, sit tight...')
    url = 'https://api.exydata.com/v1/services/replan'
    data = json.dumps({"cloud": cloud, "region": region, "resource_id": resource_id, "plan": plan, "org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--cloud', prompt='Where your resource id is running', help='Specify the cloud provider, AWS or DigitalOcean')
@click.option('--resource_id', prompt='Your resource_id', help='The resource_id you want to terminate')
@click.option('--region', prompt='Your region', help='The region you want to deploy')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to exydata')
@click.option('--token', prompt='Your token', help='The token you use to login to exydata')
def terminate(cloud, resource_id, region, org_id, token):
    """Terminate a resource in ExyData platform, this will delete the resource, data is not recoverable"""
    print('Terminating a resource, sit tight...')
    url = 'https://api.exydata.com/v1/services/terminate'
    data = json.dumps({"cloud": cloud, "resource_id": resource_id, "region": region, "org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to exydata')
@click.option('--token', prompt='Your token', help='The token you use to login to exydata')
def list(org_id, token):
    """List all resources in ExyData platform"""
    print('Getting a list of all resources...')
    url = 'https://api.exydata.com/v1/services/list/'
    data = json.dumps({"org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

# I want to create a command for balance and then a sub argument for get and add balance. 

@cli.command()
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to exydata')
@click.option('--token', prompt='Your token', help='The token you use to login to exydata')
def balance(org_id, token):
    """Get your balance in ExyData platform"""
    print('Getting your balance...')
    url = 'https://api.exydata.com/v1/balance/get'
    data = json.dumps({"org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to exydata')
@click.option('--token', prompt='Your token', help='The token you use to login to exydata')
def add_balance(org_id, token):
    """Add money to your ExyData balance"""
    print('Processing...')
    url = 'https://api.exydata.com/v1/balance/add'
    data = json.dumps({"org_id": org_id, "token": token,})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))


if __name__ == '__main__':
    cli()
