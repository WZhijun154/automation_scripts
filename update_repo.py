import git
import os.path as osp
import click


@click.command()
@click.option('--url', required=True, help='URL of the repository to update')
@click.option('--path', required=True, help='Path to the repository')
@click.option('--username', required=True, help='Username for the repository')
@click.option('--password', required=True, help='Password or token for the repository')
def update_repo(url: str, path: str, username: str, password: str) -> bool:
    try:
        if not osp.exists(osp.join(path, '.git')):
            # Cloning for the first time with authentication
            repo = git.Repo.clone_from(
                url,
                to_path=path,
                env=dict(GIT_USERNAME=username, GIT_PASSWORD=password)
            )
        else:
            # Pulling updates with authentication
            repo = git.Repo(path)
            repo.git.update_environment(
                GIT_USERNAME=username, GIT_PASSWORD=password)
            repo.remotes.origin.pull()
        return True  # Update successful
    except git.exc.GitCommandError as e:
        print(f"Error updating repository: {e}")
        return False  # Update failed


if __name__ == '__main__':
    update_repo()
# usage
# python update_repo.py --url url --path path --username username --password password
