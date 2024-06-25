# MenuDbg
# A simple tool to display system information
# Github: https://www.github.com/0x4248/MenuDbg
# Licence: GNU General Public License v3.0
# By: 0x4248

import os
from simple_term_menu import TerminalMenu
import argparse

tools = {
    "menus": {
        "Kernel": {
            "dmesg": {
                "description": "Display the message buffer of the kernel",
                "sudo": True,
                "commands": {
                    "Run dmesg": "sudo dmesg",
                    "Run dmesg with human mode": "sudo dmesg --human",
                    "Run dmesg with follow mode": "sudo dmesg --follow",
                    "Run dmesg with json output": "sudo dmesg --json"
                }
            },
            "lsmod": {
                "description": "Display the status of kernel modules",
                "sudo": True,
                "commands": {
                    "Run lsmod": "sudo lsmod"
                }
            },
            "uname": {
                "description": "Display system information",
                "sudo": False,
                "commands": {
                    "Run uname": "uname -a"
                }
            },
            "uptime": {
                "description": "Display system uptime",
                "sudo": False,
                "commands": {
                    "Run uptime": "uptime"
                }
            },
        },
        "Networking": {
            "ifconfig": {
                "description": "Display network interface configuration",
                "sudo": True,
                "commands": {
                    "Run ifconfig": "sudo ifconfig",
                    "Run ifconfig with all interfaces": "sudo ifconfig -a"
                }
            },
            "ip": {
                "description": "Display network interface configuration",
                "sudo": True,
                "commands": {
                    "Run ip": "sudo ip addr show",
                    "Run ip with all interfaces": "sudo ip addr show"
                }
            },
            "netstat": {
                "description": "Display network connections",
                "sudo": True,
                "commands": {
                    "Run netstat": "sudo netstat -tuln",
                    "Run netstat with all connections": "sudo netstat -tulna"
                }
            },
            "ss": {
                "description": "Display network connections",
                "sudo": True,
                "commands": {
                    "Run ss": "sudo ss -tuln",
                    "Run ss with all connections": "sudo ss -tulna"
                }
            },
        },
        "Processes": {
            "ps": {
                "description": "Display information about processes",
                "sudo": True,
                "commands": {
                    "Run ps": "ps aux",
                    "Run ps with all processes": "sudo ps auxf",
                    "Run ps with all processes and threads": "sudo ps auxfL",
                    "Run ps with all processes and threads in long format": "sudo ps auxfLww"
                }
            },
            "top": {
                "description": "Display information about processes",
                "sudo": True,
                "commands": {
                    "Run top": "sudo top"
    
                }
            },
            "htop": {
                "description": "Display information about processes",
                "sudo": True,
                "commands": {
                    "Run htop": "sudo htop",
                }
            },
        },
        "Users": {
            "who": {
                "description": "Display who is logged in",
                "sudo": True,
                "commands": {
                    "Run who": "who",
                    "Run who with all information": "who -a"
                },
            },
            "w": {
                "description": "Display who is logged in",
                "sudo": True,
                "commands": {
                    "Run w": "w",
                    "Run w with all information": "w -a"
                },
            }
        },
        "Disk": {
            "df": {
                "description": "Display disk usage",
                "sudo": True,
                "commands": {
                    "Run df": "sudo df -h",
                    "Run df with all filesystems": "sudo df -ha",
                    "Run df with all filesystems inodes": "sudo df -hai"
                }
            },
            "du": {
                "description": "Display disk usage",
                "sudo": True,
                "commands": {
                    "Run du": "sudo du -h",
                    "Run du with all directories": "sudo du -ha",
                    "Run du with all directories inodes": "sudo du -hai"
                }
            },
            "lsblk": {
                "description": "Display block devices",
                "sudo": True,
                "commands": {
                    "Run lsblk": "sudo lsblk",
                    "Run lsblk with all devices": "sudo lsblk -a"
                }
            },
            "fdisk": {
                "description": "Display disk partition information",
                "sudo": True,
                "commands": {
                    "Run fdisk": "sudo fdisk -l",
                    "Run fdisk with all devices": "sudo fdisk -la"
                }
            },
        },
        "Memory": {
            "free": {
                "description": "Display memory usage",
                "sudo": True,
                "commands": {
                    "Run free": "sudo free"
                }
            },
            "vmstat": {
                "description": "Display virtual memory statistics",
                "sudo": True,
                "commands": {
                    "Run vmstat": "sudo vmstat",
                    "Run vmstat with all information": "sudo vmstat -a"
                }
            }
        },
        "Power": {
            "acpi": {
                "description": "Display battery and power information",
                "sudo": True,
                "commands": {
                    "Run acpi": "sudo acpi",
                    "Run acpi with all information": "sudo acpi -a"
                }
            },
            "apm": {
                "description": "Display battery and power information",
                "sudo": True,
                "commands": {
                    "Run apm": "sudo apm",
                    "Run apm with all information": "sudo apm -a"
                }
            },
            "pmset": {
                "description": "Display battery and power information",
                "sudo": True,
                "commands": {
                    "Run pmset": "sudo pmset",
                    "Run pmset with all information": "sudo pmset -g"
                }
            },
            "upower": {
                "description": "Display battery and power information",
                "sudo": True,
                "commands": {
                    "Run upower": "sudo upower -i /org/freedesktop/UPower/devices/battery_BAT0",
                    "Run upower with all information": "sudo upower -i /org/freedesktop/UPower/devices/battery_BAT0"
                }
            }
        },
        "List commands": {
            "lscpu": {
                "description": "Display CPU information",
                "sudo": True,
                "commands": {
                    "Run lscpu": "sudo lscpu"
                }
            },
            "lspci": {
                "description": "Display PCI devices",
                "sudo": True,
                "commands": {
                    "Run lspci": "sudo lspci",
                    "Run lspci with all information": "sudo lspci -v"
                }
            },
            "lsmod": {
                "description": "Display kernel modules",
                "sudo": True,
                "commands": {
                    "Run lsmod": "sudo lsmod"
                }
            },
            "lsblk": {
                "description": "Display block devices",
                "sudo": True,
                "commands": {
                    "Run lsblk": "sudo lsblk",
                    "Run lsblk with all information": "sudo lsblk -a"
                }
            },
            "lsdev": {
                "description": "Display block devices",
                "sudo": True,
                "commands": {
                    "Run lsdev": "sudo lsdev",
                    "Run lsdev with all information": "sudo lsdev -a"
                }
            },
            "lsinitrd": {
                "description": "Display initrd information",
                "sudo": True,
                "commands": {
                    "Run lsinitrd": "sudo lsinitrd",
                    "Run lsinitrd with all information": "sudo lsinitrd -a"
                }
            },
            "lsmod": {
                "description": "Display kernel modules",
                "sudo": True,
                "commands": {
                    "Run lsmod": "sudo lsmod",
                    "Run lsmod with all information": "sudo lsmod -a"
                }
            }
        }
    }
}

