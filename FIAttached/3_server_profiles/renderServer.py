from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

uuid_pool_template = env.get_template('1_UUID_Pool.j2')
policies_template = env.get_template('2_policies.j2')
template_template = env.get_template('3_serverProfileTemplate.j2')
profiles_template = env.get_template('4_server_profiles.j2')

prefix = 'prefix.'
organization = 'default'

# VLAN settings
vlan_settings = {
    'AllowedVlans': '"70"',
    'TrunkMode': 'TRUNK',
    'DefaultVLAN': '0'
}

# VMEDIA
vmedia_settings = {
    'bootVMedia': False
}

# IPMI
ipmi_settings = {
    'Enable': False,
    'TKVM': True
}

# UUID Pool context
uuid_pool_context = {
    'prefix': prefix,
    'organization': organization,
    'uuid_block_from': '0000-000000100001',
    'uuid_block_size': 256
}

# Policies context
policies_context = {
    'prefix': prefix,
    'organization': organization,
    **vlan_settings,
    **vmedia_settings,
    **ipmi_settings
}

# Server profile template context
server_template_context = {
    'prefix': prefix,
    'organization': organization,
    'template_name': 'ExampleServerTemplate',
    **vlan_settings,
    **vmedia_settings,
    **ipmi_settings
}

# Server profiles context
server_profiles_context = {
    'prefix': prefix,
    'organization': organization,
    'domain': 'domain',
    'profiles': [
        {'name': 'Server01', 'uuid': '0000-000000100001'},
        {'name': 'Server02', 'uuid': '0000-000000100002'}
    ],
    **vlan_settings,
    **vmedia_settings,
    **ipmi_settings
}

with open('1_UUID_Pool.yaml', 'w') as f:
    f.write(uuid_pool_template.render(**uuid_pool_context) + '\n')

with open('2_policies.yaml', 'w') as f:
    f.write(policies_template.render(**policies_context) + '\n')

with open('3_serverProfileTemplate.yaml', 'w') as f:
    f.write(template_template.render(**server_template_context) + '\n')

with open('4_server_profiles.yaml', 'w') as f:
    f.write(profiles_template.render(**server_profiles_context) + '\n')

print("Rendered files: 1_UUID_Pool.yaml, 2_policies.yaml, 3_serverProfileTemplate.yaml, 4_server_profiles.yaml")