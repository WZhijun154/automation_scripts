import subprocess
import click


@click.command()
@click.option('--username', required=True, help='Username for Git')
@click.option('--password', required=True, help='Password for Git')
@click.option('--email', help='Email for Git')
def config_git(username: str, password: str, email: str = None) -> None:
    try:
        subprocess.run(['git', 'config', '--global', 'user.name', username])
        subprocess.run(['git', 'config', '--global',
                       'user.password', password])
        if email:
            subprocess.run(['git', 'config', '--global', 'user.email', email])
        print("Git global username and password configured successfully.")
    except Exception as e:
        print("An error occurred while setting Git configurations:", e)


if __name__ == '__main__':
    config_git()

# usage
# python config_git.py --username username --password password --email email
