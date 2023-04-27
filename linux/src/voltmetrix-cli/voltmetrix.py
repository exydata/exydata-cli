import click # type: ignore
import requests # type: ignore
import json

# voltmetrix cli allows you to interact with the voltmetrix platform. register, add funds to your account, login, deploy, resize and terminate services with this tool.

@click.group()
def cli():
    pass

@cli.command()
@click.option('--first_name', prompt='First Name', help='Your first name')
@click.option('--last_name', prompt='Last Name', help='Your last name')
@click.option('--email', prompt='Your email', help='The email you use to login to voltmetrix')
@click.option('--password', prompt='Your password', help='The password you use to login to voltmetrix')
def register(first_name, last_name, email, password):
    """Sign up to voltmetrix platform"""
    print('Registering...')
    url = 'https://api.voltmetrix.com/v1/accounts/register'
    data = json.dumps({"first_name": first_name, "last_name": last_name, "email": email, "password": password})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--email', prompt='Your email', help='The email you use to login to voltmetrix')
@click.option('--code', prompt='Your confirmation code', help='The confirmation code you received in your email')
def confirm(email, code):
    """Confirm your account"""
    print('Confirming your account...')
    url = 'https://api.voltmetrix.com/v1/accounts/confirm'
    data = json.dumps({"email": email, "code": code})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))


@cli.command()
@click.option('--email', prompt='Your username', help='The username you use to login to voltmetrix')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--password', prompt='Your password', help='The password you use to login to voltmetrix')
def login(email, org_id, password):
    """Login to voltmetrix platform"""
    print('Logging in...')
    url = 'https://api.voltmetrix.com/v1/accounts/login'
    data = json.dumps({"email": email, "org_id": org_id, "password": password})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@cli.command()
@click.option('--database', prompt='Your database', help='The database you want to deploy')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
@click.option('--size', prompt='Your size', help='The size you want to deploy')
@click.option('--region', prompt='Your region', help='The region you want to deploy')
def deploy(database, org_id, token, size, region):
    """Deploy a new resource to Voltmetrix platform"""
    print('Deploying a new resource, sit tight...')
    url = 'https://api.voltmetrix.com/v1/services/deploy'
    data = json.dumps({"database": database, "org_id": org_id, "token": token, "size": size, "region": region})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

# resize a database
@cli.command()
@click.option('--resource_id', prompt='Your resource_id', help='The resource_id you want to resize')
@click.option('--size', prompt='Your size', help='The size you want to resize')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
def resize(resource_id, size, org_id, token):
    """Resize a resource in Voltmetrix platform"""
    print('Resizing a resource, sit tight...')
    url = 'https://api.voltmetrix.com/v1/services/resize'
    data = json.dumps({"resource_id": resource_id, "size": size, "org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

# terminate a database, required confirmation from user
@cli.command()
@click.option('--resource_id', prompt='Your resource_id', help='The resource_id you want to terminate')
@click.option('--region', prompt='Your region', help='The region you want to deploy')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
def terminate(resource_id, region, org_id, token):
        print('Terminating a resource, sit tight...')
        url = 'https://api.voltmetrix.com/v1/services/terminate'
        data = json.dumps({"resource_id": resource_id, "region": region, "org_id": org_id, "token": token})
        r = requests.post(url, data=data)
        print(json.dumps(r.json(), indent=4, sort_keys=True))

# get a list of all databases

@cli.command()
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
def list(org_id, token):
    """List all resources in Voltmetrix platform"""
    print('Getting a list of all resources...')
    url = 'https://api.voltmetrix.com/v1/services/list/'
    data = json.dumps({"org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))


@cli.command()
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
def balance(org_id, token):
    """Get your balance"""
    print('Getting your balance...')
    url = 'https://api.voltmetrix.com/v1/accounts/balance/get'
    data = json.dumps({"org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))


if __name__ == '__main__':
    cli()
