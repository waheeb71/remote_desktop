#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
REMOTE DESKTOP ACTIVATION TOOL - HORROR THEME
Author: waheeb
Version: 2.0 - Dark Horror Edition (Ultra Fast Mode)
"""

import time
import subprocess
import sys
import os
import random
from datetime import datetime

# Horror ASCII Art
HORROR_ART = """
╔══════════════════════════════════════════════════════════════════╗
║  ██████╗ ███████╗███╗   ███╗██╗  ██╗███████╗                    ║
║  ██╔══██╗██╔════╝████╗ ████║██║  ██║██╔════╝                    ║
║  ██████╔╝█████╗  ██╔████╔██║███████║█████╗                      ║
║  ██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══██║██╔══╝                      ║
║  ██║  ██║███████╗██║ ╚═╝ ██║██║  ██║███████╗                    ║
║  ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝                    ║
║                                                                  ║
║  ███████╗██╗  ██╗██████╗ ███████╗██████╗ ██╗████████╗           ║
║  ██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝           ║
║  █████╗   ╚███╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║              ║
║  ██╔══╝   ██╔██╗ ██╔══██╗██╔══╝  ██╔══██╗██║   ██║              ║
║  ███████╗██╔╝ ██╗██║  ██║███████╗██║  ██║██║   ██║              ║
║  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝              ║
║                                                                  ║
║  ██████╗ ███████╗███╗   ██╗████████╗██████╗  █████╗ ██╗         ║
║  ██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██║         ║
║  ██████╔╝█████╗  ██╔██╗ ██║   ██║   ██████╔╝███████║██║         ║
║  ██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║██║         ║
║  ██║  ██║███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║███████╗    ║
║  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ║
╚══════════════════════════════════════════════════════════════════╝
"""

SKULL_ART = """
    ╔═══════════════════════════════════════════════════════╗
    ║          ██████╗ ███████╗███╗   ███╗███╗   ██╗     ║
    ║         ██╔═══██╗██╔════╝████╗ ████║████╗  ██║     ║
    ║         ██║   ██║███████╗██╔████╔██║██╔██╗ ██║     ║
    ║         ██║   ██║╚════██║██║╚██╔╝██║██║╚██╗██║     ║
    ║         ╚██████╔╝███████║██║ ╚═╝ ██║██║ ╚████║     ║
    ║          ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝     ║
    ╚═══════════════════════════════════════════════════════╝
"""

def print_horror(text, color="red", delay=0.001):
    """Print text with horror style - fast character print"""
    colors = {
        "red": "\033[91m",
        "dark_red": "\033[31m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "black": "\033[30m",
        "blood": "\033[38;5;88m",
        "reset": "\033[0m"
    }
    
    for char in text:
        sys.stdout.write(f"{colors.get(color, '')}{char}{colors['reset']}")
        sys.stdout.flush()
        if delay > 0:
            time.sleep(delay)
    print()

def print_skull():
    """Print skull with blood effect"""
    print_colored(SKULL_ART, "blood")

def print_colored(text, color="red", bold=False):
    """Print colored text"""
    colors = {
        "red": "\033[91m",
        "dark_red": "\033[31m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "blood": "\033[38;5;88m",
        "dark": "\033[38;5;234m",
        "reset": "\033[0m"
    }
    bold_code = "\033[1m" if bold else ""
    print(f"{bold_code}{colors.get(color, '')}{text}{colors['reset']}")

def horror_header():
    """Display horror themed header"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Blood drip effect
    print_colored("░" * 80, "blood")
    print_colored("▒" * 80, "dark_red")
    print_colored("▓" * 80, "red")
    print_colored("█" * 80, "dark_red")
    
    print_horror(HORROR_ART, "blood", 0.0005)
    
    # Glitch effect lines
    for _ in range(3):
        print_colored("▒" * random.randint(20, 60), "dark_red")
    
    print_colored("=" * 80, "blood")
    print_colored("  WELCOME TO THE DARK REMOTE DESKTOP  ", "red", True)
    print_colored("  ENTER AT YOUR OWN RISK...            ", "dark_red")
    print_colored("=" * 80, "blood")
    print()

def simulate_horror_loading(tool_name, duration=0.05):
    """Simulate loading with horror effects quickly"""
    print_colored("☠ LOADING:", "blood")
    print_horror(f"   {tool_name.upper()}...", "red", 0.002)
    
    steps = 15
    for i in range(steps + 1):
        progress = int((i / steps) * 100)
        bar = "█" * i + "░" * (steps - i)
        sys.stdout.write(f"\r   [{bar}] {progress}%")
        sys.stdout.flush()
        if duration > 0:
            time.sleep(duration / steps)
    
    print()
    print_colored("☠ LOADED SUCCESSFULLY!", "green")
    print_colored("   (OR IS IT?...)  ", "dark_red")

def check_prerequisites():
    """Check system with horror theme"""
    print_colored("☠ SCANNING THE ABYSS...", "blood")
    
    scary_messages = [
        "DETECTING SOULS...",
        "ANALYZING DARK ENERGY...",
        "CONNECTING TO THE VOID...",
        "AWAKENING THE ANCIENT ONES...",
        "READING BLOOD RUNES..."
    ]
    
    for msg in random.sample(scary_messages, 2):
        print_horror(f"   {msg}", "dark_red", 0.002)
    
    try:
        subprocess.run(["systemctl", "--version"], 
                      capture_output=True, 
                      check=True,
                      timeout=2)
        print_colored("☠ SYSTEMD PRESENT... THE RITUAL CAN BEGIN", "green")
        return True
    except:
        print_colored("☠ THE VOID IS EMPTY...", "red")
        return False

