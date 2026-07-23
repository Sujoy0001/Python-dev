from colorama import init

from app.organizer import FileOrganizer

init()

print("=" * 40)
print(" Production File Organizer ")
print("=" * 40)

organizer = FileOrganizer()

organizer.organize()

print("\nDone")