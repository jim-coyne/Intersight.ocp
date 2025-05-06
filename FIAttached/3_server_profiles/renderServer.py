from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

uuid_pool_template = env.get_template('1_UUID_Pool.j2')
policies_template = env.get_template('2_policies.j2')
template_template = env.get_template('3_serverProfileTemplate.j2')
profiles_template = env.get_template('4_server_profiles.j2')

prefix = 'prefix.'
organization = 'default'


vlan_settings = {
    'AllowedVlans': '"70"',
    'TrunkMode': 'TRUNK',
    'DefaultVLAN': '0'
}

eth_adapter_settings = {
    'EthAdapterAdvancedFilter': 'false',
    'EthAdapterArfsEnabled': 'false',
    'EthAdapterCompletionQueueCount': 2,
    'EthAdapterCompletionQueueRingSize': 1,
    'EthAdapterGeneveEnabled': 'false',
    'EthAdapterInterruptScaling': 'false',
    'EthAdapterInterruptCoalescingTime': 125,
    'EthAdapterInterruptCoalescingType': 'MIN',
    'EthAdapterInterruptCount': 4,
    'EthAdapterInterruptMode': 'MSIx',
    'EthAdapterNvgreEnabled': 'false',
    'EthAdapterPtpEnabled': 'false',
    'EthAdapterRoceClassOfService': 5,
    'EthAdapterRoceEnabled': 'false',
    'EthAdapterRoceMemoryRegions': 0,
    'EthAdapterRoceQueuePairs': 0,
    'EthAdapterRoceResourceGroups': 0,
    'EthAdapterRoceVersion': 1,
    'EthAdapterRssIpv4Hash': 'false',
    'EthAdapterRssIpv6ExtHash': 'false',
    'EthAdapterRssIpv6Hash': 'false',
    'EthAdapterRssTcpIpv4Hash': 'false',
    'EthAdapterRssTcpIpv6ExtHash': 'false',
    'EthAdapterRssTcpIpv6Hash': 'false',
    'EthAdapterRssUdpIpv4Hash': 'false',
    'EthAdapterRssUdpIpv6Hash': 'false',
    'EthAdapterRssSettings': 'false',
    'EthAdapterRxQueueCount': 1,
    'EthAdapterRxQueueRingSize': 512,
    'EthAdapterTcpLargeReceive': 'true',
    'EthAdapterTcpLargeSend': 'true',
    'EthAdapterTcpRxChecksum': 'true',
    'EthAdapterTcpTxChecksum': 'true',
    'EthAdapterTxQueueCount': 1,
    'EthAdapterTxQueueRingSize': 256,
    'EthAdapterUplinkFailbackTimeout': 5,
    'EthAdapterVxlanEnabled': 'false'
}

vmedia_settings = {
    'vMediaEnabled': 'true',
    'vMediaEncryption': 'true',
    'vMediaLowPowerUsb': 'true',
    'vMediaMappings': '[]',
    'bootVMedia': 'false'
}

ipmi_settings = {
    'Enable': 'false'
}

ntp_settings = {
    'EnableNTP': 'true',
    'NtpServers': ['1.1.1.1']
}

sol_settings = {
    'Enabled': 'true'
}

smtp_settings = {
    'EnableSMTP': 'true',
    'SMTPMinSeverity': 'critical',
    'SMTPSenderEmail': 'cimc@cisco.com',
    'SMTPRecipients': '["jicoyne@cisco.com"]',
    'SMTPServer': 'mail.cisco.com',
    'SMTPPort': 25
}

ssh_settings = {
    'EnableSSH': 'true',
    'SSHPort': 22,
    'SSHTimeout': 1800
}

kvm_settings = {
    'AllowTunneledKVM': 'true'
}

lldp_settings = {
    'CdpEnabled': 'true',
    'ForgeMac': 'allow',
    'LldpReceiveEnabled': 'true',
    'LldpTransmitEnabled': 'true',
    'MacRegistrationMode': 'allVlans',
    'UplinkFailAction': 'linkDown'
}

firmware_settings = {
    'FirmwareBundleVersion': '5.2(0.230092)',
    'FirmwareModelFamily': 'UCSX-210C-M7',
    'FirmwareTargetPlatform': 'FIAttached'
}

user_policy_settings = {
    'EnablePasswordExpiry': False,
    'EnforceStrongPassword': 'true',
    'ForceSendPassword': 'false',
    'GracePeriod': 0,
    'NotificationPeriod': 15,
    'PasswordExpiryDuration': 90,
    'PasswordHistory': 0,
    'UserRoleEnabled': 'true',
    'AdminPassword': 'Cisco123'
}

uuid_pool_context = {
    'prefix': prefix,
    'organization': organization,
    'mac_block_from': '00:25:B5:AA:10:00',
    'mac_block_size': 256,
    'uuid_prefix': '00000000-0010-0000',
    'uuid_block_from': '0000-000000100001',
    'uuid_block_size': 256,
    'server_serials': "'XXXXXXX','XXXXXXX','XXXXXXX','XXXXXXX'",
    'ip_gateway': '172.20.70.1',
    'ip_netmask': '255.255.255.0',
    'ip_primary_dns': '172.20.70.60',
    'ip_secondary_dns': '172.20.70.59',
    'ip_block_from': '172.20.70.1',
    'ip_block_to': '172.20.70.250'
}

policies_context = {
    'prefix': prefix,
    'organization': organization,
    **vlan_settings,
    **vmedia_settings,
    **ipmi_settings,
    **ntp_settings,
    **sol_settings,
    **smtp_settings,
    **ssh_settings,
    **kvm_settings,
    **lldp_settings,
    **user_policy_settings,
    **firmware_settings,
    **vmedia_settings,
    **smtp_settings,
    **eth_adapter_settings
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