def display_evil_message():
    """Display evil messages during loading"""
    evil_msgs = [
        "YOU CAN'T ESCAPE...",
        "THE DARKNESS CONSUMES...",
        "YOUR SOUL IS MINE...",
        "NO RETURN FROM HERE...",
        "EMBRACE THE VOID..."
    ]
    return random.choice(evil_msgs)

def main():
    """Main horror function"""
    
    # Display header
    horror_header()
    
    # Print skull
    print_skull()
    
    # Evil intro
    print_colored("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠", "blood")
    print_horror("  THE RITUAL BEGINS...", "red", 0.005)
    print_colored("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠", "blood")
    print()
    
    # Display user information with evil style
    print_colored("☠ USER OF THE SHADOW:", "blood")
    print_colored(f"   NAME     : bunyanbank", "red")
    print_colored(f"   PASSWORD : 123", "dark_red")
    print_colored("   (YOUR IDENTITY IS NOW MINE)", "dark_red")
    print()
    
    # Check system
    if not check_prerequisites():
        print_colored("☠ SYSTEM MAY NOT SURVIVE THIS...", "red")
        print()
    
    # Horror tools
    tools = [
        "gnome-remote-desktop (THE GATE)",
        "xrdp (THE KEYMASTER)",
        "vnc-server (THE EYE)",
        "libvncserver (THE BLOOD)",
        "xorg-xrdp (THE SKELETON)",
        "gnome-session (THE SOUL)",
        "network-manager (THE WEB)",
        "openssl (THE ENCRYPTOR)"
    ]
    
    print_colored("☠ SUMMONING DEMONIC TOOLS...", "blood")
    print_colored("☠" * 60, "dark_red")
    print()
    
    # Simulate loading with horror - fast
    total_tools = len(tools)
    for idx, tool in enumerate(tools, 1):
        print_colored(f"[{idx}/{total_tools}] ☠ {display_evil_message()}", "dark_red")
        simulate_horror_loading(tool, duration=0.02)
        print()
    
    print_colored("☠" * 60, "blood")
    print_colored("☠ ALL TOOLS HAVE BEEN SUMMONED!", "green")
    print_colored("☠ THE GATE IS OPEN...", "blood")
    print()
    
    # Execute the ritual
    print_colored("☠ CASTING THE ACTIVATION SPELL...", "blood")
    
    print_colored("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠", "dark_red")
    print_horror("  ABRAHADABRA...", "red", 0.005)
    print_horror("  SIM SALABIM...", "red", 0.005)
    print_horror("  HOCUS POCUS...", "red", 0.005)
    print_colored("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠", "dark_red")
    print()
    
    try:
        # Execute command
        result = subprocess.run(
            ["systemctl", "--user", "start", "gnome-remote-desktop"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print_colored("☠☠☠ THE RITUAL IS COMPLETE! ☠☠☠", "green", True)
            print_colored("☠ REMOTE DESKTOP HAS AWAKENED!", "blood")
            print_colored("☠ THE DARKNESS NOW CONNECTS...", "red")
        else:
            print_colored("☠ THE SPELL FAILED!", "red")
            print_colored(f"☠ {result.stderr}", "dark_red")
            
    except subprocess.TimeoutExpired:
        print_colored("☠ THE VOID CONSUMED THE SPELL!", "red")
    except FileNotFoundError:
        print_colored("☠ THE ANCIENT TOOLS ARE MISSING!", "red")
    except Exception as e:
        print_colored(f"☠ DEMONIC ERROR: {e}", "red")
    
    print()
    print_colored("█" * 80, "blood")
    print_colored("  THE ABYSS AWAITS...  ", "dark_red")
    print_colored("█" * 80, "blood")
    
    # Connection information with horror style
    print()
    print_colored("☠ PORTALS TO THE DARKNESS:", "blood")
    print_colored(f"  RDP : localhost:3389  (THE GATE)", "red")
    print_colored(f"  VNC : localhost:5900  (THE EYE)", "dark_red")
    print_colored(f"  SSH : localhost:22    (THE WHISPER)", "blood")
    print()
    
    # User info with horror style
    print_colored("☠ SACRIFICE INFORMATION:", "blood")
    print_colored(f"  USER     : waheeb", "red")
    print_colored(f"  PASSWORD : 123", "dark_red")
    print_colored(f"  TIME     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "blood")
    
    print()
    print_colored("☠ DEMONIC MESSAGES:", "dark_red")
    final_messages = [
        "YOU'RE BEING WATCHED...",
        "THE EYES IN THE DARK SEE YOU...",
        "YOUR SCREEN IS NOW OURS...",
        "WELCOME TO THE OTHER SIDE...",
        "THERE'S NO ESCAPE NOW..."
    ]
    
    for msg in random.sample(final_messages, 3):
        print_horror(f"   ☠ {msg}", "blood", 0.005)
    
    print()
    print_colored("☠" * 80, "blood")
    print_colored("  PRESS ENTER TO RETURN TO THE LIVING...  ", "dark_red")
    print_colored("☠" * 80, "blood")
    print()

if __name__ == "__main__":
    try:
        main()
        input()  # Wait for enter
    except KeyboardInterrupt:
        print_colored("\n☠ YOU CANNOT ESCAPE THE DARKNESS!", "red")
        print_colored("☠ THE RITUAL WILL CONTINUE WITHOUT YOU...", "blood")
        sys.exit(0)
    except Exception as e:
        print_colored(f"\n☠ THE ABYSS CONSUMED YOU: {e}", "red")
        sys.exit(1)
