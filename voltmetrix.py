import click # type: ignore
import requests # type: ignore
import json

@click.group()
def cli():
    pass

@cli.command()
@click.option('--email', prompt='Your email', help='The email you use to login to voltmetrix')
@click.option('--password', prompt='Your password', help='The password you use to login to voltmetrix')
def register(email, password):
    """Sign up to voltmetrix platform"""
    print('Registering...')
    url = 'http://127.0.0.1:8000/v1/accounts/register'
    data = json.dumps({"email": email, "password": password})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

@click.command()
@click.option('--email', prompt='Your email', help='The email you use to login to voltmetrix')
@click.option('--code', prompt='Your confirmation code', help='The confirmation code you received in your email')
def confirm(email, code):
    """Confirm your account"""
    print('Confirming your account...')
    url = 'http://127.0.0.1:8000/v1/accounts/confirm'
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
    url = 'http://127.0.0.1:8000/v1/accounts/login'
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
    url = 'http://127.0.0.1:8000/v1/services/deploy'
    data = json.dumps({"database": database, "org_id": org_id, "token": token, "size": size, "region": region})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

# list all databases
@cli.command()
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
def list(org_id, token):
    """List all resources in Voltmetrix platform"""
    print('Listing all databases...')
    url = 'http://127.0.0.1:8000/v1/services/list'
    data = json.dumps({"org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

# resize a database
@cli.command()
@click.option('--resource_id', prompt='Your resource_id', help='The resource_id you want to resize')
@click.option('--plan', prompt='Your size', help='The size you want to resize')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
def resize(resource_id, plan, org_id, token):
    """Resize a resource in Voltmetrix platform"""
    print('Resizing a resource, sit tight...')
    url = 'http://127.0.0.1:8000/v1/services/resize'
    data = json.dumps({"resource_id": resource_id, "size": plan, "org_id": org_id, "token": token})
    r = requests.post(url, data=data)
    print(json.dumps(r.json(), indent=4, sort_keys=True))

# terminate a database, required confirmation from user
@cli.command()
@click.option('--resource_id', prompt='Your resource_id', help='The resource_id you want to terminate')
@click.option('--region', prompt='Your region', help='The region you want to deploy')
@click.option('--org_id', prompt='Your org_id', help='The org_id you use to login to voltmetrix')
@click.option('--token', prompt='Your token', help='The token you use to login to voltmetrix')
def terminate(resource_id, region, org_id, token):
    """Terminate a resource in Voltmetrix platform"""
    confirmation = input('Are you sure you want to terminate this resource? (y/n): ')
    if confirmation != 'y':
        print('Termination aborted')
        return
    else:
        print('Terminating a resource, sit tight...')
        url = 'http://127.0.0.1:8000/v1/services/terminate'
        data = json.dumps({"resource_id": resource_id, "region": region, "org_id": org_id, "token": token})
        r = requests.post(url, data=data)
        print(json.dumps(r.json(), indent=4, sort_keys=True))

if __name__ == '__main__':
    cli()