from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

uuid_pool_template = env.get_template('1_UUID_Pool.j2')
policies_template = env.get_template('2_policies.j2')
template_template = env.get_template('3_serverProfileTemplate.j2')
profiles_template = env.get_template('4_server_profiles.j2')

prefix = 'prefix.'
organization = 'default'

rcoe_settings = { # Control nodes
    'rcoeEnabled' : False,
    'ClassOfService' : '5',
    'QueuePairs' : '0',
    'ResourceGroups' : '0',
    'Version': '1'
}

TcpOffload_settings = { # Control nodes
    'LargeReceive' : True,
    'LargeSend' : True,
    'RxChecksum' : True,
    'TxChecksum' : True
}

w_rcoe_settings = { # Worker nodes
    'workerrcoeEnabled' : False,
    'workerClassOfService' : '5',
    'workerQueuePairs' : '0',
    'workerResourceGroups' : '0',
    'workerVersion': '1'
}

w_TcpOffload_settings = { # Worker nodes
    'workerLargeReceive' : True,
    'workerLargeSend' : True,
    'workerRxChecksum' : True,
    'workerTxChecksum' : True
}

device_connector_settings = { # Common
    'IntersightOnly': 'off'
}

vlan_settings = { # Control nodes
    'AllowedVlans': '"70"',
    'TrunkMode': 'TRUNK',
    'DefaultVLAN': '0'
}

w_vlan_settings = {    # Worker nodes
    'workerAllowedVlans': '"70"',
    'workerTrunkMode': 'TRUNK',
    'workerDefaultVLAN': '0'
}

vmedia_settings = { # Control nodes
    'bootVMedia': False,
    'vmediaEnable': True,
    'vmediaEncrypt': True,
    'LowPowerUsb': True,
    'Mappings': '[]'
}

w_vmedia_settings = { # Worker nodes
    'workerbootVMedia': False,
    'workervmediaEnable': True,
    'workervmediaEncrypt': True,
    'workerLowPowerUsb': True,
    'workerMappings': '[]'
}

localAdmin_settings = { # Control nodes
    'iamEnable': True,
    'Password': 'Cisco123',
    'EnablePasswordExpiry': False,
    'EnforceStrongPassword': True,
    'ForceSendPassword': False,
    'PasswordExpiryDuration': 90,
    'PasswordHistory': 0
}

w_localAdmin_settings = { # Worker nodes
    'workeriamEnable': True,
    'workerPassword': 'Cisco123',
    'EnablePasswordExpiry': False,
    'EnforceStrongPassword': True,
    'ForceSendPassword': False,
    'PasswordExpiryDuration': 90,
    'PasswordHistory': 0
}

lldp_settings = {  # Control Nodes
    'CdpEnabled' : True,
    'ForgeMac': 'allow',
    'ReceiveEnabled': True,
    'TransmitEnabled' : True,
    'MacRegistrationMode' : 'allVlans',
    'UplinkFailAction' : 'LinkDown'
}

w_lldp_settings = {  # Worker Nodes
    'workerCdpEnabled' : True,
    'workerForgeMac': 'allow',
    'workerReceiveEnabled': True,
    'workerTransmitEnabled' : True,
    'workerMacRegistrationMode' : 'allVlans',
    'workerUplinkFailAction' : 'LinkDown'
}

ipmi_settings = { # Both Nodes
    'Enable': False
}

ntp_settings = { # Both Nodes
    'EnableNTP': True,
    'NTPServer': '10.0.10.1'
}

sol_settings = { # Control Node
    'solEnabled': True
}

w_sol_settings = { # worker Node
    'workersolEnabled': True
}

smtp_settings = { # Both nodes
    'EnableSMTP': True,
    'SMTPServer': 'mailcisco.com',
    'SMTPPort': 25,
    'SMTPSender': 'cimc@cisco.com',
    'Email1': 'jicoyne@cisco.com'
}

ssh_settings = { # Control Nodes
    'EnableSSH': True,
    'SSHPort': 22,
    'SSHTimeout': 1800
}

w_ssh_settings = { # Worker Nodes
    'workerEnableSSH': True,
    'workerSSHPort': 22,
    'workerSSHTimeout': 1800
}

kvm_settings = { # Control node
    'EnableKVM': True,
    'AllowTunneledKVM': True
}

w_kvm_settings = {   # Worker node
    'workerEnableKVM': True,
    'workerAllowTunneledKVM': True
}

firmware_settings ={ # Control Node
    'BundleVersion': '5.2(0.230092)',
    'ModelFamily': 'UCSX-210C-M7'
}

w_firmware_settings ={  # Worker node
    'workerBundleVersion': '5.2(0.230092)',
    'workerModelFamily': 'UCSX-210C-M7'
}

uuid_pool_context = { 
    'prefix': prefix,
    'organization': organization,
    'uuid_block_from': '0000-000000100001',
    'uuid_block_size': 256
}

policies_context = {
    'prefix': prefix,
    'organization': organization,
    **device_connector_settings,
    **vlan_settings,
    **vmedia_settings,
    **ipmi_settings,
    **ntp_settings,
    **sol_settings,
    **smtp_settings,
    **ssh_settings,
    **kvm_settings,
    **localAdmin_settings,
    **lldp_settings,
    **firmware_settings,
    **rcoe_settings,
    **TcpOffload_settings,
    **w_rcoe_settings,
    **w_TcpOffload_settings,
    **w_vlan_settings,
    **w_vmedia_settings,
    **w_localAdmin_settings,
    **w_lldp_settings,
    **w_sol_settings,
    **w_ssh_settings,
    **w_kvm_settings,
    **w_firmware_settings
}

server_template_context = {
    'prefix': prefix,
    'organization': organization
}

server_profiles_context = {
    'prefix': prefix,
    'organization': organization
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