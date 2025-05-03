from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

all_policies_template = env.get_template('1_allPolicies.j2')
control_template = env.get_template('2_serverProfileTemplate.control.j2')
worker_template = env.get_template('3_serverProfileTemplate.worker.j2')
derive_profiles_template = env.get_template('4_deriveProfiles.j2')

prefix = 'prefix.'
organization = 'default'
domain = 'domain'

all_policies_context = {
    'prefix': prefix,
    'organization': organization
}

control_template_context = {
    'prefix': prefix,
    'organization': organization,
    'domain': domain,
    'template_name': 'control-template'
}

worker_template_context = {
    'prefix': prefix,
    'organization': organization,
    'domain': domain,
    'template_name': 'worker-template'
}

derive_profiles_context = {
    'prefix': prefix,
    'organization': organization,
    'domain': domain,
    'profiles': [
        {'name': 'control-01', 'template': 'control-template'},
        {'name': 'worker-01', 'template': 'worker-template'},
        {'name': 'worker-02', 'template': 'worker-template'}
    ]
}

with open('1_allPolicies.yaml', 'w') as f:
    f.write(all_policies_template.render(**all_policies_context) + '\n')

with open('2_serverProfileTemplate.control.yaml', 'w') as f:
    f.write(control_template.render(**control_template_context) + '\n')

with open('3_serverProfileTemplate.worker.yaml', 'w') as f:
    f.write(worker_template.render(**worker_template_context) + '\n')

with open('4_deriveProfiles.yaml', 'w') as f:
    f.write(derive_profiles_template.render(**derive_profiles_context) + '\n')

print("Rendered: 1_allPolicies.yaml, 2_serverProfileTemplate.control.yaml, 3_serverProfileTemplate.worker.yaml, 4_deriveProfiles.yaml")