def run_command(command):
    os.system(command)

def display_menu(menu, preview_function=None):
    options = list(menu.keys())
    terminal_menu = TerminalMenu(options, preview_command=preview_function)
    choice = terminal_menu.show()
    return options[choice] if choice is not None else None

def get_preview(menu, key):
    item = menu[key]
    if isinstance(item, dict):
        description = item.get("description", "No description available.")
        sudo = item.get("sudo", False)
        commands = item.get("commands", {})
        commands_list = "\n".join(f"- {cmd}" for cmd in commands.keys())
        return f"{key}\n{description}\n\nSudo: {sudo}\nCommands available:\n{commands_list}"
    return ""

def main():
    parser = argparse.ArgumentParser(description="A simple tool to display system information")
    parser.add_argument("--dont-quit", action="store_true", help="Don't quit after running a command")
    args = parser.parse_args()

    current_menu = tools["menus"]
    menu_stack = []

    while True:
        preview_function = lambda choice: get_preview(current_menu, choice)
        choice = display_menu(current_menu, preview_function)
        if choice is None:
            if menu_stack:
                current_menu = menu_stack.pop()
            else:
                break
        elif isinstance(current_menu[choice], dict):
            if "commands" in current_menu[choice]:
                command_choice = display_menu(current_menu[choice]["commands"])
                if command_choice is not None:
                    command = current_menu[choice]["commands"][command_choice]
                    run_command(command)
                    if not args.dont_quit:
                        break
            else:
                menu_stack.append(current_menu)
                current_menu = current_menu[choice]

if __name__ == "__main__":
    main()
