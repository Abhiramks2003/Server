import win32security
import getpass

username = getpass.getuser()
print(f"Current username: {username}")

desc = win32security.GetFileSecurity(
    ".", win32security.OWNER_SECURITY_INFORMATION
)
sid = desc.GetSecurityDescriptorOwner()

sidstr = win32security.ConvertSidToStringSid(sid)
print("Sid is", sidstr)

