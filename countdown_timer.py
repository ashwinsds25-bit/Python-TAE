import time
import sys

# Platform-specific sound alert handling
try:
    import winsound  # Built-in for Windows
    WINDOWS = True
except ImportError:
    WINDOWS = False
    try:
        import os  # Fallback for Linux/macOS bell
    except ImportError:
        pass


def play_alarm():
    """Triggers an audio alert when the countdown finishes."""
    if WINDOWS:
        # 1000 Hz frequency for 2000 milliseconds (2 seconds)
        winsound.Beep(1000, 2000)
    else:
        # Terminal bell fallback for macOS / Linux
        sys.stdout.write('\a')
        sys.stdout.flush()


def countdown_timer():
    print("========================================")
    print("       PYTHON COUNTDOWN TIMER           ")
    print("========================================")

    try:
        # Prompt user for hours, minutes, and seconds to ensure exact input precision
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))

        # Convert everything into total seconds
        total_seconds = (hours * 3600) + (minutes * 60) + seconds

        if total_seconds <= 0:
            print("[-] Please enter a time greater than zero.")
            return

        print(f"\n[+] Timer started for {hours:02d}:{minutes:02d}:{seconds:02d}...\n")

        while total_seconds > 0:
            # Calculate hours, remaining minutes, and seconds
            mins, secs = divmod(total_seconds, 60)
            hrs, mins = divmod(mins, 60)

            # Format the time string as HH:MM:SS with zero-padding
            timer_display = f"\r[Time Remaining] {hrs:02d}:{mins:02d}:{secs:02d}"

            # Print using end="" and flush=True to overwrite the line smoothly in the terminal
            sys.stdout.write(timer_display)
            sys.stdout.flush()

            time.sleep(1)
            total_seconds -= 1

        # Final output when timer hits zero
        print("\r[Time Remaining] 00:00:00")
        print("\n========================================")
        print("          TIME'S UP! BEEP!              ")
        print("========================================")

        play_alarm()

    except ValueError:
        print("\n[!] Invalid input! Please enter valid integer numbers only.")
    except KeyboardInterrupt:
        print("\n\n[!] Timer manually interrupted by user.")


if __name__ == "__main__":
    countdown_timer()
