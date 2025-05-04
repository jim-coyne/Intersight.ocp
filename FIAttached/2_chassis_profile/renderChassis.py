from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

pools_template = env.get_template('1_pools.j2')
policies_template = env.get_template('2_policies.j2')
chassis_profile_template = env.get_template('3_chassis_profile.j2')

prefix = 'prefix.'
organization = 'default'
domain = 'domain'
chassisID = '01'
enableIB = False
enableOOB = True
inbandVLAN = 70

ippool_settings = {
    'ippoolGateway': '172.20.70.1',
    'ippoolNetmask': '255.255.255.0',
    'ippoolPrimaryDns': '172.20.70.60',
    'ippoolSecondaryDns': '172.20.70.59',
    'startAddr': '172.20.70.1',
    'endAddr': '172.20.70.250'
}

macPool_settings = {
    'AmacFrom': '00:25:B5:AA:10:00',
    'AblockSize': 256,
    'BmacFrom': '00:25:B5:AA:10:00',
    'BblockSize': 256
}

pools_context = {
    'prefix': prefix,
    'organization': organization,
     **macPool_settings,
     **ippool_settings
}

policies_context = {
    'prefix': prefix,
    'organization': organization,
    'enableIB': enableIB,
    'enableOOB': enableOOB,
    'inbandVLAN': inbandVLAN
}

chassis_context = {
    'prefix': prefix,
    'organization': organization,
    'domain': domain,
    'chassisID': chassisID
}

with open('1_pools.yaml', 'w') as f:
    f.write(pools_template.render(**pools_context) + '\n')

with open('2_policies.yaml', 'w') as f:
    f.write(policies_template.render(**policies_context) + '\n')

with open('3_chassis_profile.yaml', 'w') as f:
    f.write(chassis_profile_template.render(**chassis_context) + '\n')

print("Rendered files: 1_pools.yaml, 2_policies.yaml, 3_chassis_profile.yaml")
