import monitoring
import stats
import system
import configs
import sys

def main():
    while True:
        print("----System and Telemetry Monitoring Menu----\n")
        print("1. System Monitor\n")
        print("2. Basic System Information\n")
        print("3. Statistics\n")
        print("4. Configuration\n")
        print("5. Exit\n")
        try:
            result = int(input())
        except ValueError: 
            print("You must enter a number from 1 to 5. Please try again.\n")
        match result:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Goodbye!")
                sys.exit()
main()