import pytube
from pytube import YouTube
from pytube.cli import on_progress
import pycolors
from pycolors import fore, back, style, init
import os

init.init()

clearScreen = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Main code function
def main():
    url = input(f"\nInsert the url: ")
    path = input(f"Choose the file path: ")
    print("")
    format = ["video", "audio", "both"]
    print("What do you want to download?\nOptions: Video, Audio, Both")
    choose = input(f"Choose: ").lower()

    if choose in format:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            print(f"\nDownloading {choose}\n")
            if choose == "video":
                yt.streams.filter(progressive=True, subtype='mp4').get_highest_resolution().download(
                    filename=f"VIDEO {yt.title}", output_path=path)
            elif choose == "audio":
                yt.streams.filter(only_audio=True, subtype='mp4').first().download(filename=f"AUDIO {yt.title}",
                                                                                   output_path=path)
            elif choose == "both":
                yt.streams.filter(progressive=True, subtype='mp4').get_highest_resolution().download(
                    filename=f"VIDEO {yt.title}", output_path=path)
                yt.streams.filter(only_audio=True, subtype='mp4').first().download(filename=f"AUDIO {yt.title}",
                                                                                   output_path=path)
        except Exception as e:
            print(f"{fore.RED}Error!{style.RESET} {e}")
    else:
        print(f"{fore.RED}Error! {style.RESET}{choose} {fore.RED}is not a valid input{style.RESET}")
        print('Valid inputs: ' + ', '.join(format))


def logo():
    print(f"{fore.LRED}")
    print("██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗")
    print("██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝")
    print("██████╔╝ ╚████╔╝    ██║   ██║   ██║██████╔╝█████╗")
    print("██╔═══╝   ╚██╔╝     ██║   ██║   ██║██╔══██╗██╔══╝")
    print("██║        ██║      ██║   ╚██████╔╝██████╔╝███████╗")
    print("╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝")
    print("Python based Youtube video downloader")
    print(f"{style.RESET}")

# Menu function
def start():
    clearScreen()
    logo()
    print(f"[{fore.LGREEN}1{style.RESET}] Start [{fore.LGREEN}2{style.RESET}] Tutorial [{fore.LGREEN}3{style.RESET}] Credits\n")
    section = ["1", "2", "3", "4", "start", "tutorial", "credits"]
    option = input("Option: ").lower()

    if option in section:
        if option == "1" or option == "start":
            main()
        if option == "2" or option == "tutorial":
            clearScreen()
            logo()
            print("Tutorial is coming soon\n")
            input("Press return to continue")
            start()
        if option == "3" or option == "credits":
            clearScreen()
            logo()
            print(f"Made by: {fore.CYAN}onlygiogi{style.RESET}")
            print(f"- GitHub: {fore.CYAN}gioggino{style.RESET}")
            print(f"- Discord: {fore.CYAN}onlygiogi#6477{style.RESET}")
            print(f"- Telegram: {fore.CYAN}@onlygiogi{style.RESET}")
            print(f"\nLibraries used:")
            print(f"- {fore.CYAN}pycolors{style.RESET}: colored output")
            print(f"- {fore.CYAN}pytube{style.RESET}: YouTube video downloader")
            print(f"- {fore.CYAN}os{style.RESET}: Interact with os\n")
            print(f"{fore.CYAN}Please give credits if you will use the code{style.RESET}\n")
            input("Press return to continue")
            start()
        if option == "4":
            pass
    else:
        print(f"{fore.RED}Error! {style.RESET}{option} {fore.RED}is not a valid input{style.RESET}")
        print('Valid inputs: ' + ', '.join(section))

start()

    #print(f"\n{Fore.GREEN}Title:{Style.RESET_ALL} {yt.title}\n{Fore.GREEN}Author:{Style.RESET_ALL} {yt.author}\n{Fore.GREEN}Views:{Style.RESET_ALL} {yt.views}\n{Fore.GREEN}Publish Date:{Style.RESET_ALL} {yt.publish_date}\n{Fore.GREEN}ID:{Style.RESET_ALL} {yt.video_id}\n{Fore.GREEN}Thumbnail:{Style.RESET_ALL} {yt.thumbnail_url}\n{Fore.GREEN}Description:{Style.RESET_ALL} {yt.description}{Style.RESET_ALL}\n")

#finally:
    #print(f"{fore.YELLOW}Exiting the software...{style.RESET}")