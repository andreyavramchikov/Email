from fabric.api import env, run
from fabric.operations import sudo


env.user = 'ubuntu'
env.hosts = [
    'ec2-52-90-107-10.compute-1.amazonaws.com'
]

env.key_filename = '/home/andrey/Playtogether.pem'

env.project_name = 'Email'
env.path = '/home/ubuntu/commands/%(project_name)s' % env
env.env_path = '%(path)s/env' % env
env.repo_path = '%(path)s/repository' % env



def deploy():
    sudo('rm -rf Email')  # MUST REMOVE IT
    sudo('apt-get install git')
    setup_directories()
    setup_virtualenv()
    clone_repo()
    # install_requirements()

    # run('source %(env_path)s/bin/activate; %(env_path)s/bin/python %(repo_path)s/manage.py migrate' % env)


def install_requirements():
    """
    Install the required packages using pip.
    """
    run('source %(env_path)s/bin/activate; pip install -r %(repo_path)s/requirements.txt' % env)


def clone_repo():
    """
    Do initial clone of the git repository.
    """
    run('git clone https://github.com/andreyavramchikov/%(project_name)s.git %(repo_path)s' % env)


def setup_directories():
    """
    Create directories necessary for deployment.
    """
    run('mkdir -p %(path)s' % env)
    run('mkdir -p %(env_path)s' % env)


def activate_virtualenv():
    run('source %(env_path)s/bin/activate;' % env)


def setup_virtualenv():
    """
    Setup a fresh virtualenv.
    """
    run('virtualenv %(env_path)s --no-site-packages;' % env)
    run('source %(env_path)s/bin/activate;' % env)
