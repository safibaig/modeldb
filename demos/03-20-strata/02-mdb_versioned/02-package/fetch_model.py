from verta import Client
import cloudpickle

client = Client('https://dev.verta.ai')
proj = client.set_project('Tweet Classification', workspace='Convoliution')
expt = client.set_experiment('SpaCy')
run = client.get_experiment_run('First Model')
commit = run.get_commit()[0]

# retrieve model
model = run.get_model()
with open('model.pkl', 'wb') as f:
    cloudpickle.dump(model, f)

# retrieve Python version
env_ver = commit.get("env/python")
python_ver = '.'.join([
    env_ver._msg.python.version.major,
    env_ver._msg.python.version.minor,
])
with open("Dockerfile", 'w+') as f:
    contents = f.readlines()
    contents[0] += python_ver
    f.seek(0)
    f.write('\n'.join(contents))

# retrieve Python package version pins
requirements = '\n'.join([
    ''.join([
        req.library,
        req.constraint,
        '.'.join(map(str, [req.version.major, req.version.minor, req.version.patch]))+req.version.suffix,
    ])
    for req in env_ver._msg.python.requirements
])
with open('requirements.txt', 'w') as f:
    f.write(requirements)
