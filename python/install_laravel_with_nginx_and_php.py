import distro

def get_linux_distribution():
    os_info = distro.id()
    return os_info

os_info = get_linux_distribution()
print(os_info)

def run_command(command, check=True):
    result